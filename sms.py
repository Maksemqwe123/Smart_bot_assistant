# from twilio.rest import Client
# import time
# account_sid = 'AC5b4d8cec61e8321b5d1931c5c89a4c40'
# auth_token = '31eeecfbc939d076403893d4396c9e1d'
# text = 'Вас взломали, переведите 10р на карту в течение часа \n9112 3841 0133 0961 \n02/25 \nИначе все ваши фотографии будут удалены '
# receiver = '+375292459132'
#
# # while True:
# client = Client(account_sid, auth_token)
# time.sleep(20)
# message = client.messages.create(
#     body=text,
#     from_='+13204411215',
#     to=receiver
# )


import pywhatkit

phone = '+375298555344'
message = 'привет'
while True:
    pywhatkit.sendwhatmsg_instantly(phone_no=phone, message=message)
