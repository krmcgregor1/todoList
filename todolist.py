# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:36:10 2020

@author: KaiMcGregor
"""
from dataStructures.linkedqueue import LinkedQueue
from dataStructures.linkedlist import LinkedList
from cmdInputOutput import dataTypeConstruct, getInput
from os import system, name
import csv

class ToDoList():
    def __init__(self):
        self.todoList = LinkedQueue()
        self.completedList = LinkedList()
        
        # Clear screen after each entry, set to false when errors occur
        self.__clearScreen = True
        
        
    def printList(self, printLists=[]):
        # Create a list representing a table
        tableList = [['Index', 'Completed', 'Task']]
        index = 1
        for printList in printLists:
            for task in printList:
                if type(printList) == LinkedList:
                    completed = 'X'
                else:
                    completed = ' '
            
                tableList.append([index, completed, task])
            
                index += 1
        
        
        #Gets length of the longest string in each column
        largLenList = [0 for x in range(0, len(tableList[0]))]
        for row in tableList:
            for x in range(0, len(row)):
                if len(str(row[x])) > largLenList[x]:
                    cellLen = len(str(row[x]))
                    largLenList[x] = cellLen
                    
        #Add two (for padding) to the list
        largLenList = [x + 2 for x in largLenList]
        
        # print table middle alligned
        for row in tableList:
            rowString = ''
            for x in range(len(row)):
                #Get space difference between largest length and current item
                spacesString = ''.join([' ' for x in range(largLenList[x] - len(str(row[x])))])
                #Odd spacing, puts the extra space on the right
                if len(spacesString) % 2:
                    midPoint = int((len(spacesString) - 1) / 2)
                    spacesStringLeft = spacesString[:midPoint]
                    spacesStringRight = spacesString[:midPoint+1]
                                
                    rowString += f'{spacesStringLeft}{row[x]}{spacesStringRight}'
                #Even spacing
                else:
                    midPoint = int(len(spacesString) / 2)
                    spacesString = spacesString[:midPoint]
                                
                    rowString += f'{spacesString}{row[x]}{spacesString}'
                    
            print(rowString)
        
        print()
        
        
    # Read from file, default to 'todoList.csv'
    def readFromFile(self, filename='todoList.csv'):
        pass
    
    # save to default filename 'todoList.csv'
    def saveToFile(self):
        pass
        
    def menu(self):
        intType = dataTypeConstruct(int) # Specify datatypes for getInput
        strType = dataTypeConstruct(str)
        
        menuChoice = 1 #instantiating to enter the loop
        displayChoice = None
        while menuChoice != 6:
            # Clearing the screen will only work through terminal (I think)
            if self.__clearScreen:
                # Apparently specifys Windows
                if name == 'nt':
                    system('cls')
                # Vs Linux
                else:
                    system('clear')
            else:
                self.__clearScreen = True
                
            if displayChoice == 1:
                self.printList([self.todoList])
                displayChoice = None
            elif displayChoice == 2:
                self.printList([self.completedList])
                displayChoice = None
            elif displayChoice == 3:
                self.printList([self.completedList, self.todoList])
                displayChoice = None
            
            prompt = 'Would you like to:\n(1) Add an item\n(2) Remove an item\n(3) Complete an item\n(4) Import taks from a file\n(5) Print the list\n(6) Exit the program\n\nEnter Choice'
            errorMessage = 'Input must be between 1 and 6 (inclusive)'
            menuChoice = getInput(1, prompt=prompt, errorMessage=errorMessage, dataType=intType, lowerLimit=1, upperLimit=6)
            
            
            # Add Item
            if menuChoice == 1:
                prompt = 'Enter the task you would like to add'
                itemAdded = getInput(1, prompt=prompt, errorMessage=errorMessage, dataType=strType)
                self.todoList.add(itemAdded)
            # Delete an item
            elif menuChoice == 2:
                pass
            # Mark Item as completed
            elif menuChoice == 3:
                pass
            # Import from file
            elif menuChoice == 4:
                pass
            # Print List
            elif menuChoice == 5:
                prompt = 'Would you like to display:\n(1) The uncompleted list\n(2) The completed list\n(3) Both\n\nEnter Choice'
                errorMessage = 'Input must be between 1 and 3 (inclusive)'
                displayChoice = getInput(1, prompt=prompt, errorMessage=errorMessage, dataType=intType, lowerLimit=1, upperLimit=3)
                
        print('Exiting...')
        
someList = ToDoList()
someList.menu()


        
        