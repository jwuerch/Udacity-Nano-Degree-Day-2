from twilio import rest
import time

account_sid = "x" # Your Account SID from www.twilio.com/console
auth_token  = "x"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

while True:
    time.sleep(5)
    message = client.messages.create(
        body="Happy Birthday!",
        to="+15097143885",    # Replace with your phone number
        from_="+12017785264") # Replace with your Twilio number
    print(message.sid)
    print("Message sent successfully.")

