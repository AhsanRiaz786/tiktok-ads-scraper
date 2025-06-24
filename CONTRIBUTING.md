# Contributing to TikTok Ads Scraper

Thank you for your interest in contributing to TikTok Ads Scraper! We welcome contributions from the community and are grateful for any help you can provide.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Community](#community)

## 🚀 Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Make your changes
5. Test your changes
6. Submit a pull request

## 🛠️ Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account

### Local Setup

1. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/tiktok-ads-scraper.git
   cd tiktok-ads-scraper
   ```

2. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/AhsanRiaz786/tiktok-ads-scraper.git
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

5. **Install development dependencies:**
   ```bash
   pip install pytest black flake8 mypy
   ```

## 🎯 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug fixes**: Fix issues identified in the issue tracker
- **Feature enhancements**: Add new functionality or improve existing features
- **Documentation**: Improve README, add examples, or enhance code comments
- **Testing**: Add or improve test coverage
- **Performance**: Optimize code for better performance
- **UI/UX**: Improve the user interface and experience

### Before You Start

1. Check the [issue tracker](https://github.com/AhsanRiaz786/tiktok-ads-scraper/issues) for existing issues
2. For new features, open an issue to discuss your idea first
3. For bug fixes, ensure the bug hasn't already been reported
4. Search existing pull requests to avoid duplicates

## 📝 Coding Standards

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with these additional guidelines:

- Use 4 spaces for indentation
- Maximum line length: 88 characters
- Use descriptive variable and function names
- Add docstrings for all functions and classes
- Use type hints where possible

### Code Formatting

We use [Black](https://black.readthedocs.io/) for code formatting:

```bash
black .
```

### Linting

Run flake8 to check for style issues:

```bash
flake8 .
```

### Type Checking

Use mypy for type checking:

```bash
mypy .
```

## 🧪 Testing Guidelines

### Running Tests

```bash
pytest
```

### Writing Tests

- Write tests for all new functionality
- Ensure tests are descriptive and cover edge cases
- Mock external dependencies (TikTok API calls, file operations)
- Test files should be named `test_*.py`

### Test Coverage

Aim for at least 80% test coverage for new code:

```bash
pytest --cov=.
```

## 🔄 Pull Request Process

### Before Submitting

1. **Update your fork:**
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

4. **Run tests and linting:**
   ```bash
   black .
   flake8 .
   pytest
   ```

5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

### Pull Request Guidelines

- **Title**: Use a clear, descriptive title
- **Description**: Explain what your PR does and why
- **Reference Issues**: Link to related issues using `Fixes #123` or `Relates to #123`
- **Screenshots**: Include screenshots for UI changes
- **Testing**: Describe how you tested your changes
- **Documentation**: Update documentation if necessary

### PR Template

When you create a PR, please fill out our template with:

- [ ] Description of changes
- [ ] Type of change (bug fix, feature, docs, etc.)
- [ ] Testing performed
- [ ] Documentation updated (if applicable)
- [ ] Screenshots (if applicable)

## 🐛 Reporting Bugs

### Before Reporting

1. Search existing issues for duplicates
2. Try to reproduce the bug with the latest version
3. Check if it's already fixed in the main branch

### Bug Report Template

When reporting bugs, please include:

- **Environment**: OS, Python version, package versions
- **Steps to reproduce**: Clear, step-by-step instructions
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Screenshots/logs**: Any relevant visual aids or error messages
- **Additional context**: Any other relevant information

## 💡 Suggesting Features

### Feature Request Guidelines

1. **Check existing issues** for similar requests
2. **Open a discussion** before implementing large features
3. **Provide context** on why the feature would be valuable
4. **Consider backwards compatibility**
5. **Think about maintenance** burden

### Feature Request Template

- **Problem**: What problem does this solve?
- **Solution**: What would you like to see implemented?
- **Alternatives**: What alternatives have you considered?
- **Additional context**: Any other relevant information

## 📖 Documentation

### Documentation Standards

- Use clear, concise language
- Provide examples where helpful
- Keep documentation up-to-date with code changes
- Use proper Markdown formatting
- Include screenshots for UI features

### Types of Documentation

- **README**: High-level project overview
- **API docs**: Function and class documentation
- **Tutorials**: Step-by-step guides
- **Examples**: Sample code and use cases

## 🏷️ Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```
feat(scraper): add support for multiple regions
fix(gui): resolve login dialog not closing properly
docs(readme): update installation instructions
```

## 🏆 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes for significant contributions
- GitHub contributors page

## 📞 Community

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and community chat
- **Pull Requests**: Code contributions and reviews

## ❓ Questions?

If you have questions about contributing, feel free to:

1. Open an issue with the "question" label
2. Start a discussion in GitHub Discussions
3. Reach out to the maintainers

Thank you for contributing to TikTok Ads Scraper! 🎉 