# Python Module 1: Beginner Samples with Outputs

Kickstart your Python journey with foundational examples that show both the code and its output. Each section introduces a new concept with short, runnable snippets you can try in any Python 3 interpreter.

## Getting Started

### Hello, World!
```python
print("Hello, world!")
```
```
Hello, world!
```

### Comments
```python
# This is a comment; it explains what the code does.
print("Comments are ignored by Python")
```
```
Comments are ignored by Python
```

## Working with Data

### Variables and Types
```python
age = 25        # int
pi = 3.14159    # float
name = "Amina"  # str
is_student = True  # bool

print(type(age))
print(type(pi))
print(type(name))
print(type(is_student))
```
```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### Arithmetic Operations
```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```
```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
```

### Reading User Input
```python
name = input("What is your name? ")
print("Nice to meet you,", name)
```
```
What is your name? Amina
Nice to meet you, Amina
```

## String Essentials

### Concatenation and Formatting
```python
first = "Python"
second = "Basics"
combined = first + " " + second
message = f"Welcome to {combined}!"

print(combined)
print(message)
```
```
Python Basics
Welcome to Python Basics!
```

### Useful String Methods
```python
phrase = "learning python is fun"

print(phrase.title())
print(phrase.upper())
print(phrase.replace("fun", "powerful"))
print("python" in phrase)
```
```
Learning Python Is Fun
LEARNING PYTHON IS FUN
learning python is powerful
True
```

## Collections Overview

### Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(f"First fruit: {fruits[0]}")
print(f"All fruits: {fruits}")
```
```
First fruit: apple
All fruits: ['apple', 'banana', 'cherry', 'date']
```

### Tuples
```python
coordinates = (12.5, 7.3)
print(coordinates)
```
```
(12.5, 7.3)
```

### Dictionaries
```python
student = {
    "name": "Amina",
    "age": 25,
    "courses": ["Math", "Python Basics"]
}

print(student["name"])
print(student.get("courses"))
student["age"] = 26
print(student)
```
```
Amina
['Math', 'Python Basics']
{'name': 'Amina', 'age': 26, 'courses': ['Math', 'Python Basics']}
```

### Sets
```python
unique_numbers = {1, 2, 2, 3}
unique_numbers.add(4)
print(unique_numbers)
```
```
{1, 2, 3, 4}
```

## Control Flow Basics

### Conditional Statements
```python
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Keep practicing!")
```
```
Grade: B
```

### While Loop
```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Lift off!")
```
```
3
2
1
Lift off!
```

### For Loop
```python
for number in range(1, 4):
    print(number)
```
```
1
2
3
```

### Loop with Break and Continue
```python
for number in range(1, 6):
    if number == 3:
        continue
    if number == 5:
        break
    print(number)
```
```
1
2
4
```

## Functions

### Defining and Calling Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Amina"))
```
```
Hello, Amina!
```

### Functions with Default Arguments
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 5))
```
```
9
32
```

## Working with Built-ins

### Using the `len` and `sum` Functions
```python
numbers = [2, 4, 6, 8]
print(len(numbers))
print(sum(numbers))
```
```
4
20
```

### Enumerate and Range Together
```python
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):
    print(index, color)
```
```
1 red
2 green
3 blue
```

## Modules and Libraries

### Importing Modules
```python
import math

print(math.pi)
print(math.sqrt(16))
```
```
3.141592653589793
4.0
```

### Random Numbers
```python
import random

print(random.randint(1, 6))  # Simulates a dice roll between 1 and 6
```
```
4
```

## Next Steps
- Practice by modifying each example.
- Combine ideas to build tiny projects (e.g., number guesser, shopping list tracker).
- Explore Module 4: Python Fundamentals for a deeper dive into language features.

Happy coding!
