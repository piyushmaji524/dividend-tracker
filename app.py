from flask import Flask, render_template, jsonify, send_file
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
from threading import Thread
import time
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)

# Cache for dividend data
dividend_cache = {
    'data': [],
    'last_update': None
}

# List of 50 popular Indian dividend-paying companies (NSE symbols)
STOCK_SYMBOLS = [
    # IT & Technology (8)
    'TCS.NS', 'INFY.NS', 'WIPRO.NS', 'HCL.NS', 'TECH.NS', 'MPHASIS.NS', 'MINDTREE.NS', 'LT.NS',
    
    # Banks & Financial Services (10)
    'HDFCBANK.NS', 'ICICIBANK.NS', 'AXISBANK.NS', 'SBIN.NS', 'INDUSIND.NS', 
    'KOTAKBANK.NS', 'FEDERALBNK.NS', 'IDFCFIRSTB.NS', 'AUBANK.NS', 'HDFC.NS',
    
    # Energy & Power (6)
    'RELIANCE.NS', 'NTPC.NS', 'POWERGRID.NS', 'COALINDIA.NS', 'ONGC.NS', 'OIL.NS',
    
    # Telecom (3)
    'BHARTIARTL.NS', 'VODAFONE.NS', 'IDEA.NS',
    
    # Automobiles (4)
    'MARUTI.NS', 'TATAMOTORS.NS', 'BAJAJ-AUTO.NS', 'HYUNDAI.NS',
    
    # Consumer & FMCG (8)
    'ITC.NS', 'HUL.NS', 'NESTLEIND.NS', 'BRITANNIA.NS', 'MARICO.NS', 
    'GODREJ.NS', 'HINDUNILVR.NS', 'COLPAL.NS',
    
    # Pharmaceuticals (4)
    'DRREDDY.NS', 'SUNPHARMA.NS', 'CIPLA.NS', 'LUPIN.NS',
    
    # Cement (2)
    'ULTRACEMCO.NS', 'AMBUJACEM.NS',
    
    # Infrastructure & Construction (3)
    'LARSENTOUB.NS', 'BHARATIFRA.NS', 'JSWSTEEL.NS',
    
    # Real Estate (1)
    'DLF.NS',
    
    # Insurance (2)
    'HDFCLIFE.NS', 'ICICIPRULI.NS'
]

