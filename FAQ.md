# ❓ Frequently Asked Questions (FAQ)

## General Questions

### Q1: Is Dividend Tracker free to use?
**A:** Yes! Absolutely free. No registration, no login, no hidden costs. The source code is available on GitHub for transparency.

### Q2: Do I need to install anything?
**A:** For Windows: Just double-click `RUN_PROJECT.bat` - everything installs automatically.  
For others: Install Python and run `pip install -r requirements.txt` then `python app.py`.

### Q3: Is it available online or only locally?
**A:** You can run it locally on your computer, or deploy it online for free using Replit, Railway, or Render.

### Q4: Which companies are included?
**A:** 50 major Indian NSE-listed companies across sectors like IT, Banks, Energy, FMCG, Pharma, Auto, Telecom, and Infrastructure.

### Q5: Can I add more companies?
**A:** Yes! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new companies.

---

## Dividend Information

### Q6: What is an ex-dividend date?
**A:** The last date you can buy shares to receive the upcoming dividend. If you buy on or after this date, you won't get the dividend.

### Q7: What is a record date?
**A:** The date the company records shareholders in their database. You must hold shares on this date to get the dividend.

### Q8: What is a distribution date?
**A:** The date when the dividend is actually credited to your account.

### Q9: If I buy today, will I get the dividend?
**A:** The app shows "✓ QUALIFIED" if you can buy today and get the dividend. It checks if today is before the ex-dividend date.

### Q10: How often does the dividend data update?
**A:** Data updates automatically every hour. The companies shown change daily as new dividends enter the 10-day window.

### Q11: Is the dividend data real-time?
**A:** The app uses sample data for reliability. For live data, you can integrate it with financial APIs like Yahoo Finance or Alpha Vantage.

---

## Technical Questions

### Q12: What technology is used?
**A:** Python (backend), Flask (web framework), HTML/CSS/JavaScript (frontend), Pillow (image generation).

### Q13: Is my data safe?
**A:** Yes! No user data is collected. No cookies or tracking (except an optional visitor counter). All data is local.

### Q14: Can I self-host this?
**A:** Yes! Clone from GitHub and run on your own server. See [DEVELOPER.md](DEVELOPER.md) for technical details.

### Q15: Does it work on mobile?
**A:** Yes! The interface is fully responsive and works on all devices (desktop, tablet, mobile).

### Q16: Why is the app showing an error?
**A:** Check that Python is installed and all dependencies are installed. See [Troubleshooting](DEVELOPER.md#troubleshooting) section.

---

## Features & Usage

### Q17: How do I search for a specific company?
**A:** Type the company name or stock symbol in the search box. Results filter in real-time.

### Q18: How do I filter by sector?
**A:** Click the sector buttons (IT, Banks, Energy, etc.). You can select multiple sectors at once.

### Q19: Can I sort the table?
**A:** Yes! Click any column header to sort. Click again to reverse the sort order.

### Q20: How do I view detailed company information?
**A:** Click on any company row in the table. A modal opens showing stock price, market cap, PE ratio, and ROI calculations.

### Q21: What does the ROI calculator show?
**A:** It shows projected 1-year and 5-year returns based on annual dividend yields.

### Q22: How do I generate a shareable card?
**A:** Click the "📱 Share Card" button. A beautiful image is generated showing the top 5 eligible companies. Download or copy to clipboard.

### Q23: Can I share the card on social media?
**A:** Yes! Download the image and share on WhatsApp, Instagram, Facebook, Twitter, etc.

### Q24: What is the visitor counter?
**A:** The footer shows total page visits stored in your browser. It increases by 1 each time you load the page.

---

## Deployment Questions

### Q25: How do I deploy this online for free?
**A:** You can deploy to:
- **Replit** (easiest) - Just import from GitHub
- **Railway** - GitHub integration
- **Render** - Auto-deploys on push
- See [README.md](README.md#deployment) for details.

### Q26: How do I deploy to Replit?
**A:** 
1. Go to [replit.com](https://replit.com)
2. Click "Create" → "Import from GitHub"
3. Paste: `https://github.com/piyushmaji524/dividend-tracker`
4. Click "Run" → Share public URL

### Q27: What's the live URL after deployment?
**A:** After deploying to Replit, you get a URL like: `https://dividend-tracker.yourname.repl.co`

### Q28: Can I use a custom domain?
**A:** Yes! Most hosting services support custom domains. Check their documentation.

### Q29: Will it cost anything after deployment?
**A:** No! These platforms offer free tiers. Your app will run 24/7 for free.

---

## Data & Privacy

### Q30: What data do you collect from me?
**A:** We don't collect any personal data. No login, no tracking, no accounts.

### Q31: Is my browsing history tracked?
**A:** No. The only "tracking" is an optional visitor counter using your browser's localStorage.

### Q32: Can I see the source code?
**A:** Yes! It's on GitHub at: [piyushmaji524/dividend-tracker](https://github.com/piyushmaji524/dividend-tracker)

### Q33: Is it safe to run locally?
**A:** Yes! All code is open source and transparent. You can review it before running.

---

## Support & Contact

### Q34: What if I find a bug?
**A:** Report it on GitHub: [Issues](https://github.com/piyushmaji524/dividend-tracker/issues)

### Q35: How do I suggest a feature?
**A:** Create an issue on GitHub or contact the developer.

### Q36: Who built this?
**A:** Built by Piyush Maji. See [DEVELOPER.md](DEVELOPER.md) for more info.

### Q37: Can I contribute to this project?
**A:** Yes! See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

### Q38: What if I need help?
**A:** 
- Check [GUIDE.md](GUIDE.md) for user guide
- Check [DEVELOPER.md](DEVELOPER.md) for technical help
- Report issues on GitHub

---

## License & Usage

### Q39: Can I use this commercially?
**A:** This is a private project. For commercial use, contact the developer.

### Q40: Can I modify and redistribute?
**A:** This project is private with all rights reserved. See [LICENSE](LICENSE) file.

### Q41: What about the data - can I use it elsewhere?
**A:** The dividend data in the app is sample data for demonstration. For real dividend data, use official financial APIs.

### Q42: Is there an API I can use?
**A:** The app provides internal APIs (`/api/dividends`, `/api/generate-card`). For external API access, contact the developer.

---

## Common Issues

### Q43: "Port 5000 already in use" error
**A:** Change the port in `app.py`. Replace `app.run(port=5000)` with `app.run(port=8000)`.

### Q44: "Module not found" error
**A:** Install dependencies: `pip install -r requirements.txt`

### Q45: Image generation fails
**A:** Make sure Pillow is installed: `pip install Pillow==10.0.0`

### Q46: Table not showing data
**A:** Check that the `/api/dividends` endpoint is working. Open browser console (F12) and check for errors.

### Q47: Search not working
**A:** Refresh the page and try again. Check browser console for errors.

### Q48: Modal not opening
**A:** Make sure JavaScript is enabled. Check browser console for errors.

---

## Performance & Optimization

### Q49: Why is the app slow?
**A:** The app is lightweight. Slowness usually indicates internet connection issues or browser problems. Try:
- Hard refresh (Ctrl+Shift+R)
- Clear cache
- Close other tabs

### Q50: Can I optimize it further?
**A:** The app is already optimized. For high traffic, consider upgrading the deployment server.

---

**Still have questions?** [Create an issue on GitHub](https://github.com/piyushmaji524/dividend-tracker/issues) or contact the developer!

---

*Last Updated: December 17, 2025*
