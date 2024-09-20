from pyrubi import Client
from time import sleep

auth_key = "sbxhtcdauslmtnhytncavzacqyutjnof"

private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDJZ99ZXMBVx0Z1dbdF4BEPw4YQam07K5mJTUtw4+JAER/lO4UL\ntXbBw9E2xMgc/4BFAusKWOTdvdr0aek8UOUy+HxGS72ckWOTftN5GB3ql5l9qR4Z\nWgsYdutLjDC0p1sdODTV4QA1t9DBfYb4GNiORaC4P4xmN8zH0SM86aHqKwIDAQAB\nAoGABmR78xoL/MJVN2XcwvoBVC7epJITTbJ7IBGDNOwvnvksK+FxL/IQMapzxIB5\nUt3ahg8c383B1P2xVROGKfMm6j6jDK/87cCUR+OM6bAFvoPwsxJciL2mhaZW+HnJ\n+CI5dfdfOQeiT6G/13aM/OzuYuufb/Tn+2nlgApG3gJxybECQQDMMhpURoPzVEXk\nhbAXRC90YWspL3DFgsb6DvE5mkmPujVspYE+j8+GoabWL1yjlJwNxYKPi1C1YcsI\nRzt9S/4ZAkEA/ICR58JrehsBbeZc9J0IO2x8LqwbG88kfQRRljw0H9eUdMIi9YY3\n4gTS5XpuqB+anknxV1ivNj97qBRSpvuq4wJAXdCPJDUZnowTaIC7fJUJMHEpqMxx\nBW2mOXDwB0UJkw08SmRn0vSDphlS64jrCQTYBcO+znB1bkA15eHERTbK0QJBAIGc\n2ciWwybNwAES8/pYtUYTnPc0P0IaJYfK9Lpisvr5ZWo90UYpHHx3r24+V5kTiAHi\nwPDuRBpbofUYYYj3vLMCQQCk9bFS6nttJC3GBIptzyUfe5WemGRuSoNUWsERZbEE\nGQIj0rxlyvCxFd+lHB3+d8Rqjn+DZ+mubVwxdzZoicAh\n-----END RSA PRIVATE KEY-----"

bot = Client(auth=auth_key,private=private_key)
guid = 'g0FIXVv08b7906adfe5505c84753a559'
account = []

while 1>0:
    try:
        last_message = bot.get_last_message(guid)['text']
        #print(last_message)
        sleep(2)
        message_id = bot.get_last_message(guid)['message_id']
        #bot.reaction_message(guid, '%s'%message_id, 6)
        #x = bot.check_join('c0CRWUy0b0580ac9c047651cf2b38ebc', 'u0CrZrC00b41d55d42db10332d2e49b5')

        if last_message == 'ربات':
            bot.send_text(guid, 'بله؟', '%s'%message_id)
        give_account = last_message.startswith("اکانت:")
        if give_account:
            account.append(last_message)
            bot.send_text(guid, 'اکانت با موفقیت اضافه شد!','%s'%message_id)
            #print(last_message)
        elif last_message == 'اکانت':
            bot.send_text(guid, account[-1], '%s'%message_id)
        elif last_message == 'اکانت ها پاک':
            account.clear()
            bot.send_text(guid , 'تمام اکانت ها پاک شد!' , '%s'%message_id)

        elif last_message == 'اکانت ها':
            bot.send_text(guid, '%s'%account, '%s'%message_id)
        #print(account)

        sleep(2)

    except:
        continue
