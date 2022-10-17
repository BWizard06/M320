class MiniChat:
    '''
    Eine kleine Demo für das Kommunizieren von Klassen.
    '''

    def __init__(self, name):
        '''
        Ich muss mich im Chat mit Namen bekannt machen
        '''
        self.__name = name

    @property
    def name(self):
        return self.__name

    def send_a_message_to(self, receiver, message):
        '''
        Sendet eine Mitteilung (message) an einen durch Empfänger (receiver)
        :param message: Inhalt der Mitteilung
        :param receiver: Empfänger der Mitteilung
        '''
        receiver.get_a_message("Message from " + self.__name)
        receiver.get_a_message("Content: " + message)


    def get_a_message(self, message):
        '''
        Empfängt eine Meldung und gibt diese am Stdout aus.
        :param message: eine Nachricht
        '''
        print("receiver is " + self.name + "\n" + message)

if __name__ == "__main__":
    # die beteilgten Objekte
    
    ben = MiniChat("Ben")
    shahin = MiniChat("Shahin")

    ben.send_a_message_to(shahin, "hallo " + shahin.name + " wie geht es dir heute?")
    shahin.send_a_message_to(ben, "Moin " + ben.name + ", mir geht es gut, ich werde heute noch rausgehen und wie geht es dir so'")
    ben.send_a_message_to(shahin, "Jo mir geht es auch gut")


