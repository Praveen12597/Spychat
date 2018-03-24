print "Welcome to SpyChat"

# Asking for name of Spy
spy_name = raw_input("Enter your Spy Name : ")

# validation For the name . SPACES and NUMBERS are not allowed.
if spy_name.isspace():
    print "Ooops! Enter a valid name."

elif spy_name.isdigit():
    print "Ooops! Enter a valid name."

elif len(spy_name) > 2:
    print "Welcome " + spy_name + ", glad to have you back with us."

    # Asking for the SALUTATION from the spy
    salutation = raw_input("What should we call you (Mr. or Ms.) : ")

    # Verifying that the Salutation is CORRECT or not.
    if salutation == "Mr." or salutation == "Ms." or salutation == "mr." or salutation == "ms.":

        # Concatenation Name with Spy
        spy_name = salutation + " " + spy_name
        print "Alright " + spy_name + ". I'd like to know a little bit more about you..."

        # Asking the age of spy and verifying the AGE
        age = input("What's your age : ")
        if 14 < age <= 60 :

            # Asking fro the rating of Spy
            print "Rating Should be Between 0 to 10 ."
            rating = input("What are your Ratings : ")

            # Verifying Rating .
            if rating > 10 or rating < 0:
                print "Oops! Invalid Rating."

            else:
                # Display an appropriate message based on spy rating
                if 10 > rating > 7:
                    print "Great Spy."
                elif 7 > rating > 5:
                    print "Good Spy."
                elif 3 < rating < 5:
                    print "Average spy"
                else:
                    print "Who Hired You"

                spy_is_online = True
                print "Authentication complete. Welcome " +spy_name+ ", Age: " +str(age)+ ", Rating: " +str(rating)

        else:
            print "You are not eligible to be a spy."

    else:
        # printing message for invalid Salutation.
        print "Invalid Salutation."

# condition for invalid name of Spy...
else:
    print "Ooops! Enter a valid name."
