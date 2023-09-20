import requests
import Blixx

from time import sleep
from colorama import Fore

from util.plugins.common import SlowPrint, proxy

def WebhookSpammer(WebHook, Message):
    SlowPrint("\"ctrl + c\" at anytime to stop\n")
    sleep(1.5)
    while True:
        response = requests.post(
            WebHook,
            proxies=proxy(),
            json = {"content" : Message},
            params = {'wait' : True}
        )
        try:
            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.GREEN}Message sent{Fore.RESET}")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
                sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"{Fore.RED}Error : {response.status_code}{Fore.RESET}")

            sleep(.01)
        except KeyboardInterrupt:
            break

    SlowPrint(f'{Fore.RED}Spammed Webhook Successfully!{Fore.RESET} ')
    print("Enter anything to continue. . . ", end="")
    input()
    Blixx.main()