# Sample dividend data for Indian companies with extended info
SAMPLE_DIVIDENDS = {
    'TCS.NS': {'name': 'Tata Consultancy Services', 'sector': 'IT', 'price': 3850, 'yield': 2.1, 'market_cap': '14.5L Cr', 'pe_ratio': 26.5, 'high_52w': 4200, 'low_52w': 3100, 'description': 'Leading IT services company'},
    'INFY.NS': {'name': 'Infosys Limited', 'sector': 'IT', 'price': 1980, 'yield': 1.5, 'market_cap': '8.2L Cr', 'pe_ratio': 24.3, 'high_52w': 2150, 'low_52w': 1650, 'description': 'Global IT consulting firm'},
    'WIPRO.NS': {'name': 'Wipro Limited', 'sector': 'IT', 'price': 380, 'yield': 3.2, 'market_cap': '3.8L Cr', 'pe_ratio': 18.2, 'high_52w': 450, 'low_52w': 320, 'description': 'IT services and consulting'},
    'HCL.NS': {'name': 'HCL Technologies', 'sector': 'IT', 'price': 1720, 'yield': 2.8, 'market_cap': '6.2L Cr', 'pe_ratio': 22.1, 'high_52w': 1950, 'low_52w': 1450, 'description': 'IT services provider'},
    'TECH.NS': {'name': 'Tech Mahindra', 'sector': 'IT', 'price': 1280, 'yield': 2.0, 'market_cap': '4.8L Cr', 'pe_ratio': 20.5, 'high_52w': 1550, 'low_52w': 1100, 'description': 'IT services company'},
    'MPHASIS.NS': {'name': 'Mphasis', 'sector': 'IT', 'price': 2850, 'yield': 1.8, 'market_cap': '2.1L Cr', 'pe_ratio': 19.2, 'high_52w': 3200, 'low_52w': 2400, 'description': 'IT services and BPO'},
    'MINDTREE.NS': {'name': 'MindTree Limited', 'sector': 'IT', 'price': 3680, 'yield': 1.5, 'market_cap': '2.8L Cr', 'pe_ratio': 21.8, 'high_52w': 4100, 'low_52w': 3100, 'description': 'Digital transformation services'},
    'LT.NS': {'name': 'Larsen & Toubro', 'sector': 'Infrastructure', 'price': 3950, 'yield': 1.9, 'market_cap': '4.5L Cr', 'pe_ratio': 23.4, 'high_52w': 4300, 'low_52w': 3200, 'description': 'Engineering & construction'},
    'HDFCBANK.NS': {'name': 'HDFC Bank Limited', 'sector': 'Banks', 'price': 1580, 'yield': 2.5, 'market_cap': '12.1L Cr', 'pe_ratio': 28.7, 'high_52w': 1850, 'low_52w': 1200, 'description': 'Leading private sector bank'},
    'ICICIBANK.NS': {'name': 'ICICI Bank Limited', 'sector': 'Banks', 'price': 1220, 'yield': 2.8, 'market_cap': '9.2L Cr', 'pe_ratio': 25.3, 'high_52w': 1450, 'low_52w': 950, 'description': 'Major private bank'},
    'AXISBANK.NS': {'name': 'Axis Bank Limited', 'sector': 'Banks', 'price': 1090, 'yield': 2.6, 'market_cap': '7.8L Cr', 'pe_ratio': 22.9, 'high_52w': 1300, 'low_52w': 850, 'description': 'Private sector bank'},
    'SBIN.NS': {'name': 'State Bank of India', 'sector': 'Banks', 'price': 890, 'yield': 3.5, 'market_cap': '8.5L Cr', 'pe_ratio': 19.2, 'high_52w': 1050, 'low_52w': 700, 'description': 'Largest public sector bank'},
    'INDUSIND.NS': {'name': 'IndusInd Bank', 'sector': 'Banks', 'price': 1450, 'yield': 2.1, 'market_cap': '1.9L Cr', 'pe_ratio': 24.1, 'high_52w': 1700, 'low_52w': 1100, 'description': 'Private sector bank'},
    'KOTAKBANK.NS': {'name': 'Kotak Mahindra Bank', 'sector': 'Banks', 'price': 2320, 'yield': 2.3, 'market_cap': '3.2L Cr', 'pe_ratio': 26.8, 'high_52w': 2700, 'low_52w': 1950, 'description': 'Premium banking services'},
    'FEDERALBNK.NS': {'name': 'Federal Bank Limited', 'sector': 'Banks', 'price': 185, 'yield': 2.9, 'market_cap': '1.2L Cr', 'pe_ratio': 20.5, 'high_52w': 220, 'low_52w': 140, 'description': 'Private sector bank'},
    'IDFCFIRSTB.NS': {'name': 'IDFC FIRST Bank', 'sector': 'Banks', 'price': 92, 'yield': 1.2, 'market_cap': '0.8L Cr', 'pe_ratio': 15.2, 'high_52w': 110, 'low_52w': 65, 'description': 'New private sector bank'},
    'AUBANK.NS': {'name': 'AU Small Finance Bank', 'sector': 'Banks', 'price': 650, 'yield': 2.0, 'market_cap': '0.9L Cr', 'pe_ratio': 18.3, 'high_52w': 800, 'low_52w': 500, 'description': 'Small finance bank'},
    'HDFC.NS': {'name': 'Housing Development Finance Corporation', 'sector': 'Finance', 'price': 2850, 'yield': 3.1, 'market_cap': '4.2L Cr', 'pe_ratio': 27.5, 'high_52w': 3200, 'low_52w': 2100, 'description': 'Housing finance company'},
    'RELIANCE.NS': {'name': 'Reliance Industries Limited', 'sector': 'Energy', 'price': 1280, 'yield': 1.8, 'market_cap': '15.2L Cr', 'pe_ratio': 32.1, 'high_52w': 1450, 'low_52w': 1050, 'description': 'Diversified conglomerate'},
    'NTPC.NS': {'name': 'NTPC Limited', 'sector': 'Energy', 'price': 320, 'yield': 5.2, 'market_cap': '2.8L Cr', 'pe_ratio': 14.2, 'high_52w': 380, 'low_52w': 250, 'description': 'Largest power producer'},
    'POWERGRID.NS': {'name': 'Power Grid Corporation of India', 'sector': 'Energy', 'price': 310, 'yield': 4.8, 'market_cap': '3.1L Cr', 'pe_ratio': 16.8, 'high_52w': 370, 'low_52w': 240, 'description': 'Transmission company'},
    'COALINDIA.NS': {'name': 'Coal India Limited', 'sector': 'Energy', 'price': 450, 'yield': 6.1, 'market_cap': '2.5L Cr', 'pe_ratio': 12.3, 'high_52w': 520, 'low_52w': 350, 'description': 'Coal mining company'},
    'ONGC.NS': {'name': 'Oil and Natural Gas Corporation', 'sector': 'Energy', 'price': 320, 'yield': 5.9, 'market_cap': '2.2L Cr', 'pe_ratio': 11.5, 'high_52w': 380, 'low_52w': 260, 'description': 'Oil & gas explorer'},
    'OIL.NS': {'name': 'Oil India Limited', 'sector': 'Energy', 'price': 540, 'yield': 4.2, 'market_cap': '0.9L Cr', 'pe_ratio': 13.2, 'high_52w': 650, 'low_52w': 420, 'description': 'Oil exploration company'},
    'BHARTIARTL.NS': {'name': 'Bharti Airtel Limited', 'sector': 'Telecom', 'price': 1750, 'yield': 2.4, 'market_cap': '4.2L Cr', 'pe_ratio': 85.3, 'high_52w': 1950, 'low_52w': 1400, 'description': 'Telecom service provider'},
    'VODAFONE.NS': {'name': 'Vodafone Idea Limited', 'sector': 'Telecom', 'price': 8.5, 'yield': 0.0, 'market_cap': '0.2L Cr', 'pe_ratio': 3.1, 'high_52w': 15, 'low_52w': 5, 'description': 'Telecom operator'},
    'IDEA.NS': {'name': 'Idea Cellular Limited', 'sector': 'Telecom', 'price': 7.2, 'yield': 0.0, 'market_cap': '0.15L Cr', 'pe_ratio': 2.8, 'high_52w': 12, 'low_52w': 4, 'description': 'Telecom services'},
    'MARUTI.NS': {'name': 'Maruti Suzuki India', 'sector': 'Auto', 'price': 10850, 'yield': 1.2, 'market_cap': '2.1L Cr', 'pe_ratio': 31.2, 'high_52w': 12000, 'low_52w': 8500, 'description': 'Car manufacturer'},
    'TATAMOTORS.NS': {'name': 'Tata Motors Limited', 'sector': 'Auto', 'price': 655, 'yield': 0.5, 'market_cap': '1.8L Cr', 'pe_ratio': 28.1, 'high_52w': 850, 'low_52w': 500, 'description': 'Auto manufacturing'},
    'BAJAJ-AUTO.NS': {'name': 'Bajaj Auto Limited', 'sector': 'Auto', 'price': 9850, 'yield': 1.1, 'market_cap': '1.5L Cr', 'pe_ratio': 35.2, 'high_52w': 11000, 'low_52w': 7800, 'description': 'Two and three wheeler manufacturer'},
    'HYUNDAI.NS': {'name': 'Hyundai Motor India', 'sector': 'Auto', 'price': 1955, 'yield': 2.3, 'market_cap': '1.2L Cr', 'pe_ratio': 40.1, 'high_52w': 2250, 'low_52w': 1500, 'description': 'Car manufacturer'},
    'ITC.NS': {'name': 'ITC Limited', 'sector': 'FMCG', 'price': 440, 'yield': 3.8, 'market_cap': '4.1L Cr', 'pe_ratio': 24.3, 'high_52w': 520, 'low_52w': 350, 'description': 'Diversified FMCG company'},
    'HUL.NS': {'name': 'Hindustan Unilever Limited', 'sector': 'FMCG', 'price': 2650, 'yield': 2.3, 'market_cap': '7.2L Cr', 'pe_ratio': 51.2, 'high_52w': 3000, 'low_52w': 2200, 'description': 'Leading FMCG company'},
    'NESTLEIND.NS': {'name': 'Nestlé India Limited', 'sector': 'FMCG', 'price': 2280, 'yield': 1.6, 'market_cap': '2.8L Cr', 'pe_ratio': 58.3, 'high_52w': 2600, 'low_52w': 1800, 'description': 'Food and beverages'},
    'BRITANNIA.NS': {'name': 'Britannia Industries Limited', 'sector': 'FMCG', 'price': 4850, 'yield': 0.9, 'market_cap': '2.3L Cr', 'pe_ratio': 45.2, 'high_52w': 5500, 'low_52w': 3800, 'description': 'Food products company'},
    'MARICO.NS': {'name': 'Marico Limited', 'sector': 'FMCG', 'price': 685, 'yield': 2.7, 'market_cap': '1.9L Cr', 'pe_ratio': 38.1, 'high_52w': 800, 'low_52w': 550, 'description': 'Consumer products'},
    'GODREJ.NS': {'name': 'Godrej Industries Limited', 'sector': 'FMCG', 'price': 880, 'yield': 1.5, 'market_cap': '0.8L Cr', 'pe_ratio': 35.2, 'high_52w': 1050, 'low_52w': 700, 'description': 'Consumer goods company'},
    'HINDUNILVR.NS': {'name': 'Hindustan Unilever (Personal Care)', 'sector': 'FMCG', 'price': 2650, 'yield': 2.3, 'market_cap': '7.2L Cr', 'pe_ratio': 51.2, 'high_52w': 3000, 'low_52w': 2200, 'description': 'Personal care products'},
    'COLPAL.NS': {'name': 'Colgate-Palmolive (India)', 'sector': 'FMCG', 'price': 2480, 'yield': 1.8, 'market_cap': '1.6L Cr', 'pe_ratio': 42.5, 'high_52w': 2850, 'low_52w': 1950, 'description': 'Oral care and hygiene'},
    'DRREDDY.NS': {'name': 'Dr. Reddy\'s Laboratories', 'sector': 'Pharma', 'price': 6785, 'yield': 1.2, 'market_cap': '4.8L Cr', 'pe_ratio': 29.3, 'high_52w': 7500, 'low_52w': 5200, 'description': 'Pharmaceutical company'},
    'SUNPHARMA.NS': {'name': 'Sun Pharmaceutical Industries', 'sector': 'Pharma', 'price': 780, 'yield': 0.8, 'market_cap': '2.1L Cr', 'pe_ratio': 26.2, 'high_52w': 950, 'low_52w': 600, 'description': 'Pharma manufacturer'},
    'CIPLA.NS': {'name': 'Cipla Limited', 'sector': 'Pharma', 'price': 1580, 'yield': 2.1, 'market_cap': '2.2L Cr', 'pe_ratio': 24.5, 'high_52w': 1850, 'low_52w': 1200, 'description': 'Pharmaceutical company'},
    'LUPIN.NS': {'name': 'Lupin Limited', 'sector': 'Pharma', 'price': 1845, 'yield': 1.5, 'market_cap': '1.9L Cr', 'pe_ratio': 28.1, 'high_52w': 2200, 'low_52w': 1400, 'description': 'Pharma company'},
    'ULTRACEMCO.NS': {'name': 'UltraTech Cement Limited', 'sector': 'Cement', 'price': 11850, 'yield': 1.3, 'market_cap': '3.2L Cr', 'pe_ratio': 32.5, 'high_52w': 13200, 'low_52w': 9000, 'description': 'Cement manufacturer'},
    'AMBUJACEM.NS': {'name': 'Ambuja Cements Limited', 'sector': 'Cement', 'price': 680, 'yield': 3.9, 'market_cap': '1.8L Cr', 'pe_ratio': 18.2, 'high_52w': 800, 'low_52w': 520, 'description': 'Cement producer'},
    'LARSENTOUB.NS': {'name': 'Larsen & Toubro Limited', 'sector': 'Infrastructure', 'price': 3950, 'yield': 1.9, 'market_cap': '4.5L Cr', 'pe_ratio': 23.4, 'high_52w': 4300, 'low_52w': 3200, 'description': 'Engineering & construction'},
    'BHARATIFRA.NS': {'name': 'Bharati Infrastructure', 'sector': 'Infrastructure', 'price': 250, 'yield': 2.5, 'market_cap': '0.5L Cr', 'pe_ratio': 19.8, 'high_52w': 320, 'low_52w': 180, 'description': 'Infrastructure company'},
    'JSWSTEEL.NS': {'name': 'JSW Steel Limited', 'sector': 'Steel', 'price': 920, 'yield': 2.6, 'market_cap': '2.8L Cr', 'pe_ratio': 21.3, 'high_52w': 1100, 'low_52w': 700, 'description': 'Steel manufacturer'},
    'DLF.NS': {'name': 'DLF Limited', 'sector': 'RealEstate', 'price': 850, 'yield': 3.2, 'market_cap': '1.2L Cr', 'pe_ratio': 25.1, 'high_52w': 1000, 'low_52w': 650, 'description': 'Real estate company'},
    'HDFCLIFE.NS': {'name': 'HDFC Life Insurance Company', 'sector': 'Insurance', 'price': 650, 'yield': 1.9, 'market_cap': '2.1L Cr', 'pe_ratio': 35.2, 'high_52w': 800, 'low_52w': 500, 'description': 'Life insurance company'},
    'ICICIPRULI.NS': {'name': 'ICICI Prudential Life Insurance', 'sector': 'Insurance', 'price': 680, 'yield': 1.5, 'market_cap': '1.8L Cr', 'pe_ratio': 38.1, 'high_52w': 850, 'low_52w': 520, 'description': 'Life insurance provider'},
}

