---
title: "Pre-requisites - JSON PATH"
category: "cka-certification"
tags: ["cka-certification", "pre", "requisites", "json", "path"]
---

# Pre-requisites - JSON PATH

JSON PATH Quiz:

* Which of the following is used to separate the key and value in YAML?

    * Colon
    
* How many array keys are there in the following yaml snippet?
```
Fruit:
  - Orange
  - Apple
  - Banana
Vegetables:
  - Carrot
  - CauliFlower
  - Tomato
```

    * The answer is `2` --> `Fruit` and `Vegetables`
    
* Which of the following is true:

```
Which of the following statements is true?

A. Dictionary is an unordered collection whereas list is an ordered collection.


B. Dictionary is an ordered collection whereas list is an unordered collection.


C. Dictionary and list, both are an ordered collection.


D. Dictionary and list, both are an unordered collection.
```

    * The Answer is `A`.
    
* There is a yaml file named practice.yaml under /home/bob/playbooks/ directory with a key property1 and value value1. Add an additional key named property2 and value value2.

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

property1: value1
property2: value2
```

* We have updated the /home/bob/playbooks/practice.yaml file with the key name and value apple. Add some additional properties (given below) to the dictionary.


    * name= apple
    * colour= red
    * weight= 90g

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

name: apple
color: red
weight: 90g
```

* We have updated the /home/bob/playbooks/practice.yaml file with a dictionary named employee. Add the remaining properties to it using information from the table below.

Key/Property 	Value
name 	john
gender 	male
age 	24

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

employee:
  name: john
  gender: male
  age: 24
```

* Now, update the /home/bob/playbooks/practice.yaml file with a dictionary in dictionary.

Add a dictionary named address to add the address information in this file.

Key/Property 	Value
city 	edison
state 	new jersey
country 	united states

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

employee:
  name: john
  gender: male
  age: 24
  address:
    city: edison
    state: new jersey
    country: united states
```

* We have updated the /home/bob/playbooks/practice.yaml file with an array of apples. Add a new apple to the list to make it a total of 4.

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

- apple
- apple
- apple
- apple
```

* In /home/bob/playbooks/practice.yaml, add two more values apple to make it 6.

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml




Update the file as below.

- apple
- apple
- apple
- apple
- apple
- apple
```

* We have updated the /home/bob/playbooks/practice.yaml file with some data for apple, orange and mango. Just like apple, we would like to add additional details for each item, such as colour, weight etc. Modify the remaining items to match the below data.

orange
colour 	weight
orange 	90g

mango
colour 	weight
yellow 	150g

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

- name: apple
  color: red
  weight: 100g
- name: orange
  color: orange
  weight: 90g
- name: mango
  color: yellow
  weight: 150g
```

* We have updated the /home/bob/playbooks/practice.yaml file with a dictionary named employee. We would like to record information about multiple employees. Convert the dictionary named employee to an array named employees.

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

employees:
  - name: john
    gender: male
    age: 24
```

* Update the /home/bob/playbooks/practice.yaml file to add an additional employee (below the existing entry) to the list using the below information.

Key/Property 	Value
name 	sarah
gender 	female
age 	28

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

employees:
  - name: john
    gender: male
    age: 24
  - name: sarah
    gender: female
    age: 28
```

* We have updated the /home/bob/playbooks/practice.yaml file to add some more details. Now add the employee payslip information by adding an array called payslips. Remember, while address is a dictionary, payslips is an array of month and amount.

payslips
month 	amount
june 	1400
july 	2400
august 	3400

```
Edit the given yaml.

vi /home/bob/playbooks/practice.yaml

Update the file as below.

employee:
  name: john
  gender: male
  age: 24
  address:
    city: edison
    state: new jersey
    country: united states
  payslips:
    - month: june
      amount: 1400
    - month: july
      amount: 2400
    - month: august
      amount: 3400
```

* JSON Path Introduction

* Develop a JSON PATH query to extract the kind of object. A file named q1.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "value1"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q1.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer1.sh in the /root directory.

```
cat q1.json | jpath $.property1
[
  "value1"
]

