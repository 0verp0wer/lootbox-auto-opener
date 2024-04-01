import time
import requests

from colorama import Fore, init
from modules.utils import Utils

init()

with open("tokens.txt", "r") as f:
    tokens = f.readlines()
    for i in tokens:
        token = i.rstrip()
        items_found = []
        
        headers = Utils.get_headers(token)
        
        while len(items_found) != 9:
            r = requests.post("https://discord.com/api/v9/users/@me/lootboxes/open", headers=headers).json()
            if 'retry_after' in r:
                print('[' + Fore.RED + '-' + Fore.RESET + ']' + 'ratelimited for ' + str(r['retry_after']) + 'second')
                time.sleep(r['retry_after'])
            else:
                items = r['opened_item']
                items_name = Utils.get_name_items(items)
                if items_name in items_found:
                    print('[' + Fore.BLUE + '?' + Fore.RESET + ']' + 'found:' + items_name)
                else:
                    print('[' + Fore.GREEN + '+' + Fore.RESET + ']' + 'found a new object:' + items_name)
                    items_found.append(items_name)
        
        r = requests.post("https://discord.com/api/v9/users/@me/lootboxes/redeem-prize", headers=headers)
        if r.status_code == 200:
            print('[' + Fore.GREEN + '+' + Fore.RESET + ']' + 'automatically redeemed clown decoration')
        else:
            print('[' + Fore.RED + '-' + Fore.RESET + ']' + 'failed to automatically redeeme clown decoration')