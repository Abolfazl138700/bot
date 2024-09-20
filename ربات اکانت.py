from pyrubi import Client
from time import sleep
bot = Client(session='bot')
guid = 'g0FIXVv08b7906adfe5505c84753a559'
account = []


while 1>0:
    try:
        last_message = bot.get_last_message(guid)['text']
        #print(last_message)
        sleep(2)
        message_id = bot.get_last_message(guid)['message_id']
        bot.unpin_message(guid, '%s'%message_id)
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



        

