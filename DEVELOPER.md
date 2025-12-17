# 📊 Dividend Tracker - Developer Guide

**Developer:** Piyush Maji  
**Created:** December 2025  
**Project Type:** Flask Web Application  
**License:** Private - All Rights Reserved

---

## 🏗️ Project Architecture

```
dividend-tracker/
├── app.py                    # Flask backend & main application
├── requirements.txt          # Python dependencies
├── RUN_PROJECT.bat          # Windows batch file for easy launch
├── README.md                # User guide
├── DEVELOPER.md             # This file
├── templates/
│   └── index.html           # Frontend HTML template
└── static/
    ├── style.css            # Styling & layout
    └── script.js            # Frontend interactivity
```

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend** | Flask | 2.3.3 |
| **Frontend** | HTML5, CSS3, Vanilla JS | - |
| **Image Generation** | Pillow (PIL) | 10.0.0 |
| **Data Processing** | Pandas | 2.0.3 |
| **Server** | Werkzeug | 2.3.7 |
| **Web Framework** | Python | 3.x |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Development Setup

```bash
# Clone the repository
git clone https://github.com/piyushmaji524/dividend-tracker.git
cd dividend-tracker

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access at http://localhost:5000
```

### Quick Start (Windows)
Simply double-click `RUN_PROJECT.bat` - it handles everything!

---

## 🔧 Core Components

### Backend (app.py)

#### Key Data Structure: `SAMPLE_DIVIDENDS`
Dictionary containing 50 Indian NSE-listed companies with:
- Company name & sector
- Stock price & dividend yield
- Market cap & PE ratio
- 52-week high/low
- Company description

```python
"HDFC": {
    "name": "HDFC Bank",
    "sector": "Banks",
    "price": 1850.50,
    "dividend": 20.50,
    "yield": 1.11,
    ...
}
```

#### Critical Functions

**1. `get_upcoming_dividends()`**
- Generates dividend data for next 10 days
- Calculates key dates:
  - `ex_dividend_date = announcement_date - 1 day`
  - `record_date = ex_dividend_date + 1 day`
  - `distribution_date = record_date + 6 days`
- Determines eligibility: `is_eligible_today = today < ex_dividend_date`
- Calculates ROI metrics (1-year, 5-year)
- Returns: Sorted list of dividends by days_until

**2. `generate_shareable_card(dividends)`**
- Creates 1080x1920 PNG image (Instagram story size)
- Grid layout with columns: Symbol | Company | Dividend | Date
- Top 5 eligible companies displayed
- Features:
  - Gradient header (102,126,234 to 118,75,162)
  - Numbered badges (1-5)
  - Alternating row colors
  - Date & dividend information
- Returns: PIL Image object

**3. `update_dividend_cache()` (Background Thread)**
- Runs every 3600 seconds (1 hour)
- Updates `dividend_cache` dictionary
- Tracks `last_update` timestamp

#### API Endpoints

| Endpoint | Method | Returns | Purpose |
|----------|--------|---------|---------|
| `/` | GET | HTML | Serve main page |
| `/api/dividends` | GET | JSON | Get all dividends with last_update |
| `/api/refresh` | GET | JSON | Manual cache refresh |
| `/api/generate-card` | GET | Base64 PNG | Generate shareable card image |
| `/api/download-card` | GET | PNG File | Download card as file |

---

### Frontend (HTML/CSS/JS)

#### HTML Structure (templates/index.html)

**Main Sections:**
1. **Header** - Title & description
2. **Controls** - Refresh & Share buttons
3. **Sector Filters** - 11 filter buttons (All, IT, Banks, Energy, etc.)
4. **Search Box** - Company/symbol search
5. **Stats Card** - Company count
6. **Dividend Table** - 9 columns with sortable headers
7. **Modals** - Company info modal, Share modal
8. **Footer** - Branding + Visitor counter

#### CSS Styling (static/style.css)

**Key Classes & Styles:**
```css
.sector-filters     /* Filter button container */
.sector-btn         /* Individual filter button */
.sector-btn.active  /* Active filter state */
.modal              /* Modal overlay */
.modal-content      /* Modal content box */
.eligibility-badge  /* Qualified/Not qualified indicator */
.eligibility-badge.eligible      /* Green - ✓ */
.eligibility-badge.not-eligible  /* Red - ✗ */
.roi-section        /* ROI calculator section */
.roi-card           /* Individual ROI metric card */
.btn-share          /* Share button styling */
```

**Color Scheme:**
- Primary Gradient: `#667eea` → `#764ba2` (Purple)
- Eligible: `#2ecc71` (Green)
- Not Eligible: `#e74c3c` (Red)
- Alternating rows: `#faf4ff`, `#f0f8ff`

#### JavaScript (static/script.js)

**Global Variables:**
```javascript
let allDividends = [];      // Array of dividend objects
let sortDirection = {};     // Object tracking sort direction per column
let currentSectorFilter = 'all';  // Active sector filter
```

**Key Functions:**

