import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Retrieve the SendGrid API key from the environment variables
sendgrid_api_key = os.getenv('SENDGRID_API_KEY')

def send_notification_email(agent_email, name, property_id):
    message = Mail(
        from_email='nathanielmvana@gmail.com',
        to_emails=agent_email,
        subject='New Tenant Registration',
        html_content=f'<p>A new tenant, {name}, has registered interest in the property with ID {property_id}.</p>'
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))