# Security Policy

## 🔒 Supported Versions

We actively support the following versions of TikTok Ads Scraper with security updates:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | ✅ Yes             |
| < 1.0   | ❌ No              |

## 🚨 Reporting a Vulnerability

We take the security of TikTok Ads Scraper seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Where to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Send details to [your-email@example.com] (replace with your actual email)
2. **GitHub Security Advisories**: Use GitHub's private vulnerability reporting feature
3. **Direct Message**: Contact the maintainer directly through GitHub

### What to Include

Please include the following information in your report:

- **Type of issue** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s)** related to the manifestation of the issue
- **The location of the affected source code** (tag/branch/commit or direct URL)
- **Any special configuration** required to reproduce the issue
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**, including how an attacker might exploit the issue

### Response Timeline

We will respond to your report within **48 hours** and aim to:

- Confirm the problem and determine the affected versions
- Audit code to find any potential similar problems
- Prepare fixes for all supported releases
- Release patches and publish a security advisory

### Disclosure Policy

- We ask that you give us a reasonable amount of time to address the issue before any disclosure to the public or a third party
- We will credit you for the discovery in our security advisory (unless you prefer to remain anonymous)
- We will keep you informed of our progress toward a fix

## 🔐 Security Best Practices

### For Users

When using TikTok Ads Scraper, please follow these security guidelines:

1. **Credential Security**:
   - Never commit your TikTok Ads credentials to version control
   - Use environment variables or secure credential storage
   - Regularly rotate your passwords

2. **Session Management**:
   - The tool saves session state in `state.json` - keep this file secure
   - Delete `state.json` when no longer needed
   - Don't share session files

3. **Data Protection**:
   - Scraped data may contain sensitive information
   - Store output files securely
   - Consider encryption for sensitive data

4. **Network Security**:
   - Use secure networks when running the scraper
   - Be aware of network monitoring policies
   - Consider using VPN if required

### For Developers

If you're contributing to the project:

1. **Code Review**:
   - All code changes require review
   - Security-sensitive changes require additional scrutiny
   - Use static analysis tools when possible

2. **Dependencies**:
   - Keep dependencies up to date
   - Review dependency security advisories
   - Use tools like `pip audit` to check for vulnerabilities

3. **Authentication**:
   - Never hardcode credentials
   - Use secure authentication methods
   - Implement proper session handling

4. **Input Validation**:
   - Validate all user inputs
   - Sanitize file paths and URLs
   - Prevent injection attacks

## 🛡️ Known Security Considerations

### Current Limitations

1. **Credential Storage**: 
   - Login credentials are handled in-memory only
   - Session persistence uses Playwright's state management

2. **Browser Security**:
   - Uses Chromium browser with default security settings
   - Headless mode available but not enforced

3. **File Operations**:
   - Downloads videos to local filesystem
   - File paths are constructed from user input

### Planned Improvements

- [ ] Enhanced credential encryption
- [ ] Configurable security policies
- [ ] Audit logging
- [ ] Rate limiting controls

## 📊 Security Testing

We regularly perform security testing including:

- Static code analysis
- Dependency vulnerability scanning
- Manual security reviews
- Automated security testing in CI/CD

## 🔄 Security Updates

Security updates will be:

- Released as patch versions (e.g., 1.0.1)
- Announced in release notes
- Tagged with security labels
- Documented in security advisories

## 📞 Contact

For security-related questions that are not vulnerabilities:

- Open a GitHub issue with the "security" label
- Contact maintainers through GitHub discussions
- Email general inquiries to [your-email@example.com]

## 🏆 Recognition

We appreciate security researchers who help us maintain a secure project. Contributors who report valid security issues will be:

- Credited in our security advisory (if desired)
- Listed in our acknowledgments
- Invited to participate in future security discussions

---

Thank you for helping keep TikTok Ads Scraper and its users safe! 🙏 