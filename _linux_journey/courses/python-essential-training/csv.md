---
title: "We take that file object and pass it to a new csv reader object"
category: "python-essential-training"
tags: ["python-essential-training", "csv"]
---

* This is a module in Python.
```
csv
```

* To open the file for reading, we can do:
```
with open('10_02_us.csv', 'r') as f:
		 # We take that file object and pass it to a new csv reader object
		 # The reader object is not a list
		 reader = csv.reader(f)
		 for row in reader:
		 		 print(row)
```
* The output of the above example would print out all of the rows in the CSV file.
	* This would work for a comma delimited value. 
* If you run `type(reader)`, you will see the output as:
```
_csv.reader
```
* For a tab separated value we would do:
```
with open('10_02_us.csv', 'r') as f:
		 reader = csv.reader(f, delimiter='\t')
		 for row in reader:
		 		 print(row)
```
* The output would be that all of the values are split up.
* If you want to skip the header, you do:
```
with open('10_02_us.csv', 'r') as f:
		 reader = csv.reader(f, delimiter='\t')
		 # Add this to skip the header (uses the `next` function)
		 next(reader)
		 for row in reader:
		 		 print(row)
```
* It is possible to call `next(reader)` multiple times to skip over the row.
* The alternative is to convert it to a list:
```
with open('10_02_us.csv', 'r') as f:
		 reader = list(csv.reader(f, delimiter='\t'))
		 for row in reader[1:]:
		 		 print(row)
```
* The above configuration will also skip over the header as well.
* If you want to use the `header` data, using the `dict reader` is a good fit:
```
with open('10_02_us.csv', 'r') as f:
		 reader = list(csv.DictReader(f, delimiter='\t'))
		 for row in reader:
		 		 print(row)
```
* The header is used as the keys in each dictionary in the list.
* To convert it to a list object, we can do:
```
with open('10_02_us.csv', 'r') as f:
		 data = list(csv.DictReader(f, delimiter='\t'))
```
* To find postal codes that are only divisible by 1 and themselves (prime), we have:
```
with open('10_02_us.csv', 'r') as f:
		 data = list(csv.DictReader(f, delimiter='\t'))

# This code block gets all of the prime numbers between 2 and 99999
primes = []
for number in range(2, 99999):
		 for factor in range(2, int(number**0.5)):
		 			if number % factor == 0:
							break
			else:
					 primes.append(number)
# Next we filter these for prime locations. Limiting the search in the below example:
data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
```
* If we run the above and then run `len(data)`, the total output would be `91`.
* To write this back to a CSV file:
```
with open('10_02_us.csv', 'r') as f:
		 data = list(csv.DictReader(f, delimiter='\t'))

# This code block gets all of the prime numbers between 2 and 99999
primes = []
for number in range(2, 99999):
		 for factor in range(2, int(number**0.5)):
		 			if number % factor == 0:
							break
			else:
					 primes.append(number)
# Next we filter these for prime locations. Limiting the search in the below example:
data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']

with open('10_02_ma_prime.csv', 'w') as f:
		 # Can make the delimiter tabs, by passing a keyword to the writer argument below. By default a comma is used
	   writer = csv.writer(f)
	   for row in data:
	   			# Have to pass in the row as a list
	   	    writer.writerow(['place name'], row['county'])
```
