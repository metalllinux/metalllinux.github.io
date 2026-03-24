---
title: "Need to call this method below:"
category: "python-essential-training"
tags: ["python-essential-training", "json"]
---

* Loading JSON.
* Here is an example JSON string:
```
jsonString = '{"a":"apple", "b": "bear", "c": "cat"}'
```
* To convert the above into a dictionary, we need to import the `json` module.
```
import json
jsonString = '{"a":"apple", "b": "bear", "c": "cat"}'
# Need to call this method below:
# loads plural is required here:
json.loads
```
* Don't add a trailinig comma like so:
```
jsonString = '{"a":"apple", "b": "bear", "c": "cat"}'
```
* We can check for exceptions with the `try` statement:
```
import json
from json import JSONDecodeError
jsonString = '{"a":"apple", "b": "bear", "c": "cat"}'
try:
		json.loads(jsonString)
# The decoder comes from the module and needs to be specifically imported.
except JSONDecodeError:
    print('Could not parse JSON!')
```
* Dumping JSON Files
```
pythonDict = {'a':'apple', 'b': 'bear', 'c': 'cat'}
json.dumps(pythonDict)
```
* This then outputs:
```
{"a":"apple", "b": "bear", "c": "cat"}
```
* No need to add exception handling for the above, due to it being a Python Dictionary and formatted as a JSON string.
* Custom JSON Decoders
```
class Animal:
		 def __init__(self, name):
		 		 self.name = name
				 
pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'),}
json.dumps(pythonDict)
```
* Running the above produces `Object of type Animal is not JSON serializable`
	* The JSON module does not know how to handle this.
		* We can overwrite this with a JSON encoder of our own.
```
class Animal:
		 def __init__(self, name):
		 		 self.name = name

class AnimalEncoder(JSONEncoder):
		 # `o` is the object being passed into here, that needs to be decoded into JSON
	   def default(self, o):
	   			if type(o) == Animal:
						 return o.name
					# If it is not an animal, we pass it to the parent version of the decoder
					return super().default(o)

pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'),}
json.dumps(pythonDict, cls=AnimalEncoder)
```