import random
import string
import sys
import time
import webbrowser
import urllib.parse
import os

# ================= COLORS ================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ================= LINKS =================
FB_PROFILE = "https://www.facebook.com/Kristinemaeal"
FB_MESSENGER = "https://m.me/Kristinemaeal"

# ================= LOGO =================
def logo():
    print(CYAN + """
╔══════════════════════════════════════════╗
║      ███████╗██████╗     ██████╗        ║
║      ██╔════╝██╔══██╗   ██╔════╝        ║
║      █████╗  ██████╔╝   ██║             ║
║      ██╔══╝  ██╔══██╗   ██║             ║
║      ██║     ██████╔╝██╗╚██████╗        ║
║      ╚═╝     ╚═════╝ ╚═╝ ╚═════╝        ║
║           FACEBOOK CREATION TOOL          ║
╚══════════════════════════════════════════╝
""" + RESET)

# ================= LOADING =================
def loading(text="Processing"):
    spinner = ["|", "/", "-", "\\"]
    for i in range(20):
        sys.stdout.write(f"\r{YELLOW}{text} {spinner[i % 4]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# ================= KEY GENERATOR =================
def generate_key(last_digit):
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
    return f"{rand}-{last_digit}"

# ================= NOTE =================
def show_note():
    print(CYAN + """
┌──────────────────────────────────────────┐
│ NOTE:                                    │
│ Message the owner on Messenger to        │
│ activate your generated key              │
└──────────────────────────────────────────┘
""" + RESET)

# ================= ACTIVATION =================
def activate_tool(option, duration_name, price):
    loading("Checking Price")
    loading("Generating Key")

    key = generate_key(option)

    print(GREEN + """
┌──────────────────────────────────────────┐
│           ACTIVATION DETAILS             │
└──────────────────────────────────────────┘
""" + RESET)

    print(f"{CYAN}Duration :{RESET} {duration_name}")
    print(f"{CYAN}Price    :{RESET} {YELLOW}₱ {price}{RESET}")
    print(f"{CYAN}Key      :{RESET} {GREEN}{key}{RESET}")
    print(f"{CYAN}Profile  :{RESET} {BLUE}{FB_PROFILE}{RESET}")

    show_note()

    choice = input(YELLOW + "\nOpen Messenger now?[Y=yes] [N=no] (y/n): " + RESET).strip().lower()
    if choice == "y":
        open_messenger(key, duration_name, price)

# ================= OPEN MESSENGER =================
def open_messenger(key="", duration="", price=""):
    message = (
        "Hi Kristel,\n\n"
        "I'm purchasing your Tool as installation.\n\n"
        f"Selected Duration: {duration}\n"
        f"Price: ₱ {price}\n"
        f"Activation Key: {key}\n\n"
        "Thank you!"
    )

    encoded = urllib.parse.quote(message)
    link = f"{FB_MESSENGER}?text={encoded}"

    print(GREEN + "\nOpening Messenger...\n" + RESET)
    time.sleep(1)

    try:
        if sys.platform.startswith("linux"):
            os.system(f'am start -a android.intent.action.VIEW -d "{link}"')
        else:
            webbrowser.open_new_tab(link)
    except:
        print(RED + "Failed to open Messenger." + RESET)
        print(BLUE + link + RESET)

# ================= CONTACT OWNER =================
def contact_owner():
    print(CYAN + """
┌──────────────────────────────────────────┐
│  Contact Owner via Messenger             │
│  Pre-filled message will be used         │
└──────────────────────────────────────────┘
""" + RESET)

    confirm = input(YELLOW + "Continue? [Y=yes] [N=no] (y/n): " + RESET).strip().lower()
    if confirm != "y":
        print(RED + "\nCancelled.\n" + RESET)
        return

    open_messenger()

# ================= MENU =================
def menu():
    while True:
        print(GREEN + """
┌──────────────────────────────────────────┐
│        TOOL ACTIVATION MENU              │
├──────────────────────────────────────────┤
│  [1] 1 Day Duration                      │
│  [2] 3 Days Duration                     │
│  [3] 5 Days Duration                     │
│  [4] 1 Week Duration                     │
│  [5] 1 Month Duration                     │
│  [6] Contact Owner (Messenger)           │
│  [7] Exit                                │
└──────────────────────────────────────────┘
""" + RESET)

        choice = input(YELLOW + "Select option: " + RESET).strip()

        if choice == "1":
            activate_tool(1, "1 Day", 50)
        elif choice == "2":
            activate_tool(2, "3 Days", 100)
        elif choice == "3":
            activate_tool(3, "5 Days", 150)
        elif choice == "4":
            activate_tool(4, "1 Week", 190)
        elif choice == "5":
            activate_tool(5, "1 Month", 240)
        elif choice == "6":
            contact_owner()
        elif choice == "7":
            print(RED + "\nExiting tool. Goodbye!\n" + RESET)
            sys.exit()
        else:
            print(RED + "\nInvalid option. Try again.\n" + RESET)

# ================= MAIN =================
if __name__ == "__main__":
    logo()
    menu()