So you need to write the cat q1.json | jpath $.property1 into file answer1.sh.
```

* jpath $.property1: Uses JSONPath syntax to extract the value of property1.

* Develop a JSON PATH query to extract the kind of object. A file named q2.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  {
    "colour": "white",
    "price": "$120,000"
  }
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q2.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer2.sh in the /root directory.

```
echo cat q2.json | jpath $.bus
  {
    "color": "white",
    "price": "$120,000"
  }
]

So you need to write the cat q2.json | jpath $.bus into file answer2.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q3.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "$120,000"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q3.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer3.sh in the /root directory.

```
cat q3.json | jpath $.bus.price
[
  "$120,000"
]

So you need to write the cat q3.json | jpath $.bus.price into file answer3.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q4.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "$20,000"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q4.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer4.sh in the /root directory.

```
cat q4.json | jpath $.vehicles.car.price
[
  "$20,000"
]

So you need to write the cat q4.json | jpath $.vehicles.car.price into file answer4.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q5.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
    [
        {
            "model": "KDJ39848T",
            "location": "front-right"
        },
        {
            "model": "MDJ39485DK",
            "location": "front-left"
        },
        {
            "model": "KCMDD3435K",
            "location": "rear-right"
        },
        {
            "model": "JJDH34234KK",
            "location": "rear-left"
        }
    ]
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q5.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer5.sh in the /root directory.

```
cat q5.json | jpath $.car.wheels
[
  [
    {
      "model": "KDJ39848T",
      "location": "front-right"
    },
    {
      "model": "MDJ39485DK",
      "location": "front-left"
    },
    {
      "model": "KCMDD3435K",
      "location": "rear-right"
    },
    {
      "model": "JJDH34234KK",
      "location": "rear-left"
    }
  ]
]

So you need to write the cat q5.json | jpath $.car.wheels into file answer5.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q6.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  {
    "model": "KCMDD3435K",
    "location": "rear-right"
  }
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q6.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer6.sh in the /root directory.

```
cat q6.json | jpath $.car.wheels[2]
[
  {
    "model": "KCMDD3435K",
    "location": "rear-right"
  }
]

So you need to write the cat q6.json | jpath $.car.wheels[2] into file answer6.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q7.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "KCMDD3435K"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q7.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer7.sh in the /root directory.

```
cat q7.json | jpath $.car.wheels[2].model
[
  "KCMDD3435K"
]

So you need to write the cat q7.json | jpath $.car.wheels[2].model into file answer7.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q8.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  [
    {
      "month": "june",
      "amount": 1400
    },
    {
      "month": "july",
      "amount": 2400
    },
    {
      "month": "august",
      "amount": 3400
    }
  ]
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q8.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer8.sh in the /root directory.

```
cat q8.json | jpath $.employee.payslips
[
  [
    {
      "month": "june",
      "amount": 1400
    },
    {
      "month": "july",
      "amount": 2400
    },
    {
      "month": "august",
      "amount": 3400
    }
  ]
]

So you need to write the cat q8.json | jpath $.employee.payslips into file answer8.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q9.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  {
    "month": "august",
    "amount": 3400
  }
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q9.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer9.sh in the /root directory.

```
cat q9.json | jpath $.employee.payslips[2]
[
  {
    "month": "august",
    "amount": 3400
  }
]

So you need to write the cat q9.json | jpath $.employee.payslips[2] into file answer9.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q10.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  3400
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q10.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer10.sh in the /root directory.

```
cat q10.json | jpath $.employee.payslips[2].amount
[
  3400
]

So you need to write the cat q10.json | jpath $.employee.payslips[2].amount into file answer10.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q11.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  {
    "id": "914",
    "firstname": "Malala",
    "surname": "Yousafzai",
    "motivation": "\"for their struggle against the suppression of children and young people and for the right of all children to education\"",
    "share": "2"
  }
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q11.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer11.sh in the /root directory.

```
cat q11.json | jpath $.prizes[5].laureates[1]
[
  {
    "id": "914",
    "firstname": "Malala",
    "surname": "Yousafzai",
    "motivation": "\"for their struggle against the suppression of children and young people and for the right of all children to education\"",
    "share": "2"
  }
]

So you need to write the cat q11.json | jpath $.prizes[5].laureates[1] into file answer11.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q12.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "car"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q12.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer12.sh in the /root directory.

```
cat q12.json | jpath $[0]
[
  "car"
]

