import requests
import time

# vk access token
# https://vkhost.github.io/
access_token = ''

# user ids
user_ids = [1, 2, 3]

# chat ids
peer_ids = [123]

# typing/audiomessasge
message_type = "audiomessage"

while True:
    try:
        for user_id in user_ids:
            url = f'https://api.vk.com/method/messages.setActivity?user_id={int(user_id)}&type={message_type}&access_token={access_token}&v=5.131'
            print(requests.get(url).text)
        for peer_id in peer_ids:
            url = f'https://api.vk.com/method/messages.setActivity?peer_id={int(peer_id) + 2000000000}&type={message_type}&access_token={access_token}&v=5.131'
            print(requests.get(url).text)
        time.sleep(2.5)
    except Exception as Ex:
        print(Ex)
