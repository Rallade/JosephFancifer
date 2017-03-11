from twilio.rest import TwilioRestClient  # put your own credentials here
ACCOUNT_SID = 'AC6d9f36ccdc6549e56751d189e472a181'
AUTH_TOKEN = '2576c8fed716de1fc158852500535635'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to='+447405703914',
    from_='+441290211282',
    body='From python',
)