So you need to write the cat q12.json | jpath $[0] into file answer12.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q13.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "car",
  "bike"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q13.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer13.sh in the /root directory.

```
cat q13.json | jpath '$[0,3]'
[
  "car",
  "bike"
]

So you need to write the cat q13.json | jpath $[0,3] into file answer13.sh.
```

* JSON PATH - Wild Cards

* Develop a JSON PATH query to extract the kind of object. A file named q1.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "value1",
  "value2"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q1.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer1.sh in /root directory.

```
cat q1.json | jpath $.*
[
  "value1",
  "value2"
]

So you need to write the cat q1.json | jpath $.* into file answer1.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q2.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "blue",
  "white"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q2.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer2.sh in /root directory.

```
cat q2.json | jpath $.*.color
[
  "blue",
  "white"
]

So you need to write the cat q2.json | jpath $.*.color into file answer2.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q3.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "$20,000",
  "$120,000"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q3.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer3.sh in /root directory.

```
cat q3.json | jpath $.vehicles.*.price
[
  "$20,000",
  "$120,000"
]

So you need to write the cat q3.json | jpath $.vehicles.*.price into file answer3.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q4.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "KDJ39848T",
  "MDJ39485DK",
  "KCMDD3435K",
  "JJDH34234KK"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q4.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer4.sh in /root directory.

```
cat q4.json | jpath '$[*].model'
[
  "KDJ39848T",
  "MDJ39485DK",
  "KCMDD3435K",
  "JJDH34234KK"
]

So you need to write the cat q4.json | jpath '$[*].model' into file answer4.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q5.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "KDJ39848T",
  "MDJ39485DK",
  "KCMDD3435K",
  "JJDH34234KK"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q5.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer5.sh in /root directory.

```
cat q5.json | jpath $.car.wheels[*].model
[
  "KDJ39848T",
  "MDJ39485DK",
  "KCMDD3435K",
  "JJDH34234KK"
]

So you need to write the cat q5.json | jpath $.car.wheels[*].model into file answer5.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q6.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "KDJ39848T",
  "MDJ39485DK",
  "KCMDD3435K",
  "JJDH34234KK",
  "BBBB39848T",
  "BBBB9485DK",
  "BBBB3435K",
  "BBBB4234KK"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q6.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer6.sh in /root directory.

```
cat q6.json | jpath $.*.wheels[*].model
[
  "KDJ39848T",
  "MDJ39485DK",
  "KCMDD3435K",
  "JJDH34234KK",
  "BBBB39848T",
  "BBBB9485DK",
  "BBBB3435K",
  "BBBB4234KK"
]

So you need to write the cat q6.json | jpath $.*.wheels[*].model into file answer6.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q7.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  1400,
  2400,
  3400
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q7.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer7.sh in /root directory.

```
cat q7.json | jpath $.employee.payslips[*].amount
[
  1400,
  2400,
  3400
]

So you need to write the cat q7.json | jpath $.employee.payslips[*].amount into file answer7.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q8.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "Arthur",
  "Gérard",
  "Donna",
  "Frances H.",
  "George P.",
  "Sir Gregory P.",
  "James P.",
  "Tasuku",
  "Denis",
  "Nadia",
  "William D.",
  "Paul M.",
  "Kailash",
  "Malala",
  "Rainer",
  "Barry C.",
  "Kip S.",
  "Jacques",
  "Joachim",
  "Richard",
  "Jeffrey C.",
  "Michael",
  "Michael W."
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q8.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer8.sh in /root directory.

```
cat q8.json | jpath $.prizes[*].laureates[*].firstname
[
  "Arthur",
  "Gérard",
  "Donna",
  "Frances H.",
  "George P.",
  "Sir Gregory P.",
  "James P.",
  "Tasuku",
  "Denis",
  "Nadia",
  "William D.",
  "Paul M.",
  "Kailash",
  "Malala",
  "Rainer",
  "Barry C.",
  "Kip S.",
  "Jacques",
  "Joachim",
  "Richard",
  "Jeffrey C.",
  "Michael",
  "Michael W."
]

