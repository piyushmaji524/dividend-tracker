# 📖 User Guide - Complete Tutorial

Welcome to Dividend Tracker! This guide will walk you through every feature step-by-step.

---

## 🎯 Getting Started

### Step 1: Open the Application
**Windows:** Double-click `RUN_PROJECT.bat`  
**Others:** Run `python app.py` in terminal

Open your browser to: **http://localhost:5000**

### Step 2: Understand the Layout
The page has 5 main sections:
1. **Header** - Title and description
2. **Controls** - Refresh and Share buttons
3. **Filters** - Sector buttons and search
4. **Table** - Dividend data
5. **Footer** - Credits and visitor count

---

## 🔍 Finding Companies

### Method 1: Browse All Dividends
When you open the app, you see all companies with dividends in next 10 days.

**What you see:**
- Symbol (e.g., "TCS")
- Company Name (e.g., "Tata Consultancy Services")
- Ex-Dividend Date (last day to buy)
- Record Date
- Distribution Date
- Dividend per share (₹)
- Current stock price (₹)
- Dividend yield (%)
- Eligibility status

### Method 2: Search by Company Name
**Steps:**
1. Type in search box: "HDFC"
2. Results filter automatically
3. Click ✕ button to clear

**Tips:**
- Search is case-insensitive
- Works with partial names ("HD" finds "HDFC")
- Works with symbols and full names

### Method 3: Filter by Sector
**Steps:**
1. Click a sector button (IT, Banks, Energy, etc.)
2. Table shows only that sector
3. You can click multiple sectors
4. Click "All Sectors" to reset

**Sectors available:**
- IT (Technology companies)
- Banks (Banking & financial)
- Energy (Power & oil)
- Finance (Financial services)
- FMCG (Consumer goods)
- Pharma (Pharmaceutical)
- Auto (Automobile)
- Telecom (Telecommunications)
- Infrastructure (Construction & real estate)

### Method 4: Sort by Column
**Steps:**
1. Click any column header (Symbol, Company, Ex-Date, etc.)
2. Column sorts A→Z or ascending
3. Click again to sort Z→A or descending
4. Arrow (↑↓) shows sort direction

**Best columns to sort by:**
- **Ex-Date:** See dividends by urgency
- **Dividend/Share:** See highest paying dividends
- **Yield %:** See best percentage returns
- **Days Left:** See deadline (sorted by Ex-Date)

---

## 📊 Understanding Dividend Information

### The 4 Most Important Pieces of Info

**1. Ex-Dividend Date** ⚠️
- Last date to BUY and get the dividend
- Buy BEFORE this date → You get dividend ✓
- Buy ON or AFTER → You don't ✗
- This date is KEY to the eligibility checker

**2. Dividend per Share** 💰
- Amount you receive per share held
- Example: If dividend is ₹25 and you own 100 shares → ₹2,500 total
- Paid once per dividend cycle

**3. Yield %** 📈
- Annual return percentage
- Formula: (Annual Dividend / Stock Price) × 100
- Higher yield = better return (but higher risk usually)
- Compare across companies

**4. Eligibility Status** ✓/✗
- **GREEN ✓ QUALIFIED:** You can buy today and get dividend
- **RED ✗ NOT QUALIFIED:** Ex-date passed, can't get dividend
- Updates automatically each day

---

## 💡 Using the Eligibility Checker

### What is Eligibility?
If you buy a stock today, will you get the next dividend?

### How It Works
1. App checks today's date
2. Compares with ex-dividend date
3. If today < ex-date → ✓ QUALIFIED
4. If today ≥ ex-date → ✗ NOT QUALIFIED

### Example Timeline
```
TODAY: Dec 17
Company A dividends:
- Ex-Date: Dec 19
- Status: ✓ QUALIFIED (you can still buy and get dividend)

Company B dividends:
- Ex-Date: Dec 17 (TODAY)
- Status: ✗ NOT QUALIFIED (too late to buy)

Company C dividends:
- Ex-Date: Dec 16 (Yesterday)
- Status: ✗ NOT QUALIFIED (ex-date already passed)
```

