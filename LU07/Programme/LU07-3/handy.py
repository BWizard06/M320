from phone import Phone

class Handy(Phone):

    def handle_sms(self):
        print("sms senden und empfangen")

    def what_i_am(self):
        return "an old handy"