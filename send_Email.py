import smtplib
import os


def send_email(sender, subject, message):
    recipient = 'cstephenson882@gmail.com'
    # Create an SMTP object
    with smtplib.SMTP("smtp.gmail.com", 587) as smpt:
        # Start TLS encryption
        smpt.starttls()
        # Login with your email and password

        #print(password)
        smpt.login(user="cstephenson882@gmail.com",password = os.getenv('PASSWORD'))
        # Create the email content
        content = f"Subject: {subject}\n\n{message}\n\n From: {sender}"
        # Send the email
        smpt.sendmail(sender, recipient, content)
        # Close the connection
        # smtp.quit()

send_email('cstephenson882@gmail.com','Hey you','This is a test email')


if __name__ == '__main__':
    send_email('test', 'test', 'test')