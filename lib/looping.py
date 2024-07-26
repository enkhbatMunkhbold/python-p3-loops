#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i >= 0:
        print(i)
        if i == 0:
            print("Happy New Year!")
        i -= 1

def square_integers(int_list):
    int_list = [num * num for num in int_list]
    return int_list        

def fizzbuzz():
   for num in range(101):
      if num == 0:
          continue
      elif num % 3 == 0 and num % 5 == 0:
          print ("FizzBuzz")
      elif num % 3 == 0:
          print ("Fizz")
      elif num % 5 == 0:
          print ("Buzz")
      else:
          print (num)

