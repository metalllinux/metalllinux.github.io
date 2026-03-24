---
title: "Dictionaries"
category: "python-essential-training"
tags: ["python-essential-training", "dictionaries"]
---

* Dictionaries and Lists.
	* Dictionaries need WD40 to move.
	* Lists need ducktape to grounded down.
* 95% of the data structures.
* Dictionary example:
```
animals = {
    'a': 'aardvark',
	  'b': 'bear',
	  'c': 'cat',
}
animals
```
* The above will output:
```
{'a': 'aardvark', 'b': 'bear', 'c': 'cat'}
```
* If we do `animals['a']`, `'aardvark'` is returned.
* Can add items to the dictionary with:
```
animals['d'] = 'dog'
animals
```
* Will output:
```
{'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}
```
* To change an item in the Dictionary, we can do:
```
animals['a'] = 'antelope'
animals
```
* Will output:
```
{'a': 'antelope', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

```
* If we want to get the keys and values of the dictionary, we do:
```
animals.key()
```
* The output for that would be `dict_keys(['a', 'b', 'c', 'd'])`
	* Its a dict_keys object.
	* They are immutable and you cannot add to them - need to change the underlying dictionary.
* To get the values we run:
```
animals.values()
```
* This prints out:
```
dict_values(['antelope', 'bear', 'cat', 'dog'])
```
* It is possible to convert these to lists.
	* `list(animals.keys())`
		* That will then output:
```
['a', 'b', 'c', 'd']
```
* What if you try to access a key that is not present.
	* For example `animals['e']` will then output an error message.
		* For that we would use the `get` function, `animals.get('e', 'elephant')` , the default value being `elephant` here and it will print `elephant` instead of an error.
	* If you do `animals.get('a')`, the output will be:
```
'antelope'
```
* Since that is part of the dictionary.
	* Like strings and lists, you can also use the `len` function on a dictionary, for example `len(animals)`
		* This outputs `4`, since there are 4 keys in the dictionary.
* A common pattern in programming, is where the dictionary values are lists:
```
animals = {
     'a': ['aardvark', 'antelope'],
	   'b': ['bear'],
}
```
* To add `bison` to the above structure of animals:
```
animals['b'].append('bison')
```
* `bison` starts with a `b`.
* If we need to add `cat` however, the list for `c` does not exist.
```
animals['c'] = ['cat']
```
* What if we don't know if the above key exists or not.
	* Write something like this:
```
if 'c' not in animals:
    animals['c'] = []
	
animals['c'].append('cat')
```
* The above code is rather convoluted. The solution is `Default Dict`.
* That has to be imported from the `collections` package with: 
```
from collections import defaultdict
```
* The Default Dict
	* Need to pass the type of object that it should return by default.
```
animals = defaultdict(list)
```
* A common mistake in the above example, is that some people will pass in an instance of the thing they want returned.
* Running `animals` will not return anything yet:
```
defaultdict(list, {})
```
```
animals['e'].append('elephant')
animals
```
* That will output the below:
`defaultdict(list, {'e':['elephant']})`
* If you do the same thing again, for instance:
```
animals['e'].append('emu')
animals
```
* That also gets added to the list like so:
`defaultdict(list, {'e':['elephant', 'emu']})`
* Running `animals['f']` will return an empty list, as we haven't added anything there yet.
