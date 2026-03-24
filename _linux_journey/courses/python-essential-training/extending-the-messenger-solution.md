---
title: "This function returns the current time as a string"
category: "python-essential-training"
tags: ["python-essential-training", "extending", "messenger", "solution"]
---

* Common pattern in programming is sending messages between senders and receivers.
	* The receivers are sometimes called listeners.
```
    from datetime import datetime
    
		 # This function returns the current time as a string    
    def getCurrentTime():
        return datetime.now().strftime(\%m-%d-%Y %H:%M:%S\)
    
    # This contains two methods: a `send` method and a `receive` method.
	  # Each function has a bunch of listeners within them and they are extended from the Messenger class
    class Messenger:
        def __init__(self, listeners=[]):
            self.listeners = listeners
        
        def send(self, message):
						 # Each listener is iterated through
            for listener in self.listeners:
								 # listener.receive is then called for the message. All of the listeners that are listening here will receive the message
                listener.receive(message)
    
        def receive(self, message):
            # Must be implemented by extending classes
            pass
    
    # This saves the messages and adds them to a list. It also saves the time that the messages was received
    class SaveMessages(Messenger):
				 # Constructor is overwritten
        def __init__(self, listeners=[]):
            super().__init__(listeners)
			 			# This is the list where they are saved here:
						 # We can add whatever custom attributes we want
            self.messages = []
            
        def receive(self, message):
						 # Every time a message is received, it adds it to the list of messages
            self.messages.append({'message': message, 'time': getCurrentTime()})
            
        def printMessages(self):
            for m in self.messages:
                print(f'Message: \{m[\message\]}\ Time: {m[\time\]}')
						 # The list of messages is reset here. It will only print out the message once and then clear it afterwards
            self.messages = []
			
listener = SaveMessages()

sender = Messenger([listener])

sender.send('Hello, there! This is the first message!')

sender.send('This is the second message!')

sender.send('This is the third message!')

listener.printMessages()
```
* This will print out the following:
```
Messages: "Hello, there! This is the first message!" Time:10-09-2023 12:40:00 
```
* It will do this for all three messages.
* Tuples and Dictionaries can also be used to hold the messages. Another component is where do we put the list of messages. 