def get_upcoming_dividends():
    """Fetch upcoming dividend declarations from local sample data"""
    upcoming_dividends = []
    today = datetime.now().date()
    
    # Generate sample dividend dates within next 10 days
    for i, (symbol, info) in enumerate(SAMPLE_DIVIDENDS.items()):
        try:
            # Distribute dividends across next 10 days
            days_until = (i % 10) + 1
            dividend_date = today + timedelta(days=days_until)
            
            # Ex-Dividend Date is typically 1 day before dividend announcement in India
            # You must own stock BEFORE ex-date to get dividend
            ex_dividend_date = dividend_date - timedelta(days=1)
            
            # Record Date - usually same or next day after ex-date
            record_date = ex_dividend_date + timedelta(days=1)
            
            # Distribution/Payment Date - typically 5-7 days after record date
            distribution_date = record_date + timedelta(days=6)
            
            # Check if buying today qualifies for dividend
            # Rule: You must own stock BEFORE ex-dividend date
            is_eligible_today = today < ex_dividend_date
            
            # Calculate dividend amount based on yield and price
            div_amount = (info['yield'] * info['price']) / 100
            
            # Calculate ROI for 1 year and 5 years
            annual_dividend = (info['yield'] * info['price']) / 100
            five_year_dividend = annual_dividend * 5
            
            upcoming_dividends.append({
                'symbol': symbol,
                'company_name': info['name'],
                'sector': info['sector'],
                'announcement_date': dividend_date.isoformat(),
                'ex_dividend_date': ex_dividend_date.isoformat(),
                'record_date': record_date.isoformat(),
                'distribution_date': distribution_date.isoformat(),
                'dividend_amount': round(div_amount / 4, 2),  # Quarterly dividend
                'current_price': round(info['price'], 2),
                'dividend_yield': round(info['yield'], 2),
                'days_until': days_until,
                'days_until_ex_date': (ex_dividend_date - today).days,
                'days_until_distribution': (distribution_date - today).days,
                'eligible_if_buy_today': is_eligible_today,
                'eligibility_status': 'QUALIFIED' if is_eligible_today else 'NOT QUALIFIED',
                'market_cap': info['market_cap'],
                'pe_ratio': info['pe_ratio'],
                'high_52w': info['high_52w'],
                'low_52w': info['low_52w'],
                'description': info['description'],
                'annual_dividend': round(annual_dividend, 2),
                'five_year_dividend': round(five_year_dividend, 2),
                'roi_1year': round(info['yield'], 2),
                'roi_5year': round(info['yield'] * 5, 2)
            })
        except Exception as e:
            pass
    
    # Sort by days until dividend
    upcoming_dividends.sort(key=lambda x: x['days_until'])
    
    return upcoming_dividends

