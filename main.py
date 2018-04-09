from spy_details import spy1, spy, chatmessage, id
from steganography.steganography import Steganography
from datetime import datetime
import csv
from colorama import Fore

# list of default Status message or the previous status
status_message = ["Busy.", "Leave a message.", "Don't Disturb.", "Help me !!! "]

# all the information of frnds stored in this list
frnd1 = spy("sonu","Mr.",19,8.5)
frnd2 = spy("monu", "Mr." , 19 , 9 )
frnd_list = [frnd1,frnd2]

# all id password of spy is in this list.
ID = []
# All chats are saved here.
chats = []
# list of special messages
Special_message = ["SOS", "HELP", "SAVE", "NEED" "HELP ME", "SAVE ME", "NEED HELP", "NEED BACKUP"]

def load_frnds():  # this load the friend list from .csv file
    with open("friends.csv", "rb") as friends_data:
        reader = list(csv.reader(friends_data))
        for row in reader[1:]:
            #print row
            frnd = spy(name=row[0],salutation=row[1],rating=row[3],age=row[2])
            frnd_list.append(frnd)


load_frnds()


def load_chat():  # this load the char list from .csv file
    with open("chat.csv", "rb") as friends_chat:
        reader = list(csv.reader(friends_chat))
        for row in reader[1:]:
            message = chatmessage(message=row[1], sent_by_me=row[3], sender=row[5], recever=row[4])
            chats.append(message)


load_chat()


def login():  # A function for login.
    with open("login.csv", "rb") as login_data:
        reader = csv.reader(login_data)
        for row in reader:
            user = id(id=row[0], password=row[1])
            ID.append(user)

    print "\n===============> Login <===============\n"
    # don't use salutation in name
    id1 = raw_input("Enter your Name or ID : ")
    # verifying Spy name
    id_found = 0
    for i in ID:
        if id1 == i.id:
            id_found = 1
            pass1 = raw_input("Enter Your Password : ")
            if pass1 == i.password:
                menu(id1)
                break
            else:
                print Fore.RED + "\nIncorrect Password."
    if id_found == 0:
        print Fore.RED + "\nIncorrect ID or Name. "


def signup():
    spy2 = spy("", "", 0, 0.0)

    # Asking for name of Spy
    spy2.name = raw_input("\nEnter your Spy Name : ")

    # validation For the name . SPACES and NUMBERS are not allowed.
    if spy2.name.isspace():
        print Fore.RED + "Ooops! Enter a valid name."

    elif spy2.name.isdigit():
        print Fore.RED + "Ooops! Enter a valid name."

    elif len(spy2.name) > 2:
        print "Welcome " + spy2.name + ", glad to have you back with us.\n"

        # Asking for the SALUTATION from the spy
        spy2.salutation = raw_input("What should we call you (Mr. or Ms.) : ")

        # Verifying that the Salutation is CORRECT or not.
        if spy2.salutation == "Mr." or spy2.salutation == "Ms." or spy2.salutation == "mr." or spy2.salutation == "ms.":

            password = raw_input("Choose a Password for Login : ")

            if len(password) == 0:
                print "You didn't created your password."

            print "Alright %s %s. I'd like to know a little bit more about you...\n" % (spy2.salutation,spy2.name)

            # Asking the age of spy and verifying the AGE
            spy2.age = input("What's your age : ")
            if 14 < spy2.age <= 60:

                # Asking fro the rating of Spy
                print "\nRating Should be Between 0 to 10 ."
                spy2.rating = input("What are your Ratings : ")

                # Verifying Rating .
                if spy2.rating > 10 or spy2.rating < 0:
                    print "Oops! Invalid Rating."

                else:
                    # Display an appropriate message based on spy rating
                    if 10 >= spy2.rating > 7:
                        print "\nGreat Spy.\n"
                    elif 7 > spy2.rating > 5:
                        print "\nGood Spy.\n"
                    elif 5 < spy2.rating < 3:
                        print "\nAverage spy\n"
                    else:
                        print "\nWho Hired You\n"

                    spy_is_online = True

                    print "Authentication complete. \nWelcome %s %s , Age: %d , Rating: %.1f .\n" % (spy2.salutation, spy2.name, spy2.age, spy2.rating)

                    with open("signup.csv", "a") as friends_data:
                        writer = csv.writer(friends_data)
                        writer.writerow([spy2.name, spy2.salutation, spy2.rating, spy2.age, spy2.is_online])
                        #frnd_list.append(spy2)

                    with open("login.csv", "a") as login_data:
                        writer = csv.writer(login_data)
                        writer.writerow([spy2.name, password])
                        #frnd_list.append(spy2)

                    menu(spy2.name)

            else:
                print Fore.RED + "You are not eligible to be a spy."

        else:
            # printing message for invalid Salutation.
            print Fore.RED + "Invalid Salutation."

    # condition for invalid name of Spy...
    else:
        print Fore.RED + "Ooops! Enter a valid name."


