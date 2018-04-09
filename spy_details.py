from datetime import datetime


class spy:

    # cresting constructor for this class
    def __init__(self, name, salutation, age, rating):
        # self.name = salutation + " " + name
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chat = []
        self.current_status_message = None


# creating object
spy1 = spy("praveen", "Mr." , 19 , 9 )

# chat class
class chatmessage:

    def __init__(self, message, sent_by_me, sender, recever):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
        self.sender = sender
        self.recever = recever


class id:

    def __init__(self,id,password):
        self.id = id
        self.password = password