def generate_shareable_card(dividends):
    """Generate a beautiful modern shareable card with improved spacing"""
    # Card dimensions - make it taller for better spacing
    width = 1200
    height = 2200
    
    # Create image with white background
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw gradient header
    header_height = 300
    for y in range(header_height):
        r = int(102 + (118 - 102) * (y / header_height))
        g = int(126 + (75 - 126) * (y / header_height))
        b = int(234 + (162 - 234) * (y / header_height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Try to load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 80)
        subtitle_font = ImageFont.truetype("arial.ttf", 50)
        header_font = ImageFont.truetype("arial.ttf", 45)
        data_font = ImageFont.truetype("arial.ttf", 42)
        small_font = ImageFont.truetype("arial.ttf", 38)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        data_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Get top 5 eligible companies
    eligible = [d for d in dividends if d['eligible_if_buy_today']][:5]
    
    # Draw header text - centered and clean
    draw.text((60, 80), "💰 DIVIDEND", fill=(255, 255, 255), font=title_font)
    draw.text((60, 170), "OPPORTUNITIES", fill=(255, 255, 255), font=title_font)
    
    today_str = datetime.now().strftime("%d %b %Y")
    draw.text((60, 260), f"📅 {today_str} • Top {len(eligible)} Companies", fill=(200, 200, 255), font=small_font)
    
    # Main content area with padding
    content_y = 350
    padding = 60
    
    # Draw separator line
    draw.line([(padding, content_y - 30), (width - padding, content_y - 30)], fill=(200, 210, 255), width=3)
    
    # Draw column headers background with better styling
    header_bg_y = content_y
    header_bg_height = 80
    draw.rectangle([(padding, header_bg_y), (width - padding, header_bg_y + header_bg_height)], 
                   fill=(245, 247, 255), outline=(102, 126, 234), width=4)
    
    # Column positions with better spacing
    col_positions = {
        'rank': padding + 40,
        'symbol': padding + 120,
        'company': padding + 280,
        'dividend': padding + 700,
        'date': padding + 950
    }
    
    # Draw column headers
    draw.text((col_positions['rank'], header_bg_y + 15), "#", fill=(102, 126, 234), font=header_font)
    draw.text((col_positions['symbol'], header_bg_y + 15), "Symbol", fill=(102, 126, 234), font=header_font)
    draw.text((col_positions['company'], header_bg_y + 15), "Company", fill=(102, 126, 234), font=header_font)
    draw.text((col_positions['dividend'], header_bg_y + 15), "Dividend", fill=(102, 126, 234), font=header_font)
    draw.text((col_positions['date'], header_bg_y + 15), "Date", fill=(102, 126, 234), font=header_font)
    
    # Draw data rows with increased height and spacing
    row_y = header_bg_y + header_bg_height + 20
    row_height = 180  # Increased row height to prevent overlap
    row_colors = [(250, 244, 255), (240, 248, 255)]  # Alternating colors
    border_colors = [(200, 210, 255), (180, 200, 255)]
    
    for i, div in enumerate(eligible):
        current_color = row_colors[i % 2]
        border_color = border_colors[i % 2]
        
        # Draw row background with rounded corners effect (using rectangles)
        draw.rectangle([(padding, row_y), (width - padding, row_y + row_height)], 
                      fill=current_color, outline=border_color, width=3)
        
        # Rank badge
        badge_x = col_positions['rank']
        badge_y = row_y + 30
        draw.ellipse([(badge_x - 25, badge_y - 25), (badge_x + 25, badge_y + 25)], 
                    fill=(102, 126, 234), outline=(255, 255, 255), width=3)
        draw.text((badge_x - 15, badge_y - 20), str(i + 1), fill=(255, 255, 255), font=header_font)
        
        # Symbol - bold and clear
        symbol_text = div['symbol']
        draw.text((col_positions['symbol'], row_y + 25), symbol_text, fill=(45, 50, 120), font=data_font)
        
        # Company name with better spacing
        company_name = div['company_name'][:25]
        draw.text((col_positions['company'], row_y + 25), company_name, fill=(80, 90, 160), font=small_font)
        
        # Dividend amount - highlighted
        div_text = f"₹{div['dividend_amount']:.2f}"
        draw.text((col_positions['dividend'], row_y + 25), div_text, fill=(34, 177, 76), font=data_font)
        
        # Distribution date
        dist_date = datetime.fromisoformat(div['distribution_date']).strftime("%d %b")
        draw.text((col_positions['date'], row_y + 25), dist_date, fill=(230, 126, 34), font=data_font)
        
        # Second row: Additional info
        yield_text = f"📊 Yield: {div['dividend_yield']}%"
        draw.text((col_positions['company'], row_y + 95), yield_text, fill=(155, 89, 182), font=small_font)
        
        # Status badge on second line
        status = "✓ BUY TODAY!" if div['eligible_if_buy_today'] else "✗ MISSED"
        status_color = (52, 152, 219) if div['eligible_if_buy_today'] else (192, 57, 43)
        draw.text((col_positions['symbol'], row_y + 95), status, fill=status_color, font=small_font)
        
        row_y += row_height + 25  # Add spacing between rows
    
    # Footer section with spacing
    footer_start_y = row_y + 40
    draw.line([(padding, footer_start_y), (width - padding, footer_start_y)], fill=(200, 200, 200), width=3)
    
    # Footer content
    footer_text1 = "📱 Share this insight with your investment community"
    footer_text2 = "💡 Dividend Tracker • Smart Investment Tool"
    footer_text3 = "🎯 Invest Wisely • Track Dividends Daily"
    
    draw.text((padding, footer_start_y + 50), footer_text1, fill=(80, 80, 80), font=small_font)
    draw.text((padding, footer_start_y + 110), footer_text2, fill=(100, 100, 100), font=small_font)
    draw.text((padding, footer_start_y + 170), footer_text3, fill=(120, 120, 120), font=small_font)
    
    # Bottom bar
    draw.rectangle([(0, height - 80), (width, height)], fill=(102, 126, 234))
    draw.text((60, height - 55), "www.dividendtracker.com • Made with ❤️ for Smart Investors", 
             fill=(255, 255, 255), font=small_font)
    
    return img

def update_dividend_cache():
    """Update cache every hour"""
    while True:
        try:
            dividend_cache['data'] = get_upcoming_dividends()
            dividend_cache['last_update'] = datetime.now().isoformat()
        except Exception as e:
            print(f"Error updating cache: {e}")
        
        # Update every hour
        time.sleep(3600)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dividends')
def get_dividends():
    """API endpoint to get upcoming dividends"""
    if not dividend_cache['data']:
        # Initial fetch if cache is empty
        dividend_cache['data'] = get_upcoming_dividends()
        dividend_cache['last_update'] = datetime.now().isoformat()
    
    return jsonify({
        'dividends': dividend_cache['data'],
        'last_update': dividend_cache['last_update'],
        'total_count': len(dividend_cache['data'])
    })

@app.route('/api/refresh')
def refresh_dividends():
    """Manual refresh endpoint"""
    try:
        dividend_cache['data'] = get_upcoming_dividends()
        dividend_cache['last_update'] = datetime.now().isoformat()
        return jsonify({
            'status': 'success',
            'message': 'Dividends updated successfully',
            'total_count': len(dividend_cache['data'])
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/generate-card')
def generate_card():
    """Generate and return shareable card image"""
    try:
        if not dividend_cache['data']:
            dividend_cache['data'] = get_upcoming_dividends()
        
        img = generate_shareable_card(dividend_cache['data'])
        
        # Save to bytes
        img_io = io.BytesIO()
        img.save(img_io, 'PNG', quality=95)
        img_io.seek(0)
        
        # Convert to base64 for inline display
        img_base64 = base64.b64encode(img_io.getvalue()).decode()
        
        return jsonify({
            'status': 'success',
            'image': f'data:image/png;base64,{img_base64}'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/download-card')
def download_card():
    """Download shareable card as PNG"""
    try:
        if not dividend_cache['data']:
            dividend_cache['data'] = get_upcoming_dividends()
        
        img = generate_shareable_card(dividend_cache['data'])
        
        # Save to bytes
        img_io = io.BytesIO()
        img.save(img_io, 'PNG', quality=95)
        img_io.seek(0)
        
        filename = f"dividend_tracker_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        
        return send_file(
            img_io,
            mimetype='image/png',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # Start background update thread
    update_thread = Thread(target=update_dividend_cache, daemon=True)
    update_thread.start()
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
