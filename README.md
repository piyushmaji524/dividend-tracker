# 📊 Dividend Tracker - Free Web Application

**Track Indian Companies Declaring Dividends in Next 10 Days**

[![GitHub](https://img.shields.io/badge/GitHub-piyushmaji524-blue)](https://github.com/piyushmaji524/dividend-tracker)
[![License](https://img.shields.io/badge/License-Private-red)](#license)
[![Python](https://img.shields.io/badge/Python-3.7+-green)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-lightblue)](https://flask.palletsprojects.com/)

---

## 🎯 What is Dividend Tracker?

**Dividend Tracker** is a **free, open-source web application** that helps Indian stock market investors track companies declaring dividends within the next **10 days**. 

### Key Features:
✅ **Real-time Dividend Data** - See upcoming dividends for 50 NSE-listed companies  
✅ **Eligibility Checker** - Know if buying today qualifies you for dividends  
✅ **Distribution Timeline** - Ex-date, Record date, and Distribution date  
✅ **Sector Filtering** - Filter by IT, Banks, Energy, FMCG, Pharma, and more  
✅ **ROI Calculator** - Calculate 1-year and 5-year returns  
✅ **Shareable Cards** - Generate beautiful dividend cards for WhatsApp/Instagram  
✅ **Visitor Counter** - Track page visits with localStorage  
✅ **Responsive Design** - Works on desktop, tablet, and mobile  

---

## 🚀 Quick Start

### Option 1: Run Locally (Windows)
Simply **double-click** `RUN_PROJECT.bat` - that's it!

### Option 2: Run with Terminal
```bash
git clone https://github.com/piyushmaji524/dividend-tracker.git
cd dividend-tracker
pip install -r requirements.txt
python app.py
```

### Option 3: Deploy Online (Replit)
1. Go to [replit.com](https://replit.com)
2. Click "Create" → "Import from GitHub"
3. Select: `https://github.com/piyushmaji524/dividend-tracker`
4. Click "Run"

---

## 📊 Companies Tracked

**50 major Indian NSE-listed companies** across sectors:
- **IT:** TCS, Infosys, Wipro, HCL, Tech Mahindra
- **Banks:** HDFC Bank, ICICI Bank, Axis Bank, IndusInd Bank
- **Energy:** Reliance, NTPC, Power Grid
- **FMCG:** ITC, Nestlé, Unilever, Britannia
- **Pharma:** Cipla, Dr. Reddy's, Sunpharma
- **And more...**

---

## 🎨 Features in Detail

### 1. **Dividend Eligibility Checker**
Know if buying today qualifies you for upcoming dividends

### 2. **Three Important Dates**
- Ex-Dividend Date, Record Date, Distribution Date

### 3. **Advanced Filtering**
- Search by name/symbol, filter by sector

### 4. **Company Info Modal**
- Price, market cap, PE ratio, 52-week high/low

### 5. **ROI Calculator**
- 1-year and 5-year return calculations

### 6. **Shareable Cards**
- Generate beautiful 1080x1920px cards for social media

---

## 💻 Technology Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Backend |
| **Flask 2.3.3** | Web framework |
| **HTML5 + CSS3** | Frontend |
| **JavaScript** | Interactivity |
| **Pillow (PIL)** | Image generation |

---

## 📁 Project Structure

```
dividend-tracker/
├── app.py
├── requirements.txt
├── RUN_PROJECT.bat
├── README.md
├── DEVELOPER.md
├── FAQ.md
├── FEATURES.md
├── GUIDE.md
├── templates/index.html
└── static/style.css, script.js
```

---

## 🔧 Installation

1. **Install Python 3.7+**
2. **Clone the repository**
3. **Install dependencies:** `pip install -r requirements.txt`
4. **Run:** `python app.py`
5. **Open:** `http://localhost:5000`

## Features Explained

- **Symbol**: Stock ticker symbol
- **Company**: Company name
- **Dividend Date**: When the dividend will be declared
- **Days Until**: Countdown in days
- **Dividend/Share**: How much dividend per share
- **Price**: Current stock price
- **Yield %**: Annual dividend yield percentage

## Color Coding

- 🔴 **Red badge**: Dividend in 1 day (urgent)
- 🟡 **Yellow badge**: Dividend in 2-3 days
- 🟢 **Green badge**: Dividend in 4+ days

## Customization

### Adding More Stocks

Edit `app.py` and modify the `STOCK_SYMBOLS` list:

```python
STOCK_SYMBOLS = [
    'AAPL', 'MSFT', 'GOOGL', 'YOUR_SYMBOL', ...
]
```

### Data Source

This tool uses **yfinance** which provides free access to Yahoo Finance data. No API key required!

## How It Works

1. App fetches dividend data from Yahoo Finance for tracked stocks
2. Filters to show only dividends within next 10 days
3. Displays results in an interactive table
4. Auto-refreshes data every hour
5. You can manually refresh anytime with the "Refresh Data" button

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to 5001 or another port
```

### No Dividends Showing
- This is normal! Not all stocks declare dividends
- Only companies with upcoming dividends in next 10 days will show
- Market data updates daily

### Connection Issues
- Make sure you have internet connection
- yfinance requires internet to fetch data

## Technical Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Data Source**: Yahoo Finance (via yfinance)
- **Database**: None (all real-time data)

## License

Free to use, modify, and distribute

## Support

For issues or suggestions, feel free to modify and extend the code!

---

**Made with ❤️ for dividend investors**
