# Google Form Automation with Selenium & Flask Email Service

A Python-based automation project that fills Google Forms using Selenium WebDriver and sends automated emails with attachments using Flask and SMTP.

## 🚀 Features

- **Automated Form Filling**: Uses Selenium WebDriver to automatically fill Google Forms
- **Dynamic Code Extraction**: Automatically extracts and fills verification codes from the form
- **Screenshot Capture**: Takes screenshots of form submission confirmation
- **Email Automation**: Flask-based web service for sending emails with attachments
- **SMTP Integration**: Secure email sending using Gmail SMTP with app passwords
- **Multiple Attachments**: Supports PDF, image, and video file attachments

## 📁 Project Structure

```
├── fill-form.py          # Main Selenium automation script
├── mail.py              # Flask web service for email automation
├── form_confirmation.png # Screenshot of successful form submission
├── demo-video.mp4       # Demo video of the automation
├── resume.pdf           # Resume attachment
└── requirements.txt     # Python dependencies
```

## 📦 Dependencies

- **selenium**: Web browser automation
- **webdriver-manager**: Automatic ChromeDriver management
- **flask**: Web framework for email service
- **smtplib**: Built-in SMTP email functionality
- **email**: Built-in email handling

## 🔍 Technical Details

### Selenium Implementation
- Uses Chrome WebDriver with automatic driver management
- Implements robust element selection using CSS selectors and XPath
- Handles dynamic content loading with appropriate wait times
- Executes JavaScript for reliable button clicking

### Email Service
- Flask-based REST API for email sending
- MIME multipart support for attachments
- Gmail SMTP with TLS encryption
- Error handling for missing attachments

### Form Automation Features
- **Dynamic Field Detection**: Automatically finds all input fields
- **Code Extraction**: Extracts verification codes from form elements
- **Screenshot Capture**: Saves confirmation screenshots
- **Error Handling**: Graceful handling of missing elements

## 🚨 Security Notes

- **App Passwords**: Use Gmail App Passwords instead of regular passwords
- **Environment Variables**: Consider using environment variables for sensitive data
- **Credentials**: Never commit passwords or sensitive information to version control
