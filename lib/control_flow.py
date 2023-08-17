#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else: 
         return "Access denied"
    

 def hows_the_weather(temperature):
    if temperature <40:
        return "its brisk out there!"
    elif 40 <= temperature <= 65:
        return "its a littly chilly out there"
    elif temperature >85:
        return "its too dang hot out there!"
    else: 
        return "its perfect out there!"
    # your code here
    

 def fizzbuzz(num):
    if num % 3 ==0 and num % 5 == 0:
      return "FizzBuzz"
    elif num % 3 == 0:
      return "Fizz" 
    elif num % 5 ==0: 
      return "Buzz" 
    else :
      return num

    

 def calculator(operation, num1, num2):
    if operation == "+":
      return num1 +num2
    elif operation == "-":
      return num1 -num2
    elif operation == "*":
      return num1 * num2
    elif operation == "/":
      if num2 != 0: # avoid division by zero
          return num1 /num2
      else: 
          return "invalid operation! cannot divide by zero."
    else: 
      return "invalid operation!"