So you need to write the cat q8.json | jpath $.prizes[*].laureates[*].firstname into file answer8.sh.
```

* Develop a JSON PATH query to extract the kind of object. A file named q9.json is provided in the terminal. Your task is to develop a JSON path query to extract the expected output from the Source Data.

Expected output should be like this

[
  "Kailash",
  "Malala"
]

You can test the JSON PATH query as below (noted that the query below is just sample, not a solution).

cat q9.json | jpath $.property1
[
  "value1"
]

If the output matched the expectation then write the whole command into a file named answer9.sh in /root directory.

```
cat q9.json | jpath '$.prizes[?(@.year == 2014)].laureates[*].firstname'
[
  "Kailash",
  "Malala"
]

So you need to write the cat q9.json | jpath '$.prizes[?(@.year == 2014)].laureates[*].firstname' into file answer9.sh.
```

* JSON PATH - LISTS

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Apple"
]

Save the the query to filename answer1.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output $.kind

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[0]'

Save the command used for the query to filename answer1.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Apple"
  "Facebook"
]

Save the query to filename answer2.sh under the root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[0,4]'

save the command used for the query to filename answer2.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Apple",
  "Google",
  "Microsoft",
  "Amazon",
  "Facebook"
]

Save the query to filename answer3.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[0:5]'

save the command used for the query to filename answer3.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Microsoft",
  "Amazon",
  "Facebook",
  "Coca-Cola",
  "Samsung"
]

Save the query to filename answer4.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[2:7]'

save the command used for the query to filename answer4.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "McDonald's"
]

Save the query to filename answer5.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[-1:]'

save the command used for the query to filename answer5.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Samsung",
  "Disney",
  "Toyota",
  "McDonald's"
]

Save the query to filename answer6.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[-4:]'

save the command used for the query to filename answer6.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Amazon",
  "Facebook",
  "Coca-Cola",
  "Samsung",
  "Disney",
  "Toyota"
]

Save the query to filename answer7.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[3:9]'

save the command used for the query to filename answer7.sh
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "In Ltd"
]

Save the query to filename answer8.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[-1:]'

save the command used for the query to filename answer8.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Consectetuer Adipiscing Elit Limited",
  "Accumsan Convallis PC",
  "In Ltd"
]

Save the query to filename answer9.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[-3:]'

save the command used for the query to filename answer9.sh under root directory.
```

* Develop a JSON path query to extract the expected output from the Source Data.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "Magna Nec Corp.",
  "Egestas Corporation",
  "Est Congue Associates",
  "Non Cursus Inc.",
  "Elit Fermentum Associates",
  "Consectetuer Adipiscing Elit Limited"
]

Save the query to filename answer10.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[-8:-2]'

save the command used for the query to filename answer10.sh under root directory.
```

* Develop a JSON path query to extract the phone numbers of first 5 users.
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  "+1 (850) 469-2827",
  "+1 (825) 558-2599",
  "+1 (946) 495-3285",
  "+1 (948) 406-2941",
  "+1 (903) 413-2132"
]

Save the query to filename answer11.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[0:5].phone'

save the command used for the query to filename answer11.sh under root directory.
```

* Develop a JSON path query to extract the age of last 5 users
A file named input.json is provided in the terminal. Provide the file as input by the cat command.
for example, the command should be like this cat filename | jpath $query

The expected output should be like this.

[
  24,
  34,
  20,
  37,
  40
]

Save the query to filename answer12.sh under root directory.

```
cat filename | jpath '$[query]'
Filename - input.json, It is an input for jpath query.
It is the query to get the required output '$[xx]'

So the final command would be like this to get output try it yourself.

cat input.json | jpath '$[-5:].age'

save the command used for the query to filename answer12.sh under root directory.
```

* JSON PATH - KUBERNETES

* In this lab, we provide you with a Kubernetes pod information file in JSON format. Try to build JSON path queries with CLI to extract information from JSON.

* In the given data, what is the data type of the root element?

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "nginx-pod",
    "namespace": "default"
  },
  "spec": {
    "containers": [
      {
        "image": "nginx:alpine",
        "name": "nginx"
      }
    ],
    "nodeName": "node01"
  }
}