def add_status(status):  # function for adding a status.
    if status != None:
        print "\n     Your current status is " + status
    else:
        print "\n       You don't have any status currently.\n"

    existing_status = raw_input("\nYou want to select from old status ?  Y/N: ")

    if existing_status.upper() == "N":
        new_status = raw_input("\nEnter Your status: ")
        if len(new_status) > 0:
            status_message.append(new_status)  # adding the new status  to the list of status message .
            print "\nYour Status was Updates Successfully."
            return new_status
        else:
            print "Enter a valid Status."

    elif existing_status.upper()=="Y":
        count = 1  # using this variable for numbering of lines.

        for i in status_message:   # for loop for printing the list of previous status.
            print str(count) + ". " + i
            count = count + 1

        user_choice = input("\nEnter your choice: ")
        print "\nYour Status was Updates Successfully."
        new_status = status_message[user_choice - 1]
        return new_status


def add_frnd(id):  # function for adding a friend.

    frnd = spy("", "", 0, 0.0)

    # saving the input in the friend list
    frnd.name = raw_input("Enter your friends name: ")
    frnd.sal = raw_input("Salutation : ")
    frnd.age = input("Enter your friend age: ")
    frnd.rating = input("Enter your friend rating: ")
    frnd.is_online = True

    if len(frnd.name) > 2 and frnd.age > 14:  # validating name and age
        #frnd_list.append(frnd)
        with open("friends.csv", "a") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name, frnd.sal, frnd.rating, frnd.age, frnd.is_online,id])
            frnd_list.append(frnd)

        print "You have successfully added a friend."

    else:
        print "The friend cannot be added "

    return len(frnd_list)  # return the total number of frind in the list.


def select_a_frnd():  # this method print the name of friends and take the user input.

    count = 1
    for i in frnd_list:
        print str(count) + ". " + i.name
        count = count + 1
    select = input("Enter your choice: ")
    return select - 1  # index of this frnd in the list is one less than the user input, because list starts from 0 index.


def send_message(id):
    selected_frnd = select_a_frnd()  # selecting the friend.
    # print frnd_list[selected_frnd].name  # name of selected friend

    # creating the variables for encode function
    original_image = raw_input("What is tha name of your original image: ")
    text = raw_input("What is your secret text? ")
    output_path = "output.jpg"

    # creating a list for saving the sliced message
    msg = []
    # splitting the msg word by word and a saving it to msg
    msg = text.split()

    # matching the word from some special words
    emergency = 0
    for i in Special_message:
        for j in msg:
            if i == j.upper():
                emergency = 1
                break
            if emergency == 1:
                break
        if emergency == 1:
            break

    if emergency == 1:
        print Fore.RED + "\n You are sending a Special/Emergency message. \n"
        print Fore.BLACK
        print "Please wait ,  Your message is Encoding ... "
    # this function encode the message or hide the message in a image.
    Steganography.encode(original_image,output_path,text)
    print "Your secret message is ready!"
    # saving the message send by Spy.
    new_chat = chatmessage(text,True,id,frnd_list[selected_frnd].name)
    frnd_list[selected_frnd].chat.append(new_chat)

    with open("chat.csv", "a") as chat_data:
        writer = csv.writer(chat_data)
        writer.writerow([frnd_list[selected_frnd].name, text, datetime.now(), True,frnd_list[selected_frnd].name,id])

    # loading the chat again to the list.


def read_message(id):

    msg = 0
    senderr = []
    for i in chats:
        c = 0
        if i.recever == id:
            senderr.append(i.sender)
            # print "You have message from " + i.sender
            msg = 1
        else:
            c = c + 1

    print "\nYou have message From " + senderr[-1] + ".\n"

    if msg == 0:
        print "You don't Have any message."

    if msg == 1:
        selected_frnd = select_a_frnd()

        for i in chats:
            c = 0
            if i.recever == frnd_list[selected_frnd].name:
                sender = i.sender
            else:
                c = c + 1

        output_path = raw_input("Which image you want to decode? ")
        text = Steganography.decode(output_path)
        print "\n Secret text is ::: " + text

        time = chats[c].time

        print Fore.BLUE + "         " + str(time) + Fore.RED + " " + " Sender : "+ sender

        print Fore.BLACK + "Your secret message has been saved!\n"

        # appending the message to new_chat
        new_chat = chatmessage(text, False, frnd_list[selected_frnd].name, id)

        frnd_list[selected_frnd].chat.append(new_chat)

        # no need to write again in the csv file.

        #with open("chat.csv", "a") as chat_data:
            #writer = csv.writer(chat_data)
            #writer.writerow([frnd_list[selected_frnd].name, text, datetime.now(), False, id, frnd_list[selected_frnd].name])


