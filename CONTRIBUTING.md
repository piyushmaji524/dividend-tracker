# 🤝 Contributing Guidelines

Thank you for your interest in contributing to Dividend Tracker! We appreciate all types of contributions.

---

## 📋 Code of Conduct

### Our Commitment
We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Expected Behavior
- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discrimination
- Insulting/derogatory comments
- Personal attacks
- Public or private harassment
- Publishing private information without consent
- Violent language or threats

---

## 🐛 Reporting Bugs

### Before Reporting
1. Check [FAQ.md](FAQ.md) - Your question might be answered
2. Check [Troubleshooting](DEVELOPER.md#troubleshooting) section
3. Search [existing issues](https://github.com/piyushmaji524/dividend-tracker/issues) - Someone might have reported it
4. Test on latest version - Bug might be already fixed

### How to Report

**Create an issue on GitHub:**
1. Go to [Issues](https://github.com/piyushmaji524/dividend-tracker/issues)
2. Click "New Issue"
3. Choose "Bug report" template

**Include:**
- **Title:** Clear, concise description
- **Description:** What happened?
- **Steps to reproduce:** Exact steps to trigger bug
- **Expected behavior:** What should happen?
- **Actual behavior:** What actually happened?
- **Screenshots:** If applicable
- **Environment:**
  - OS (Windows, Mac, Linux)
  - Python version
  - Browser (if web-related)
  - App version

### Example Bug Report
```
Title: Shareable card not generating on Chrome

Steps to reproduce:
1. Open app in Google Chrome
2. Click "📱 Share Card"
3. Wait 5 seconds
4. Card doesn't appear

Expected: Card image should display
Actual: Blank space, no error message

Environment:
- OS: Windows 11
- Python 3.11
- Chrome 121
- App: Latest from main branch
```

---

## ✨ Suggesting Features

### Feature Request Process

1. Check [FEATURES.md](FEATURES.md) - Feature might exist
2. Check [Issues](https://github.com/piyushmaji524/dividend-tracker/issues) - Someone might have suggested it
3. Create new issue if not found

**Template:**
```
Title: [Feature] Add dark mode

Description:
Add a dark mode to reduce eye strain

Motivation:
Many users prefer dark interfaces for night browsing

Proposed Solution:
Add toggle button in settings
Apply dark CSS colors
Save preference in localStorage

Alternatives:
Use system preference (prefers-color-scheme)
```

### Good Feature Ideas
- UI improvements
- Additional companies
- New sectors
- Better visualizations
- Performance optimizations
- Documentation improvements
- Bug fixes with PR

### Less Likely to Be Accepted
- Features requiring paid APIs
- Breaking changes
- Major architecture rewrites
- Out-of-scope features (not dividend-related)

---

## 👨‍💻 Code Contributions

### Development Setup

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/dividend-tracker.git
cd dividend-tracker

# 3. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create feature branch
git checkout -b feature/your-feature-name

# 6. Make changes
# ... edit files ...

# 7. Test your changes
python app.py

# 8. Commit changes
git add .
git commit -m "Add your feature description"

# 9. Push to your fork
git push origin feature/your-feature-name

# 10. Create Pull Request on GitHub
```

### Code Style

**Python:**
- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Use meaningful variable names
- Add comments for complex logic
- Use type hints where applicable

**JavaScript:**
- Use 2 spaces for indentation
- Use const/let (not var)
- Use camelCase for variables
- Add comments for clarity
- Use meaningful function names

**HTML/CSS:**
- Use 4 spaces for indentation
- Use semantic HTML elements
- Use meaningful class names
- Keep CSS organized
- Use comments for sections

### Example: Adding a New Company

**File: app.py**

```python
SAMPLE_DIVIDENDS = {
    # ... existing companies ...
    "NEW_SYMBOL": {
        "name": "New Company Name",
        "sector": "IT",  # Use existing sector
        "price": 1000.00,
        "dividend": 25.00,
        "yield": 2.50,
        "market_cap": "₹1,00,000 Cr",
        "pe_ratio": 20.5,
        "high_52w": 1200.00,
        "low_52w": 800.00,
        "description": "Brief description of the company"
    }
}
```

**File: templates/index.html** (if new sector)

```html
<button class="sector-btn" data-sector="NewSector">NewSector</button>
```

### Testing Your Changes

1. **Run locally:**
   ```bash
   python app.py
   ```

2. **Test in browser:**
   - Open http://localhost:5000
   - Test all features
   - Test on mobile (DevTools)

3. **Check for errors:**
   - Open browser console (F12)
   - Look for JavaScript errors
   - Check network tab for failed requests

4. **Manual testing checklist:**
   - [ ] Search works
   - [ ] Filters work
   - [ ] Sorting works
   - [ ] Modal opens/closes
   - [ ] Card generates
   - [ ] Responsive on mobile
   - [ ] No console errors

---

## 📝 Documentation Contributions

### Types of Documentation
- User guides
- Developer guides
- README improvements
- FAQ additions
- Code comments
- Examples

### How to Contribute Docs

1. Identify documentation gap
2. Create branch: `git checkout -b docs/your-topic`
3. Write or update markdown files
4. Check grammar and spelling
5. Test code examples if applicable
6. Submit pull request

### Documentation Guidelines

- Use clear, simple language
- Include examples where helpful
- Use markdown formatting
- Add table of contents for long docs
- Keep formatting consistent
- Link to related sections
- Update "Last Updated" dates

---

## 📊 Data Contributions

### Adding New Companies

**Process:**
1. Verify company is NSE-listed
2. Get current stock price (from NSE website or broker)
3. Get dividend information (company website or announcement)
4. Add to SAMPLE_DIVIDENDS dictionary
5. Test thoroughly
6. Submit pull request

**Company Data Template:**
```python
"SYMBOL": {
    "name": "Full Company Name",
    "sector": "Existing Sector or New",
    "price": 1000.00,  # Current market price
    "dividend": 25.00,  # Announced dividend
    "yield": 2.50,  # dividend/price * 100
    "market_cap": "₹1,00,000 Cr",  # Company valuation
    "pe_ratio": 20.5,  # Price/Earnings
    "high_52w": 1200.00,  # 52-week high
    "low_52w": 800.00,  # 52-week low
    "description": "Brief company description"
}
```

### Adding New Sectors

**Process:**
1. Suggest new sector in issue
2. Get approval
3. Add to HTML filters
4. Add to Python if-statements
5. Add companies for that sector
6. Submit pull request

---

## 🚀 Pull Request Process

### Before Submitting PR

1. **Update main branch:**
   ```bash
   git checkout main
   git pull origin main
   git checkout your-feature-branch
   git rebase main
   ```

2. **Test thoroughly:**
   - All existing features still work
   - New feature works correctly
   - No console errors
   - No performance issues

3. **Update documentation:**
   - Update README.md if needed
   - Update FEATURES.md for new features
   - Add comments to code
   - Update CHANGELOG.md

4. **Clean up commits:**
   ```bash
   # Make logical commits (not too many tiny ones)
   # Write clear commit messages
   # Squash if needed
   ```

### Submitting PR

1. Push to your fork: `git push origin feature-name`
2. Go to GitHub and create Pull Request
3. Fill PR template completely:
   - **Title:** Clear description
   - **Description:** What does this do?
   - **Type:** Bug fix / Feature / Documentation
   - **Related Issues:** Link to related issues
   - **Testing:** How to test the changes
   - **Screenshots:** If UI changes

### PR Template Example
```
## Description
Add feature to generate shareable dividend cards

## Type
- [ ] Bug fix
- [x] Feature
- [ ] Documentation

## Related Issues
Fixes #123

## How to Test
1. Click "📱 Share Card" button
2. Image should generate in 2-3 seconds
3. Download should work
4. Copy to clipboard should work

## Screenshots
[Attach images if UI changed]

## Checklist
- [x] My code follows style guidelines
- [x] I've tested the changes
- [x] Documentation updated
- [x] No new warnings/errors
```

### Review Process

1. **Automated checks:**
   - Code syntax
   - Dependencies
   - File changes

2. **Manual review:**
   - Code quality
   - Logic correctness
   - Style consistency
   - Documentation

3. **Testing:**
   - Feature verification
   - Regression testing
   - Cross-browser testing

4. **Feedback:**
   - Changes might be requested
   - Respond to comments
   - Update PR with changes
   - Request re-review

---

## 🎓 Learning Resources

### For New Contributors

- [GitHub Guides](https://guides.github.com/)
- [How to Contribute](https://opensource.guide/how-to-contribute/)
- [Fork & Pull](https://guides.github.com/activities/forking/)
- [Making PRs](https://docs.github.com/en/pull-requests)

### Python Development

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Best Practices](https://docs.python-guide.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Frontend Development

- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [JavaScript Tips](https://javascript.info/)

---

## 💪 Types of Help Needed

### Easy First Issues
- Documentation improvements
- Adding new companies
- Fixing typos
- Small bug fixes
- Code comments

### Medium Issues
- New sectors
- UI improvements
- Feature enhancements
- Performance optimizations

### Hard Issues
- Live API integration
- Architecture changes
- Complex features
- Database implementation

---

## 🎁 Rewards

### Recognition
- Contributors listed in README
- Credit in commit messages
- Mention in project history
- Community respect

### Learning
- Improve programming skills
- Learn web development
- Understand open source
- Gain project experience

### Impact
- Help real users
- Improve product
- Build portfolio
- Join community

---

## ❓ Getting Help

### Questions?
- Check [FAQ.md](FAQ.md)
- Read [GUIDE.md](GUIDE.md)
- Check [DEVELOPER.md](DEVELOPER.md)
- [Create an issue](https://github.com/piyushmaji524/dividend-tracker/issues)

### Need Guidance?
- Comment on related issues
- Ask in PR discussions
- Email: piyushmaji524@gmail.com
- GitHub Discussions (if enabled)

---

## 📝 Changelog

### How to Update Changelog

When submitting PR, update `CHANGELOG.md`:

```markdown
## [Version X.X.X] - YYYY-MM-DD

### Added
- New feature description
- Another new feature

### Fixed
- Bug fix description
- Another bug fix

### Changed
- Change description

### Removed
- Deprecated feature
```

---

## 🙏 Thank You!

Your contributions help make Dividend Tracker better for everyone. We appreciate:

✅ Bug reports  
✅ Feature suggestions  
✅ Code contributions  
✅ Documentation improvements  
✅ Company data updates  
✅ Testing and feedback  
✅ Sharing the project  

**Thank you for being awesome!** ⭐

---

**Questions?** [Open an issue](https://github.com/piyushmaji524/dividend-tracker/issues)

*Last Updated: December 17, 2025*
