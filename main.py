import json
import sys
import os
from os import path

#checks to see if the file exists
def made():
    exists=path.exists("acc.json")#checks to see if the file exists and sets a boolean value
    return exists#returns the value

#Reads from a JSON file
def read(accList):
    exists = made()#checks to see if the file exists
    if exists is False:#if it does not
        accountFile=open("acc.json", "w+")#create the file
    else:#if it does
        accountFile = open('acc.json',"r")#open it with read option
        first = accountFile.read(1)#check to see if the file is empty
        if not first:#if it is
            print("No accounts")#print no accounts
        else:#if it is not empty
            accountFile.seek(0)#set the parser to character zero
            accList=json.load(accountFile)#load the JSON into a list of dictionaries
    accountFile.close()#close the file
    return(accList)#return the list

#Writes to the JSON file
def write(accList):
    with open('acc.json',"w") as accountFile:#opens the file with write option
        accountFile.write(json.dumps(accList, indent = 4, sort_keys=True))#write the profiles to the file with some styling
    accountFile.close()#close the file

#Searches for a specified profile, and if found returns the data as a dict
def search(user,password,accList):
    for a in accList['account']:#searched the account list
        if a['username'] == user and a['password'] == password:#if the username and the password find a match
            account={#create a dictionary with the personal info
                "name" : a['name'],#assign the user name
                "city" : a['city'],#assign the city they live in
                "age" : a['age']#assign their age
            }#account
            return account#return the dictionary
            break#break
        else:#if the user is not found
            return False#return the false
            break#break
#acts as a login for the user
def login(accList):
    accList=read(accList)#populate the account list
    user=input("Please enter your username: ")#get the username
    #To Do: Idiot Proof here
    password=input("Please enter your password: ")#get the password
    #To Do: Idiot Proof here
    found=search(user,password,accList)#search for the user

    if type(found)== bool:#if the return type is boolean
        if found is False:#if the boolean is false
            print("User not found.")#print message
            choice=input("Press 1 to try again, 2 to create an account, or 3 to exit:\n")#allow the user to make a decision if the username is not found
            #To Do: Idiot Proof here
            choice=int(choice)#set the variable to int
            if choice == 1:#if the user chooses 1
                login(accList)#re-run this method
            elif choice == 2:#if the user chooses 2
                create(accList)#call the create function
            elif choice == 3:#if the user selects 3
                print("Goodbye")#print Goodbye
                sys.exit()#exit the program
            else:#if the user enters something else
                print("Error. Not a choice. Exiting.")#WILL CHANGE DURING IDIOT PROOFING
            #To Do: Idiot Proof here
    elif type(found)== dict:#if the type returns as dict
        print("User found.")#print that the user has been found
        print("Name:\t"+found['name'])#print name
        print("City:\t"+found['city'])#print city
        print("Age:\t"+found['age'])#print their age
        sys.exit()#exit the program

#creates the users account
def create(accList):
    accList=read(accList)#loads the list of accounts
    name=input("Please enter your name: ")#get the user name
    age =input("How old are you: ")#get the user age
    city = input("What city do you live in: ")#get the users city
    user=input("Please create a username: ")#ask the user to create a username
    password=input("Please create a  password: ")#ask the user to create a password
    accList["account"].append({#create a dictionary with the users information and add it to a list
        "name": name,
        "age": age,
        "city": city,
        "username": user,
        "password": password
    })
    write(accList)#send the list to the write method

#this is the main function
def main():
    accList = {}#create a dictionary object
    accList["account"] = []#create a list of dictionaries to hold the user accounts
    returning=input("Welcome to Cael's login screen.\nDo you already have an account? ")#greeting message
    #To Do: Idiot Proof here
    if(returning.lower()=="yes"):#if the user has an account
       login(accList)#call the login function
    elif(returning.lower()=="no"):#if the user does not have an account
       create(accList)#call the create function
    else:#if the user says something else
       print("Sorry that's not a valid answer. Please only type \'Yes\' or \'No\'.")#tell them that they did not enter a valid answer
    
main()#call the main function to start the program
#TO DO: ADD COMMENTS AND IDIOT PROOFING