def Read_All_messages(id):
    msg = 0
    sender = []
    for i in chats:
        if i.recever == id:
            sender = i.sender
            msg = 1
            print "\n" + Fore.BLACK + i.message

            # Searching for the accurate time , when the msg was send ,, from chat.csv file
            with open("chat.csv", "rb") as friends_chat:
                reader = list(csv.reader(friends_chat))
                for row in reader[1:]:
                    if row[5] == i.sender:
                        time = row[2]

            print Fore.BLUE + str(time) + Fore.GREEN + "   Sender -> " + Fore.RED + i.sender
            print Fore.BLACK

    if msg == 0:
        print "You don't Have any message."


def ChatHistory(id):

    msg = 0
    senderr = []
    for i in chats:
        if i.recever == id:
            senderr.append(i.sender)
            msg = 1

    if msg == 0:
        print "You don't Have any message."

    print "\n You have " + str(len(senderr)) + " messages from Your friends.\n"

    c = 1
    for i in senderr:
        print str(c) + ". " + i
        c = c + 1

    print "\n"

    select = raw_input("Type the name of your  Friend : ")

    for i in chats:
        if i.recever == id:
            if i.sender == select:
                print "\n" + Fore.BLACK + i.message

                with open("chat.csv", "rb") as friends_chat:
                    reader = list(csv.reader(friends_chat))
                    for row in reader[1:]:
                        if row[5] == select:
                            time = row[2]

                print Fore.BLUE + str(time) + Fore.GREEN + "   Sender -> " + Fore.RED + select
                print Fore.BLACK


def menu(id):
    current_status = None  # current status of the spy

    show_menu = True

    # While Loop -> Display options until Spy will quit.
    while show_menu:
        # Different options for the Spy
        print "\n                          M E N U"
        print Fore.LIGHTBLUE_EX + \
              "\n                  1) Add a status update \n" \
              "                  2) Add a friend \n" \
              "                  3) See friend list \n" \
              "                  4) Send a secret message \n" \
              "                  5) Read a secret message \n" \
              "                  6) Chat History \n " \
              "                 7) Read All Messages \n " \
              "                 8) Close application \n" \
              "                  9) Logout \n"

        print Fore.BLACK
        choice = input("Choose your option : ")
        if choice == 1:

            current_status = add_status(current_status)
            print "\nYour updated status is: " + current_status + "\n"

        elif choice == 2:

           no_of_frnds = add_frnd(id)
           print "\nYour have " + str(no_of_frnds) + " friends.\n"

        elif choice == 3:
            count = 1
            print Fore.LIGHTRED_EX

            for i in frnd_list:
                print str(count) + ". " + i.name
                count = count + 1

            print Fore.BLACK

        elif choice == 4:
            send_message(id)

        elif choice == 5:
            read_message(id)

        elif choice == 6:
            ChatHistory(id)

        elif choice == 7:
            Read_All_messages(id)

        elif choice == 8:
            print "\n       Thanks For Using Spy Chat.\n"
            show_menu = False

        elif choice == 9:
            welcome()

        else:
            print "\nSorry, This is Invalid Input."


########################################################################################################################


def welcome():

    print "\nWelcome to SpyChat\n"

    # Asking Question from Spy that he is new user or existing user.
    question = raw_input("Are you a New User ? Y/N : ")

    if question.upper() == "Y":
        signup()

    elif question.upper() == "N":

        print Fore.CYAN + "\n<----- DESCRIPTION OF DEFAULT USERS ----->"
        # praveen is the default user.
        print "\n             Welcome Back %s" % (spy1.name)
        print "             Your Password is : 123\n"
        print "<---------------------------------------->"
        print Fore.BLACK
        print "There are three TWO more default user , see in login.csv "
        print "You can also create your own ID and Password.\n\n"
        login()

    else:
        print "invalid input."


welcome()