### Why It Matters
- Don't miss the deadline!
- Filter for ✓ QUALIFIED to find companies you can still buy
- ✗ NOT QUALIFIED are no longer eligible

---

## 👆 Clicking on a Company

### View Detailed Information
**Steps:**
1. Find a company in the table
2. Click on the row
3. A modal opens with detailed info

### What You See
**Company Header:**
- Stock Symbol
- Company Name
- Status (Eligible/Not Eligible)

**Key Information:**
- Current Stock Price (₹)
- Dividend per Share (₹)
- Dividend Yield (%)
- Market Cap (₹)
- PE Ratio (Price-to-Earnings)
- 52-week High (₹)
- 52-week Low (₹)

**ROI Information:**
- 1-Year Annual Dividend (₹)
- 1-Year Expected Return (%)
- 5-Year Dividend Projection (₹)
- 5-Year Expected Return (%)

### Understanding Each Metric

| Metric | Meaning |
|--------|---------|
| **Market Cap** | Total company worth |
| **PE Ratio** | Price relative to earnings (higher = more expensive) |
| **52-week High** | Highest price in last year |
| **52-week Low** | Lowest price in last year |
| **1-Year ROI** | Expected return if you hold for 1 year |
| **5-Year ROI** | Expected return if you hold for 5 years |

### Close the Modal
- Click the ✕ button
- Click outside the modal
- Press ESC key

---

## 📱 Generating Shareable Cards

### What is a Shareable Card?
A beautiful image showing the top 5 eligible dividend companies, perfect for sharing on social media.

### Steps to Generate

**Step 1:** Click "📱 Share Card" button

**Step 2:** Wait for image to generate (a few seconds)

**Step 3:** You see a beautiful card showing:
- Header: "💰 DIVIDEND OPPORTUNITIES"
- Columns: Symbol | Company | Dividend | Date
- Top 5 eligible companies
- Color-coded rows
- Your current date

### Downloading the Card

**Option 1: Download to Computer**
1. Image appears in modal
2. Click "⬇️ Download" button
3. File saves as `dividend-card-YYYY-MM-DD.png`
4. Find in Downloads folder

**Option 2: Copy to Clipboard**
1. Click "📋 Copy to Clipboard" button
2. Open WhatsApp, Instagram, etc.
3. Paste (Ctrl+V) to share
4. Works with most social media apps

### Where to Share
- **WhatsApp:** Paste in status or chat
- **Instagram:** Upload as post or story
- **Facebook:** Paste as image post
- **Twitter:** Upload as image
- **LinkedIn:** Share with colleagues

### Tips for Sharing
- Mobile friendly: Image is portrait (1080×1920)
- High quality: Perfect for Instagram stories
- Professional: Great for investor communities
- Easy: No editing needed!

---

## 🔄 Refreshing Data

### Manual Refresh
**Steps:**
1. Click "🔄 Refresh Data" button
2. Button disables for 5 seconds
3. Data updates
4. Table refreshes with new data

**When to refresh:**
- After a long time idle
- If data seems outdated
- To see if new companies appeared

### Automatic Refresh
- App updates every hour automatically
- Happens in background
- No action needed from you
- You'll see fresh data

### What Changes on Refresh?
- Companies in the 10-day window may change
- Eligibility status may change
- Days until dividend count down
- New companies may appear as others pass

---

## 👀 Monitoring Dividends

### Daily Habit (Best Practice)

**Every morning:**
1. Open the app
2. Check "✓ QUALIFIED" dividends
3. Decide which companies to buy
4. Note the Ex-Dates

**Key dates to track:**
- **Ex-Dates:** Buy before these dates
- **Record Dates:** You should own shares by this date
- **Distribution Dates:** When money arrives

### Understanding the Timeline
```
Day 1: Ex-Dividend Date
  └─ ✓ QUALIFIED (last day to buy and get dividend)

Day 2: Record Date
  └─ Company records who owns shares

Day 7: Distribution Date
  └─ Dividend credited to your account
```

---

## 📊 Making Investment Decisions

### Information to Consider

**1. Dividend Amount**
- Higher dividend = more money
- But higher risk sometimes
- Compare to company size (market cap)

