def generate_twilio_token():
    from twilio.rest import Client
    account_sid = ''
    auth_token = ''
    twilio_token = Client(account_sid, auth_token)
    return twilio_token


def calling():
    client = generate_twilio_token()

    from_number = '【Twiloで購入した番号】'
    to_number = '【転送先の番号】'

    twiml = (
    '<Response>'
        '<Say voice="alice" language="ja-JP">'
            'こんにちわ, 世界!'
        '</Say>'
    '</Response>'
    )

    client.calls.create(
        twiml=twiml,
        to = to_number,
        from_ = from_number
    )


calling()