| Function | Purpose |
|----------|---------|
| `fetchDividends()` | Call `/api/dividends`, populate table |
| `populateTable(dividends)` | Render table rows with onclick handlers |
| `filterTable()` | Apply search term + sector filter |
| `sortTable(columnIndex)` | Sort by column, toggle direction |
| `showCompanyInfo(symbol)` | Open modal with detailed company info |
| `generateShareableCard()` | Call `/api/generate-card`, display image |
| `downloadCard()` | Trigger browser download of PNG |
| `copyCardToClipboard()` | Copy image to clipboard |
| `initializeVisitorCounter()` | Initialize & update visitor count |

**Visitor Counter Logic:**
- Uses browser's `localStorage`
- Stores count in key: `dividendTrackerVisitors`
- Increments by 1 on each page load
- Persists across browser sessions

---

## 📊 Data Flow

```
User opens app
    ↓
HTML loads → Fetch /api/dividends
    ↓
Backend calculates upcoming dividends (next 10 days)
    ↓
Backend generates eligibility status
    ↓
JSON response → JavaScript populates table
    ↓
User sees companies with:
  - Symbol, Name, Dates, Dividend, Price, Yield
  - Eligibility status (Qualified/Not Qualified)
```

---

## 🔄 Dividend Calculation Logic

### Timeline Example
**Today:** Dec 17, 2025

```
Company A announces dividend Dec 20:
├─ Announcement Date: Dec 20
├─ Ex-Dividend Date: Dec 19 (announcement - 1 day)
├─ Record Date: Dec 20 (ex-date + 1 day)
├─ Distribution Date: Dec 26 (record + 6 days)
└─ Eligibility: Dec 17 < Dec 19 → ✓ QUALIFIED
```

If you buy today (Dec 17), you get the dividend!

---

## 🎨 Shareable Card Design

**Dimensions:** 1080x1920 px (Instagram Story size)

**Layout:**
```
┌─────────────────────┐
│ Header (Gradient)   │ (280px)
│ 💰 DIVIDEND...      │
└─────────────────────┘
│ Symbol│Company│Div│Date│ (70px - Column headers)
├─────────────────────┤
│ 1 │ TCS   │₹25 │12/20│ (150px per row)
├─────────────────────┤
│ 2 │ HDFC  │₹20 │12/25│
├─────────────────────┤
│ 3 │ INFY  │₹22 │01/05│
├─────────────────────┤
│ 4 │ ICICI │₹18 │12/28│
├─────────────────────┤
│ 5 │ BAJAJ │₹15 │01/10│
└─────────────────────┘
```

---

## 🔐 Visitor Counter Implementation

**Storage:** Browser LocalStorage
**Key:** `dividendTrackerVisitors`
**Persistence:** Across browser sessions & tabs

```javascript
// Get current count
let count = localStorage.getItem('dividendTrackerVisitors');

// Increment on each page load
localStorage.setItem('dividendTrackerVisitors', count + 1);

// Display in footer
document.getElementById('visitCount').textContent = count.toLocaleString();
```

---

## 🚀 Deployment

### Local Testing
```bash
python app.py
# Visit http://localhost:5000
```

### Production Deployment

**Option 1: Replit** (Easiest)
1. Go to [replit.com](https://replit.com)
2. Click "Create" → "Import from GitHub"
3. Select: `piyushmaji524/dividend-tracker`
4. Click "Run"
5. Share public link

**Option 2: Railway**
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Deploy automatically

**Option 3: Render**
1. Go to [render.com](https://render.com)
2. Create "New Web Service"
3. Connect GitHub repo
4. Deploy

---

## 📝 Modifying the Project

### Add New Company
Edit `app.py` in `SAMPLE_DIVIDENDS`:
```python
"NEW_SYMBOL": {
    "name": "Company Name",
    "sector": "Sector",
    "price": 1000.00,
    "dividend": 25.00,
    "yield": 2.50,
    "market_cap": "₹5,00,000 Cr",
    "pe_ratio": 20.5,
    "high_52w": 1200.00,
    "low_52w": 800.00,
    "description": "Description here"
}
```

### Add New Sector Filter
**In HTML** (templates/index.html):
```html
<button class="sector-btn" data-sector="NewSector">NewSector</button>
```

### Customize Colors
**In CSS** (static/style.css):
```css
/* Primary gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Card colors */
.eligible { background: #2ecc71; }
.not-eligible { background: #e74c3c; }
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 already in use | Change `app.run(port=5000)` to different port in app.py |
| Pillow not installed | `pip install Pillow==10.0.0` |
| Table not populating | Check `/api/dividends` response in browser console |
| Modal not opening | Verify symbol exists in `allDividends` array |
| Image generation fails | Ensure Pillow is installed & Arial font available |

---

## 📞 Developer Contact

**Project Owner:** Piyush Maji  
**GitHub:** [piyushmaji524](https://github.com/piyushmaji524)  
**Repository:** [dividend-tracker](https://github.com/piyushmaji524/dividend-tracker)

---

## 📄 License

**PRIVATE LICENSE - ALL RIGHTS RESERVED**

This project and all its contents are the exclusive property of Piyush Maji. Unauthorized copying, distribution, modification, or use of this software is strictly prohibited.

© 2025 Piyush Maji. All rights reserved.

---

**Last Updated:** December 17, 2025
