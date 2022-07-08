# Required Packages
import requests


# Some Required Dictionaries
Raw_Url_Pastebin_Link = ""
Timeout = 5
Headers = {'User-Agent': 'Script Tampering Checker (BOT)'}


# Main Function
def main():
    print("Hello World")


# Runner With Checker
if __name__ == "__main__":
    with open(__file__, "r") as read:
        if read != requests.get(url=Raw_Url_Pastebin_Link, timeout=Timeout).text:
            main()
        else:
            print(">>> Script Tampering Has Been Detected <<<\n\n - Tampering Protection v1.0 Detected That This Script Has Been Tampered In Some Way!!!")
