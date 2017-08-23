# This is a developer oriented guide for teaching you
# how to use Echonify to develop productivity tools.

# More development resources https://github.com/Echonify

import sys
sys.path.append("../lib")

from Echonify import writePlain, writeFileRef, readPlain

def familiar_with_software_interface():
    writePlain(
        "We assume that you have opened Echonify.\r\n"
        "You see the interface similar to the general chat software. "
        "The only difference is that your communication object is a script file "
        "rather than a real person."
        )
    writeFileRef("images/main_interface.png")
    writePlain(
        "The blue rectangle part on the left show the already loaded script. "
        "Each script provides different functions, and you can interact with it "
        "through the chat window on the right.\r\n"
        "If you already have a script, you can click button on the green rectangle to load it."
        )
    writeFileRef("images/create_conversation_window.png")
    writePlain("This is the window used to load a new script.")
    writePlain("Finally, click the dolphin icon in the upper right corner of the screen and open the Preferences window.")
    writeFileRef("images/state_item.png")
    writeFileRef("images/perferences_window.png")
    writePlain("This is preferences window and you can fill in your basic profile here.")
    
def download_and_run_script():
    writePlain(
        "For ease of use, we have prepared some scripts for evaluation. "
        "You can visit https://github.com/Echonify/Scripts to download."
        )
    writePlain(
        "I downloaded a script for calculating the file MD5 value. "
        "Now I need to load it into Echonify."
        )
    writeFileRef("images/load_first_script.png")
    writePlain(
        "The software automatically generates display name and icon for me. "
        "Of course you can also customize it."
        )
    writePlain("The script has been loaded successfully, let's try it.")
    writeFileRef("images/first_message.png")

def write_your_own_script():
    writePlain("Writing an Echonify script may be simpler than you might think.")
    writePlain(
        "Whatever the scripting language you use, you only need to know is the standard "
        "input and output stream. The script receives the user input "
        "through the standard input stream and sends the message to the user "
        "through the standard output stream."
    )
    writePlain(
        "The only thing that is worth noting is to flush buffer immediately after "
        "writing to the standard output stream."
        )
    writePlain("Such as this:")
    writePlain(
        "*print \"Hello Echonify!\"*\r\n"
        "*sys.stdout.flush()*\r\n"
        , "markdown")

def security_directory():
    writePlain(
        "In order to prevent malicious scripts from harming the system, all files accessed in "
        "the script must be included in the Security Path."
    )
    writeFileRef("images/security_path.png")

if __name__ == '__main__':
    writePlain(
        "Welcome! We are excited you want to learn how to use Echonify.\r\n"
        "In this four-part tutorial, you will:\r\n\r\n"
        "1. Familiar with software interface.\r\n"
        "2. Download and run script.\r\n"
        "3. Write your own script tools.\r\n"
        "4. Security Directory.\r\n"
        )
    writePlain(
               "The software itself is very simple so that beginners can quickly get started. "
               "the value of Echonify is in how it can ship and run scripts; "
               "it's totally agnostic as to what your script actually does."
               )
    writePlain("Now pick a topic you are interested in (Type topic number):")
    while True:
        index = readPlain()
        index = index.strip()
        if(index == '1'):
            familiar_with_software_interface()
        elif(index == '2'):
            download_and_run_script()
        elif(index == '3'):
            write_your_own_script()
        elif(index == '4'):
            security_directory()

        writePlain(
            "Now pick a topic you are interested in (Type topic number):\r\n\r\n"
            "1. Familiar with software interface.\r\n"
            "2. Download and run script.\r\n"
            "3. Write your own script tools.\r\n"
            "4. Security Directory.\r\n"
            )
