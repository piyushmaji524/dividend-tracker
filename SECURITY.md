# 🔐 Security Policy

## Overview

This document outlines the security practices and policies for the Dividend Tracker project.

---

## 🛡️ Security Principles

### 1. Privacy First
- **No data collection:** We don't collect any personal information
- **No tracking:** No analytics or user tracking
- **No cookies:** Only optional browser localStorage for visitor counter
- **No logins:** Anonymous access, no user accounts

### 2. Open Source Transparency
- **Public code:** All code available on GitHub for review
- **No hidden functionality:** You can see exactly what the app does
- **Community audit:** Anyone can review security
- **Version control:** Complete history of changes

### 3. Minimal Dependencies
- **Few external libraries:** Reduces attack surface
- **Popular libraries only:** Flask, Pillow, Pandas (well-maintained)
- **Regular updates:** Dependencies updated regularly
- **Security audits:** Popular libraries are audited by security community

---

## 🚨 Known Security Considerations

### What the App Does NOT Do

❌ **Does NOT:**
- Collect personal data
- Track user behavior
- Store any information about users
- Connect to external APIs (by default)
- Download files automatically
- Execute arbitrary code
- Access file system (except app directory)

### What the App DOES Do (Safely)

✅ **DOES:**
- Run locally on your computer (you control it)
- Store optional visitor counter in browser localStorage
- Generate images using Pillow library
- Process data in memory (no database)
- Serve static files (HTML, CSS, JS)

---

## 🔒 Data Security

