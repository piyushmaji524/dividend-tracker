# Dividend Tracker - Next 10 Days

A free, lightweight web tool that shows which companies will declare dividends within the next 10 days.

## Features

- 📊 Real-time dividend data from Yahoo Finance
- 📈 Beautiful, responsive UI
- 🔍 Search and filter companies
- 📅 Days-until countdown for each dividend
- 💰 Display dividend amount and yield
- 🔄 Auto-refresh capability
- ⚡ Fast and lightweight
- 📱 Mobile-friendly interface

## Installation

1. **Install Python 3.8+** from [python.org](https://www.python.org)

2. **Clone or download this project**

3. **Navigate to the project folder:**
   ```bash
   cd "d:\Digital Products\STOCK DEVIDENT"
   ```

4. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

3. The app will automatically fetch dividend data for popular stocks

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
