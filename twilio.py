from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACeeb845760b50a417872173a0c6605ba6"
# Your Auth Token from twilio.com/console
auth_token = "59c7864858f4e68c60211be94dc114cb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917018903309", from_="+17577045474", body="Hello from Deepanshu 123!"
)

print(message)
