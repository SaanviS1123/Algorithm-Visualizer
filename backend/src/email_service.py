import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_signup_email(username, email):
    """Send email notification when user signs up"""
    try:
        sender_email = os.getenv('EMAIL_ADDRESS')
        sender_password = os.getenv('EMAIL_PASSWORD')
        
        # Email to admin (you)
        admin_email = sender_email
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "New User Signup!"
        message["From"] = sender_email
        message["To"] = admin_email
        
        text = f"""\
        New user has signed up!
        
        Username: {username}
        Email: {email}
        """
        
        html = f"""\
        <html>
          <body>
            <h2>New User Signup!</h2>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Email:</strong> {email}</p>
          </body>
        </html>
        """
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        
        message.attach(part1)
        message.attach(part2)
        
        # Send email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, admin_email, message.as_string())
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False