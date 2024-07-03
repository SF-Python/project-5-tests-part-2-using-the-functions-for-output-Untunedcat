name="Seth Shorten"
GitHub_Name="untunedcat"
course_ID="COP2002.0M1"
todays_Date="06/28/24"
major="Network Security"
title="Peoject 5 part 2"
description="Helps with learning some important port numbers"

# Makes what you want random
from random import randrange

# The list of names
portNameArray = ["FTP","FTP","SSH","Telnet","SMTP","DNS","DHCP","DHCP","HTTPS","POP3",
"NetBIOS","NetBIOS","IMAP","SNMP","SNMP","LDAP","HTTPS","SMB","RDP"]

# The list of numbers as a string
portNumArray = ["20","21","22","23","25","53","67","68","80","110","137",
"139","143","161","162","389","443","445","3389"]


# Used for finding the right number to name
def numToName(portNumList: list[str], portNameList:  list[str], portNumber:  str) -> str:
    index = 0

    # For finding the right port numbers to name.
    for port in portNumList:
        if port == portNumber:
            return portNameList[index]

    # The ELSE for finding the answer if it's right
        else:
            index += 1

    # If the number was not found in the prompt.
    return "If you see this, then you got a number that isn't in this test."

# Used to find the right name to number
def nameToNum(portNumList: list[str], portNameList:  list[str],  portName:  str) -> list[str]:
    # For storing the answer
    result = []
    for index in range(len(portNumList)):
         # Now for the name to number
         if portName == portNameList[index]:
              result.append(portNumList[index])

    # For the right answer
    return result

# Getting the players input
# Make sure you get the correct input for 1,2,3 and, m
def getInput():
    # Make me say it one more time what this does
    userInput = ""
    while userInput not in ["1","2","3","m"]:
             userInput = input("Choice:  ").rstrip()


    # The return of the input
    return userInput

# Prints the menu
def menu():
    # The menu for the user
    prompt = "Main Menu:"
    prompt += "\n1.  Given a port number, identify the PROTOCOL (use abrreviation)."
    prompt += "\n2.  Given a port ptoyocol, identify a port NUMBER."
    prompt += "\n3.  Exit"
    print(prompt)
    userInput = getInput()
    # Make it to where the user doesn't mess it up with spaces
    return userInput.strip()

# Gives the number to guess the name
def qWhatName():
    msg = "Option 1:  Identify the port's NAME."
    msg += "\n------------------------------\n"
    print(msg)
    selection = ""

    while selection != "m":
        qIndex = randrange(0, len(portNumArray))

        qNum = portNumArray[qIndex]

        answer = numToName(portNumArray, portNameArray, qNum)

        prompt = f"What is the number for the protocol {qNum} (m=Main Menu)"
    
        selection = input(prompt)

        while selection in ["","\n"]:
            selection = input(prompt)

        if selection in answer:
          print("Correct answer!\n")
        else:
          msg = f"Incorrect.  The correct answer is {portNameArray[qIndex]}.\n"
          print(msg)

# Gives a name to guess the number
def qWhatNumber():
    msg = "Option 2:  Identify the port's NUMBER."
    msg += "\n------------------------------\n"
    print(msg)
    selection = ""

    while selection != "m":
        qIndex = randrange(0, len(portNameArray))

        qName = portNameArray[qIndex]

        answer = nameToNum(portNumArray, portNameArray, qName)

        prompt = f"What is the number for the protocol {qName} (m=Main Menu)"
    
        selection = input(prompt)

        while selection in ["","\n"]:
            selection = input(prompt)

        if selection in answer:
          print("Correct answer!\n")
        else:
          msg = f"Incorrect.  The correct answer is {portNumArray[qIndex]}.\n"
          print(msg)

# What the user will see.
def main():
    selection = ""
    # A while statement because they're very useful
    # Makes it end if the player enters 3
    while selection != "3":
        selection = menu()
        # If choice 1
        if selection == "1":
            qWhatName()
        # If choice 2
        elif selection == "2":
            qWhatNumber()
    
    
    #### Keeping this becasue I like what it does
    ## Makes the print show the name instead of the index number in the array
    #random_index = randrange(len(portNameArray))
    ## It prints
    #print(portNameArray[random_index])


if __name__ == "__main__":
    main()