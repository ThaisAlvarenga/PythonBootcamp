"""
Name: Thais Alvarenga
Course: 100 Days of Python
Description:  Book name generator
Date: 04/02/2023
"""
import random

titleWords =["Chronicles", "Adventures" ,"Tales", "Journey"]

print("WELCOME TO BOOK NAME GENERATOR")
print("My job is to help you find the name for your best selling book!")
noun = input("Give me a noun that describes your protagonist: ")
adjective = input("Now give me an adjective about the mood of your book: ")

print("Your noun book title is...")
print("The " + titleWords[random.randint(1,4)] + " of the " + adjective.capitalize() + " " + noun.capitalize())