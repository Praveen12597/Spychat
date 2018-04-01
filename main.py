from spy_details import spy , new_spy
from steganography.steganography import Steganography
from datetime import datetime
#import spy_details

# list of default Status message or the privious status
status_message = ["Busy","Leave a message","Don't Disturb.","Help me"]

# all the information of frnds stored in this list
frnd_list = [ {"name": "sonu", "age": 22, "rating": 6, "is_online": True, "message": []},
              {"name": "monu", "age": 23, "rating": 8, "is_online": True, "message": []}]


def add_status(status):  # function for adding a status.
    if status != None:
        print "\n     Your current status is " + status
    else:
        print "\n       You don't have any status currently.\n"

    existing_status = raw_input("\nYou want to select from old status ?  Y/N: ")

    if existing_status.upper() == "N":
        new_status = raw_input("\nEnter Your status: ")
        if len(new_status)>0:
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


def add_frnd(): # function for adding a friend.
    frnd = { "name": "",
             "age": 0,
             "rating": 0.0,
             "is_online": True,
             "message": []
        }

    # saving the input in the friend list
    frnd["name"] = raw_input("Enter your friend name: ")
    frnd["age"] = input("Enter your friend age: ")
    frnd["rating"] = input("Enter your friend rating: ")

    if len(frnd["name"]) > 2 and frnd["age"] > 14:  # validating name and age
        frnd_list.append(frnd)
        print "You have successfully added a friend."

    else:
        print "The friend cannot be added "

    return len(frnd_list)  # return the total number of frind in the list.


def select_a_frnd():  # this method print the name of friends and take the user input.
    count = 1
    for i in frnd_list:
        print str(count) + ". " + i["name"]
        count = count + 1
    select = input("Enter your choice: ")
    return select - 1  # index of this frnd in the list is one less than the user input, because list starts from 0 index.


def send_message():
    selected_frnd = select_a_frnd()  # selecting the friend.

    # creating the variables for encode function
    original_image = raw_input("What is tha name of your original image: ")
    text = raw_input("What is your secret text? ")
    output_path = "output.jpg"

    # this function encode the meessage or hide the message in a image.
    Steganography.encode(original_image,output_path,text)
    print "Your secret message is ready!"

    # saving the message send by Spy.
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    frnd_list[selected_frnd]["message"].append(new_chat)


def read_message():
    selected_frnd = select_a_frnd()
    output_path = raw_input("Which image you want to decode? ")
    text = Steganography.decode(output_path)
    print "Secret text is ::: " + text
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    frnd_list[selected_frnd]["message"].append(new_chat)
    print "Your secret message has been saved!\n"

#        I WANT TO PRINT ALL THE MESSAGES HE RECEIVED .
#    read = raw_input("You want to read all messages? Y/N ")
#    if read.upper() == "Y":
#        count = 1
#        for i in frnd_list[selected_frnd]["message"]:
#            print str(count) + ". " + i
#            count = count + 1


def menu():
    current_status = None  # current status of the spy

    show_menu = True

    # While Loop -> Display options until Spy will quit.
    while show_menu:
        # Different options for the Spy
        print "\n                  1) Add a status update \n" \
              "                  2) Add a friend \n" \
              "                  3) Send a secret message \n" \
              "                  4) Read a secret message \n" \
              "                  5) Read chats from a user \n" \
              "                  6) Close application \n"
        choice = input("Choose your option : ")
        if choice == 1:

            current_status = add_status(current_status)
            print "\nYour updated status is: " + current_status + "\n"

        elif choice == 2:

           no_of_frnds = add_frnd()
           print "\nYour have " + str(no_of_frnds) + " friends.\n"

        elif choice == 3:
            send_message()

        elif choice == 4:
            read_message()

        elif choice == 5:
            print ("Not Done Till now.")

        elif choice == 6:
            print "\n       Thanks For Using Spy Chat.\n"
            show_menu = False

        else:
            print "\nSorry, This is Invalid Input."


def login():  # A function for login.
    print "\n===============> Login <===============\n"
    # don't use salutation in name
    spy_name2 = raw_input("Enter your name : ")

    # verifying Spy name
    if spy_name2 == spy["name"]:
        print "Welcome Back, Mr. %s , Age: %d , Rating: %.1f .\n" % (spy["name"], spy["age"], spy["rating"])
        print "     Here is your options.\n"
        menu()

    elif spy_name2 == new_spy["name"]:
        print "Welcome Back, %s %s , Age: %d , Rating: %.1f .\n" % (new_spy["salutation"],new_spy["name"] , new_spy["age"] , new_spy["rating"])
        print "     Here is your options.\n"
        menu()

    # this is not working -------> WHY  ?
    else:
        print "Invalid User."


print "Welcome to SpyChat\n"

# Asking Question from Spy that he is new user or existing user.
question = raw_input("Are you a New User ? Y/N : ")

if question.upper() == "Y":
    # Asking for name of Spy
    spy_name = raw_input("\nEnter your Spy Name : ")

    # validation For the name . SPACES and NUMBERS are not allowed.
    if spy_name.isspace():
        print "Ooops! Enter a valid name."

    elif spy_name.isdigit():
        print "Ooops! Enter a valid name."

    elif len(spy_name) > 2:
        print "Welcome " + spy_name + ", glad to have you back with us.\n"

        # Asking for the SALUTATION from the spy
        salutation = raw_input("What should we call you (Mr. or Ms.) : ")

        # Verifying that the Salutation is CORRECT or not.
        if salutation == "Mr." or salutation == "Ms." or salutation == "mr." or salutation == "ms.":

            # Concatenation Name with Spy
            # spy_name = salutation + " " + spy_name
            # print "Alright " + spy_name + ". I'd like to know a little bit more about you..."

            print "Alright %s %s. I'd like to know a little bit more about you...\n" % (salutation,spy_name)

            # Asking the age of spy and verifying the AGE
            age = input("What's your age : ")
            if 14 < age <= 60 :

                # Asking fro the rating of Spy
                print "\nRating Should be Between 0 to 10 ."
                rating = input("What are your Ratings : ")

                # Verifying Rating .
                if rating > 10 or rating < 0:
                    print "Oops! Invalid Rating."

                else:
                    # Display an appropriate message based on spy rating
                    if 10 >= rating > 7:
                        print "\nGreat Spy.\n"
                    elif 7 > rating > 5:
                        print "\nGood Spy.\n"
                    elif 5 < rating < 3:
                        print "\nAverage spy\n"
                    else:
                        print "\nWho Hired You\n"

                    spy_is_online = True
                    # print "Authentication complete. \nWelcome " +spy_name+ ", Age: " +str(age)+ ", Rating: " +str(rating)
                    print "Authentication complete. \nWelcome %s %s , Age: %d , Rating: %.1f .\n" % (salutation,spy_name,age,rating) # String formatting using placeholders

                    new_spy["name"] = spy_name
                    new_spy["salutation"] = salutation
                    new_spy["age"] = age
                    new_spy["rating"] = rating
                    #spy_details.id1(spy_name,salutation, age, rating)
                    #name1 = spy_details.id1(spy_name,salutation,age,rating)
                    login()

            else:
                print "You are not eligible to be a spy."

        else:
            # printing message for invalid Salutation.
            print "Invalid Salutation."

    # condition for invalid name of Spy...
    else:
        print "Ooops! Enter a valid name."

elif question.upper() == "N":
    # praveen is the default user.
    print "Welcome Back Mr. %s\n" % (spy["name"])
    login()

else:
    print "invalid input."