```
The root element is the top most object in a JSON document. Look at the encapsulation. Is it square brackets [] or curly brackets {} ? If it's square brackets its an array/list. If its curly brackets it is a dictionary.
```

* How many properties/fields does the root object(dictionary) have?

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "nginx-pod",
    "namespace": "default"
  },
  "spec": {
    "containers": [
      {
        "image": "nginx:alpine",
        "name": "nginx"
      }
    ],
    "nodeName": "node01"
  }
}

```
The root dictionary has properties/fields apiVersion, kind, metadata, and spec. so the answer will be 4.
```

* In the given data, what is the data type of the root element?

[
  {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
      "name": "web-pod-1",
      "namespace": "default"
    },
    "spec": {
      "containers": [
        {
          "image": "nginx:alpine",
          "name": "nginx"
        }
      ],
      "nodeName": "node01"
    }
  },
  {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
      "name": "web-pod-2",
      "namespace": "default"
    },
    "spec": {
      "containers": [
        {
          "image": "nginx:alpine",
          "name": "nginx"
        }
      ],
      "nodeName": "node02"
    }
  }
]

```
The data type of the root element is List
```

* How many items does the list have?

[
  {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
      "name": "web-pod-1",
      "namespace": "default"
    },
    "spec": {
      "containers": [
        {
          "image": "nginx:alpine",
          "name": "nginx"
        }
      ],
      "nodeName": "node01"
    }
  },
  {
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
      "name": "web-pod-2",
      "namespace": "default"
    },
    "spec": {
      "containers": [
        {
          "image": "nginx:alpine",
          "name": "nginx"
        }
      ],
      "nodeName": "node02"
    }
  }
]

```
Within the array/list each item is a dictionary as its encapsulated in curly brackets. So it's a List of Dictionaries. So count each item of that list. Answer is 2
```

* What is the data type of the apiVersion field?

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "nginx-pod",
    "namespace": "default"
  },
  "spec": {
    "containers": [
      {
        "image": "nginx:alpine",
        "name": "nginx"
      }
    ],
    "nodeName": "node01"
  }
}

```
The apiVersion has a value v1. So its data type should be string
```

* What is the data type of the metadata field?

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "nginx-pod",
    "namespace": "default"
  },
  "spec": {
    "containers": [
      {
        "image": "nginx:alpine",
        "name": "nginx"
      }
    ],
    "nodeName": "node01"
  }
}

```
The metadata field has a value that's encapsulated in curly braces. So it should be a dictionary.
```

* Which of the below is the best description of the type of data in the containers field?

{
  "apiVersion": "v1",
  "kind": "Pod",
  "metadata": {
    "name": "nginx-pod",
    "namespace": "default"
  },
  "spec": {
    "containers": [
      {
        "image": "nginx:alpine",
        "name": "nginx"
      }
    ],
    "nodeName": "node01"
  }
}

```
The containers field is an array as its values are encapsulated in square brackets. But within the array each item is a dictionary as its encapsulated in curly brackets. So its a List of Dictionaries
```

* Now let's get into some action with JSON PATH.

Develop a JSON PATH query to extract the kind of object. A file named input.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  "Pod"
]


save query command to filename answer9.sh under root directory.

```
cat filename | jpath $.query
Filename - input.json, It is an input for jpath query.
It is the query to get the required output $.kind


So the final command would be like this to get output try it yourself.

cat input.json | jpath $.kind

save the command used for the query to filename answer9.sh under the root directory.
```

* Develop a JSON PATH query to get the name of the POD.A file named input.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  "nginx-pod"
]


save query command to filename answer10.sh under root directory.

```
cat filename | jpath $.query
Filename - input.json, It is an input for jpath query.
It is the query to get the required output $.metadata.name


So the final command would be like this to get output try it yourself.

cat input.json | jpath $.metadata.name

save the command used for the query to filename answer10.sh under root directory.
```

* Develop a JSON PATH query to get the name of the POD. A file named input.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  "node01"
]


Save query command to filename answer11.sh under root directory.

