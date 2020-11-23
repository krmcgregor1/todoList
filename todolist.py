# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:36:10 2020

@author: KaiMcGregor
"""
from dataStructures.linkedqueue import LinkedQueue
from dataStructures.linkedlist import LinkedList
from cmdInputOutput import dataTypeConstruct, getInput, printTable
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
        
        # print table middle alligned
        printTable(tableList, align='m')
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
        
        