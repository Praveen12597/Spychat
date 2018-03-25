from sqlalchemy.dialects.sqlite.pysqlite import _SQLite_pysqliteDate
import spy_details


def start_chat():
    show_menu = True

    # While Loop -> Display options until Spy will quit.
    while show_menu:
        # Different options for the Spy
        print "                  1. Add a Status\n" \
              "                  2. Add a Friend \n" \
              "                  0. Exit\n"
        choice = input("Choose your option :")
        if choice == 1:
            print "\n       Will Add a Status.\n"

        elif choice == 2:
            print "\n       Will Add a Friends.\n"

        elif choice == 0:
            print "\n       Thanks For Using Spy Chat.\n"
            show_menu = False

        else:
            print "\nSorry, This is Invalid Input."


def login():  # A function for login.
    print "\n===============> Login <===============\n"
    # don't use salutation in name
    spy_name2 = raw_input("Enter your name : ")

    # verifying Spy name
    if spy_name2 == spy_details.name:
        print "Welcome Back Mr. %s , Age: %d , Rating: %.1f .\n" % (spy_details.name, spy_details.age, spy_details.rating)
        print "                 Here is your options.\n"
        start_chat()

    elif spy_name2 == name1:
        print "Welcome back %s\n" % (name1)
        print "                 Here is your options.\n"
        start_chat()

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
                    print "Authentication complete. \nWelcome %s , Age: %d , Rating: %.1f .\n" % (spy_name,age,rating) # String formatting using placeholders

                    spy_details.id1(spy_name,salutation, age, rating)
                    name1 = spy_details.id1(spy_name,salutation,age,rating)
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
    print "Welcome Back Mr. %s\n" % (spy_details.name)
    login()

else:
    print "invalid input."