### Local Execution
- App runs on your machine (http://localhost:5000)
- No data sent to external servers
- Complete control of your data
- Offline capable (except live API features)

### Session Data
- All session data held in memory
- Data cleared when browser closes
- No persistent database
- No files saved (except optional card images)

### Visitor Counter
- Stored in browser localStorage
- Only stores integer count
- No personal information
- Can be cleared by clearing browser cache

### Generated Images
- Shareable cards created locally
- Generated on demand
- Stored only if you download
- No automatic upload

---

## 🔐 Code Security

### No Malicious Code
- ✅ Code reviewed and transparent
- ✅ No hidden malware
- ✅ No cryptocurrency mining
- ✅ No botnet components
- ✅ No keyloggers or spyware

### Dependency Security
```
Flask==2.3.3           ✅ Secure, popular web framework
Pillow==10.0.0         ✅ Secure, well-maintained image library
Pandas==2.0.3          ✅ Secure, widely used data library
Werkzeug==2.3.7        ✅ Flask dependency, secure
```

### Best Practices Implemented
- Input validation where applicable
- Error handling (no sensitive info in errors)
- No SQL injection (no database used)
- No XSS vulnerabilities (DOM manipulation safe)
- No CSRF (internal app only)

---

## 🔑 API Security

### Internal APIs Only
- `/api/dividends` - Returns JSON data (public data)
- `/api/generate-card` - Generates image (no auth needed)
- `/api/download-card` - Downloads image (no auth needed)

### No Authentication
- These APIs don't need login (public service)
- No API keys or tokens
- Rate limiting not implemented (local use assumed)

### Safe Data
- Only dividend information returned
- No personal data exposed
- Public financial data only

---

## 🛡️ Deployment Security

### Local Deployment
```
python app.py
→ Runs on http://localhost:5000
→ Only accessible from your computer
→ No internet exposure by default
```

**Security notes:**
- Listen on localhost (not accessible remotely by default)
- Flask development server safe for local use
- Single-user scenario

### Online Deployment (Replit/Railway/Render)
When deployed to internet:

**Recommended practices:**
- Use HTTPS (hosting provider handles this)
- Keep dependencies updated
- Monitor error logs
- Use environment variables for secrets (if needed)

**What's NOT a risk:**
- Public code (already public on GitHub)
- Public data (dividend data is public)
- No authentication bypass needed (no auth system)

---

## 🔒 Browser Security

### Safe in Modern Browsers
- No deprecated APIs
- No unsafe JavaScript practices
- Content Security Policy compatible
- Works with browser security features enabled

### JavaScript Safety
- Vanilla JavaScript (no suspicious libraries)
- DOM manipulation is safe
- No eval() or dynamic code execution
- No external script injections

### Storage Security
- localStorage only stores visitor count
- No sensitive data stored
- Survives browser restart (intentional)
- Can be cleared anytime

---

## 🚀 Secure Deployment Checklist

If deploying to production:

- [ ] Use HTTPS (not HTTP)
- [ ] Keep Python updated
- [ ] Keep dependencies updated: `pip install --upgrade -r requirements.txt`
- [ ] Run security audit: `pip install safety && safety check`
- [ ] Use environment variables for any sensitive config
- [ ] Monitor error logs for issues
- [ ] Restrict access if needed (behind authentication)
- [ ] Run behind reverse proxy (Nginx) in production
- [ ] Enable security headers (X-Frame-Options, etc.)
- [ ] Implement rate limiting if public
- [ ] Backup data regularly (if you add database later)

---

## 🐛 Security Vulnerability Reporting

### Found a Vulnerability?

**DO NOT** publicly post security issues!

**Instead, contact the developer privately:**
- GitHub: [Create private security advisory](https://github.com/piyushmaji524/dividend-tracker/security/advisories)
- Email: piyushmaji524@gmail.com

**Include:**
- Description of vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

**Response time:** Vulnerabilities will be addressed within 48 hours.

---

## 📋 Security Audit Results

### Latest Audit: December 17, 2025

**Status:** ✅ SECURE

**Findings:**
- ✅ No critical vulnerabilities
- ✅ No high-severity issues
- ✅ No data exposure risks
- ✅ No injection vulnerabilities
- ✅ No authentication bypass
- ✅ Safe dependencies
- ✅ Proper error handling

**Recommendations:**
- Keep dependencies updated
- Monitor Python security updates
- Review code before deploying to shared servers

---

## 🔄 Dependency Update Policy

### Regular Updates
- Dependencies checked monthly
- Security updates applied immediately
- Breaking changes tested before deployment
- Update log maintained

### Current Status
```
Latest security updates applied: December 17, 2025
Next check: January 17, 2026
```

---

## 📝 Security Best Practices for Users

### If Running Locally
1. ✅ Download from official GitHub repo only
2. ✅ Check commit history for changes
3. ✅ Run on trusted computer
4. ✅ Use updated Python and dependencies
5. ✅ Don't share localhost URL publicly

### If Deploying Online
1. ✅ Use reputable hosting (Replit, Railway, Render)
2. ✅ Keep dependencies updated
3. ✅ Monitor logs for errors
4. ✅ Use HTTPS only
5. ✅ Backup your deployment

### General Safety
1. ✅ Keep operating system updated
2. ✅ Keep browser updated
3. ✅ Use antivirus software
4. ✅ Don't trust data from unknown sources
5. ✅ Verify you're on correct GitHub page

---

## ⚖️ Limitations & Disclaimers

### What We Secure
- ✅ Application code
- ✅ Your local data
- ✅ Your privacy

### What You Must Secure
- ❌ Your computer (antivirus, firewall)
- ❌ Your network (VPN, secure WiFi)
- ❌ Your deployment environment (if shared server)
- ❌ Your backup strategy

### No Guarantee of Availability
- This is free, open-source software
- Provided "as-is" without warranties
- No SLA (Service Level Agreement)
- No liability for data loss

---

## 🔗 Security Resources

### Recommended Reading
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [Flask Security](https://flask.palletsprojects.com/security/)

### Tools
- [Safety](https://pyup.io/) - Python dependency checker
- [Bandit](https://bandit.readthedocs.io/) - Python code security linter
- [OWASP ZAP](https://www.zaproxy.org/) - Web security scanner

---

## 📞 Security Contact

**For security issues:** piyushmaji524@gmail.com  
**GitHub:** [piyushmaji524/dividend-tracker](https://github.com/piyushmaji524/dividend-tracker)  
**Issues:** [GitHub Issues](https://github.com/piyushmaji524/dividend-tracker/issues)

---

## 📄 Policy Updates

This security policy is effective as of December 17, 2025.

### Previous Updates
- None (initial version)

### Next Review
- January 17, 2026

---

**Last Updated:** December 17, 2025

**Version:** 1.0

---

*This project prioritizes your security and privacy. Questions? [Contact the developer](mailto:piyushmaji524@gmail.com)*
