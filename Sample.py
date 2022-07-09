# Required Packages
import requests
import os


# Some Required Dictionaries
Raw_Url_Pastebin_Link = ""  # Example "https://pastebin.com/raw/HBpLcMCd"
Timeout = 5  # In Seconds
Headers = {'User-Agent': 'Script Tampering Checker (BOT)'}

Type = "Safe"
# Change This Part Based On The Info Bellow This Line
    # Safe - If The Script Has Been Tampered, It Will Just Notify The User And Stops The Script.
    # Unsafe - If The Script Has Been Tampered, It Will Remove The Script Itself Then Stops The Script. (Use At Your Own Risk)




# Main Function. (Insert Your Code Inside Of This Function)
def main():
    print("Hello World")



# Runner With Checker
if __name__ == "__main__":

    # Checks The File Itself If It Is Modified In Any Way Via "Raw_Url_Pastebin_Link"
    with open(__file__, "r") as read:

        # Tries If The User Who Is Using This Script Is Online
        try:

            # Compares This Local Python File To The "Raw_Url_Pastebin_Link" As Text. If Valid, Then It Will Just Go To "main" Function
            if read != requests.get(url=Raw_Url_Pastebin_Link, timeout=Timeout).text:
                main()
            # If Not, It Will Show A Problem And Terminate The Script.
            else:

                def Safe():
                    # Prompting The User
                    print(">>> Script Tampering Has Been Detected <<<\n\n - Tampering Protection v1.0 Detected That This Script Has Been Tampered In Some Way!!!")
                    # Then Exit
                    exit()

                def Unsafe():
                    # Prompting The User
                    print(">>> Script Tampering Has Been Detected <<<\n\n - Tampering Protection v1.0 Detected That This Script Has Been Tampered In Some Way!!!")
                    # Removing The File Itself Based On What Operating System They Are Using It
                    if os.name == "posix":
                        os.system(f'rm -rf {__file__}')
                    else:
                        os.system(f'del {__file__} /q')
                    # Then Exit
                    exit()

                # Decides What To Run
                if Type == "safe":
                    Safe()
                elif Type == "unsafe":
                    Unsafe()
                else:
                    main()  # (This Is Added To Make This Part Of The Script Run Stealthy)

        # If Not, Then It Will Just Go To "main" Function (Same Reason ------> ^^^)
        except (requests.ConnectionError, requests.ConnectTimeout):
            main()


"""
This Script Works The Best When This Is Obfuscated So No One Will Try To Modify/Reverse-engineer Your Code.
(Sorry For My Bad English... ( I Am Trying My Best To Explain How This Script Works For You To Use It :) ))

Having Issues For This Template? Create An Issue Over Here "https://github.com/RedFurrFox/Anti-Tampering-Template/issues"
I Will Try My Best To Fix Your Issue As Soon As Possible.

Created By: RedFurrFox On Github
"""