```
cat filename | jpath $.query
Filename - input.json, It is an input for jpath query.
It is the query to get the required output $.spec.nodeName


So the final command would be like this to get output try it yourself.

cat input.json | jpath $.spec.nodeName

save the command used for the query to filename answer11.sh under root directory.
```

* Develop a JSON PATH query to get the name of the POD. A file named input.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  {
    "image": "nginx:alpine",
    "name": "nginx"
  }
]


Save query command to filename answer12.sh under root directory.

```
cat filename | jpath $.query
Filename - input.json, It is an input for jpath query.
It is the query to get the required output $.spec.containers[0]


So the final command would be like this to get output try it yourself.

cat input.json | jpath $.spec.containers[0]

save the command used for the query to filename answer12.sh under root directory.
```

* Develop a JSON PATH query to get the image name under the containers section.

A file named input.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  "nginx:alpine"
]


Save query command to filename answer13.sh under root directory.

```
cat filename | jpath $.query
Filename - input.json, It is an input for jpath query.
It is the query to get the required output $.spec.containers[0].image


So the final command would be like this to get output try it yourself.

cat input.json | jpath $.spec.containers[0].image

save the command used for the query to filename answer13.sh under root directory.
```

* We now have POD status too. Develop a JSON PATH query to get the phase of the pod under the status section.


A file named k8status.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  "Pending"
]


Save query command to filename answer14.sh under root directory.

```
cat filename | jpath $.query
Filename - k8status.json, It is an input for jpath query.
It is the query to get the required output $.status.phase


So the final command would be like this to get output try it yourself.

cat k8status.json | jpath $.status.phase

save the command used for the query to filename answer14.sh under root directory.
```

* Develop a JSON PATH query to get the reason for the state of the container under the status section.

A file named k8status.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  "ContainerCreating"
]


Save query command to filename answer15.sh under root directory. 

```
cat filename | jpath $.query
Filename - k8status.json, It is an input for jpath query.
It is the query to get the required output $.status.containerStatuses[0].state.waiting.reason


So the final command would be like this to get output try it yourself.

cat k8status.json | jpath $.status.containerStatuses[0].state.waiting.reason

Save the command used for the query to filename answer15.sh under root directory.
```

* Develop a JSON PATH query to get the restart count of the redis-container under the status section.

A file named k8status.json is provided in the terminal. Provide the file as input to the cat command
for example, the command should be like this cat filename | jpath $.query

Expected output should be like this

[
  2
]


Save query command to filename answer16.sh under root directory.

```
cat filename | jpath $.query
Filename - k8status.json, It is an input for jpath query.
It is the query to get the required output $.status.containerStatuses[1].restartCount


So the final command would be like this to get output try it yourself.

cat k8status.json | jpath $.status.containerStatuses[1].restartCount

Save the command used for the query to filename answer16.sh under root directory.
```

* Develop a JSON PATH query to get all pod names.

A file podslist.json file is provided in the terminal.
The expected output should be like this.

[
  "web-pod-1",
  "web-pod-2",
  "web-pod-3",
  "web-pod-4",
  "db-pod-1"
]


save query command to filename answer17.sh under root directory.

```
cat filename | jpath $.query
Filename - podslist.json is an input for jpath query.
It is the query to get the required output $[*].metadata.name


So the final command would be like this to get output try it yourself.

cat podslist.json | jpath '$[*].metadata.name'

Save the command used for the query to filename answer17.sh under root directory.
```

* Develop a JSON PATH query to get all pod names.

A file userslist.json file is provided in the terminal.
The expected output should be like this.

[
  "aws-user",
  "dev-user",
  "test-user"
]


save query command to filename answer18.sh under root directory.

```
cat filename | jpath $.query
Filename - userslist.json is an input for jpath query.
It is the query to get the required output $.users[*].name


So the final command would be like this to get output try it yourself.

cat userslist.json | jpath $.users[*].name

Save the command used for the query to filename answer18.sh under root directory.
```

* Kubernetes Data Objects and JSON PATH exercises:

https://mmumshad.github.io/json-path-quiz/index.html#!/?questions=questionskub1

https://mmumshad.github.io/json-path-quiz/index.html#!/?questions=questionskub2
