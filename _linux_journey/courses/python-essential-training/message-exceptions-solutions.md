---
title: "Message Exceptions Solutions"
category: "python-essential-training"
tags: ["python-essential-training", "message", "exceptions", "solutions"]
---

* Challenge Requirements:
```
   **\\# 1. Finish creating the TooManyMessagesException class**
    Fill in the TooManyMessagesException class. Add a custom message!
```
```
    **\\# 2. Raise a TooManyMessagesException exception here**
    Make sure that the SaveMessages class doesn't get over-full and raises an Exception if the max_messages limit is reached.
```
```
    **\\# 3. Catch a TooManyMessagesException and print the messages**
    Modify this code so that, if an exception is raised when the message is sent, the messages are printed out (emptying the message list) and the message is re-sent. Make sure to print out any remaining messages at the end!
```
* Solution is:
```
from datetime import datetime

def getCurrentTime():
	   return datetime.now().strftime(\%m-%d-%Y %H:%M:%S\)
	   
class Messenger:,
		def __init__(self, listeners=[]):
			self.listeners = listeners
	
		def send(self, message):
			for listener in self.listeners:
				listener.receive(message)

		def receive(self, message):
			# Must be implemented by extending classes
			pass

# We need this class to extend the Python Exception class
class TooManyMessagesException(Exception):
		def __init__(self, message):
			  super().__init__(f'Message "{message}" could not be added. Please clear existing messages')
			
class SaveMessages(Messenger):
		def __init__(self, listeners=[]):
				super().__init__(listeners)
				self.messages = []
				self.max_messages = 10
            
		def receive(self, message):
				if len(self.messages) >= self.max_messages:
					# From the `TooManyMessagesException` function's super statement above, we need to make sure the exception is raised here:
					raise TooManyMessagesException(message)
				self.messages.append({'message': message, 'time': getCurrentTime()})
            
		def printMessages(self):
				for m in self.messages:
					  print(f'Message: "{m["message"]}" Time: {m["time"]}')
				self.messages = []

listener = SaveMessages()
sender = Messenger([listener])

for i in range(0, 1000):
		try:
				sender.send(f'This is message {i}')
		# We catch the "TooManyMessages" Exception.
		except TooManyMessagesException:
				# All messages are printed
				listener.printMessages()
				# We resend them here afterwards
				sender.send(f'This is message {i}')
# We print all of the remaining messages inside the class
listener.printMessages()


```
* Example output:
```
Message: "This is message 999" Time: 10-02-2022 21:09:44
```