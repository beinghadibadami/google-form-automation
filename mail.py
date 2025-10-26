from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

@app.route('/send-assignment-email')
def send_assignment_email():
    sender = "hadibadami14@gmail.com"
    app_password = "hnju lleh eacx atec"
    to = "tech@themedius.ai"
    cc = "hr@themedius.ai"

    # Email setup
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = to
    msg["Cc"] = cc
    msg["Subject"] = "Python (Selenium) Assignment - Hadi Badami"

    # Email body
    body = """
Hello Team,

Please find my Selenium assignment submission below:

1. Screenshot of form confirmation (attached)
2. Video demo of the automation (attached)
3. GitHub Repo: https://github.com/beinghadibadami/google-form-automation
4. Approach: Automated using Python + Selenium + Flask + SMTP
5. Resume: Attached
6. Past Projects: https://carphd.com, https://codechat-jgxg.onrender.com/, https://vegvision.onrender.com/, https://hadi-portfolio-gn8n.onrender.com/
7. Availability: Full time (10 am - 7 pm) for 3–6 months.

Regards,  
Hadi Badami
"""
    msg.attach(MIMEText(body, "plain"))

    # --- Attachments ---
    attachments = [
        ("form_confirmation.png", "application", "octet-stream"),
        ("demo-video.mp4", "video", "mp4"),
        ("resume.pdf", "application", "pdf")
    ]

    for filename, maintype, subtype in attachments:
        try:
            with open(filename, "rb") as f:
                part = MIMEBase(maintype, subtype)
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            msg.attach(part)
        except FileNotFoundError:
            print(f"⚠️ File not found: {filename}, skipping attachment")

    # --- Send Email ---
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, app_password)
        smtp.send_message(msg)

    return "✅ Email sent successfully to tech@themedius.ai!"

if __name__ == "__main__":
    app.run(debug=True)