**2. Dividend Yield %**
- High yield (>4%) = good return
- Compare to bank interest rates
- Historical highs/lows matter

**3. Company Health**
- PE Ratio: Lower is better (cheaper)
- Market Cap: Larger = more stable
- 52-week range: Shows volatility

**4. ROI Projections**
- 1-year ROI: Short-term returns
- 5-year ROI: Long-term potential
- Compare different companies

### Simple Decision Framework

```
1. Find ✓ QUALIFIED companies
2. Check dividend amount (higher = better)
3. Check yield % (compare to alternatives)
4. Check PE ratio (lower = cheaper)
5. Check 1-year ROI (expected return)
6. Decide based on your goals
```

---

## ❓ Common Scenarios

### Scenario 1: "I want highest dividend amount"
1. Click column "Dividend/Share"
2. Sort highest first
3. See top paying dividends
4. Check if ✓ QUALIFIED

### Scenario 2: "I want best percentage return"
1. Click column "Yield %"
2. Sort highest first
3. Filter for ✓ QUALIFIED
4. Compare top options

### Scenario 3: "I want stable, big companies"
1. Click on each company
2. Check Market Cap (larger = better)
3. Check 52-week range (smaller = more stable)
4. Check PE Ratio (lower = better value)

### Scenario 4: "I want IT sector dividends"
1. Click "IT" sector filter
2. See only IT companies
3. Sort by your preference
4. Choose from filtered list

### Scenario 5: "I want to share on social media"
1. Click "📱 Share Card"
2. Wait for image
3. Click "📋 Copy to Clipboard"
4. Open WhatsApp/Instagram
5. Paste and share!

---

## 🎓 Learning More

### Key Concepts to Understand

**Dividend:** Money paid to shareholders (you) from company profits

**Ex-Dividend Date:** Last date to buy and receive dividend

**Record Date:** Date company records shareholders (must own before this)

**Distribution Date:** When money is credited to your account

**Yield:** Annual return percentage on your investment

**ROI (Return on Investment):** Profit you expect to make

**Market Cap:** Total value of company

**PE Ratio:** Price compared to earnings (valuation metric)

### Resources

- [FEATURES.md](FEATURES.md) - Detailed feature list
- [FAQ.md](FAQ.md) - Answers to common questions
- [DEVELOPER.md](DEVELOPER.md) - Technical details

---

## 🆘 Troubleshooting

### Problem: "No dividends found"
**Solution:** Check current date. If it's end of month, fewer dividends may be scheduled.

### Problem: "Search not working"
**Solution:** 
- Refresh page
- Clear search box
- Try different spelling

### Problem: "Modal not opening"
**Solution:**
- Make sure JavaScript is enabled
- Try different browser
- Refresh page

### Problem: "Card not generating"
**Solution:**
- Wait a few seconds
- Refresh page
- Check internet connection

### Problem: "Table looks weird"
**Solution:**
- Refresh page (Ctrl+R)
- Hard refresh (Ctrl+Shift+R)
- Try different browser

---

## ⭐ Pro Tips

1. **Check eligibility first:** Always verify ✓ QUALIFIED status
2. **Sort by ex-date:** See most urgent dividends first
3. **Compare yields:** Higher isn't always better
4. **Check market cap:** Larger companies = more stable
5. **Share cards regularly:** Keep friends informed
6. **Monitor daily:** Dividends disappear from list after ex-date
7. **Take screenshots:** Save interesting opportunities
8. **Set calendar reminders:** Note important dates
9. **Track your purchases:** Remember which you bought
10. **Review history:** See which dividends you got

---

## 🎯 Final Checklist

Before buying a dividend-paying stock:

- [ ] Is it ✓ QUALIFIED?
- [ ] Is ex-date far enough away?
- [ ] Is dividend amount satisfactory?
- [ ] Is yield % competitive?
- [ ] Is company financially healthy?
- [ ] Do I have funds to buy?
- [ ] Is this part of my investment strategy?
- [ ] Have I checked the company fundamentals?

---

**Need more help?** Check [FAQ.md](FAQ.md) or open an issue on [GitHub](https://github.com/piyushmaji524/dividend-tracker/issues)

*Last Updated: December 17, 2025*
