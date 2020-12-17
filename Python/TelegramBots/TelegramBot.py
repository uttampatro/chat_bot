# -*- coding: UTF8 -*-
import requests
import datetime



class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '1412238433:AAGldTGuNYV3nv-LOa9uZCb0Gc0rEteBJhI' #Token of your bot
magnito_bot = BotHandler(token) #Your bot's name



def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=magnito_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'Hi':
                    magnito_bot.send_message(first_chat_id, 'Hello ' + first_chat_name)
                    new_offset = first_update_id + 1
                elif first_chat_text == 'I have to join engineering':
                    magnito_bot.send_message(first_chat_id, 'Ohh nice decision ')
                    new_offset = first_update_id + 1  
                elif first_chat_text == 'Which is the best department':
                    magnito_bot.send_message(first_chat_id, 'Information Technology ')
                    new_offset = first_update_id + 1  
                elif first_chat_text == 'Yes':
                    magnito_bot.send_message(first_chat_id, 'what can i do for you ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'How much fees for Information Technology course':
                    magnito_bot.send_message(first_chat_id, '1 lac ')
                    new_offset = first_update_id + 1
                elif first_chat_text == 'Ok thank you':
                    magnito_bot.send_message(first_chat_id, 'Welcome ')
                    new_offset = first_update_id + 1
                else:
                    magnito_bot.send_message(first_chat_id, 'Welcome '  + first_chat_name)
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
