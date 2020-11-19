# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:36:10 2020

@author: KaiMcGregor
"""
from linkedqueue import LinkedQueue
from cmdInputOutput import dataTypeConstruct, methodApplier, getInput, printTable

class ToDoList(LinkedQueue):
    def __init__(self, sourceCollection=None):
        LinkedQueue.__init__(self, sourceCollection)
        
    def printList(self):
        # Create a list representing a table
        tableList = [['Index', 'Completed', 'Task']]
        index = 1
        for task, completed in self:
            if completed:
                completed = 'X'
            else:
                completed = ' '
            
            tableList.append([index, completed, task])
            
            index += 1
        
        # print table middle alligned
        print()
        printTable(tableList, align='m')
        
    def menu(self):
        intType = dataTypeConstruct(int) # Specify datatypes for getInput
        strType = dataTypeConstruct(str)
        
        menuChoice = 1 #instantiating to enter the loop
        while menuChoice != 5:
            prompt = 'Would you like to:\n(1) Add an item\n(2) Remove an item\n(3) Mark an item as completed\n(4) Print the list\n(5) Exit the program\n\nEnter Choice'
            errorMessage = 'Input must be between 1 and 4 (inclusive)'
            menuChoice = getInput(1, prompt=prompt, errorMessage=errorMessage, dataType=intType, lowerLimit=1, upperLimit=4)
            # Add Item
            if menuChoice == 1:
                prompt = 'Enter the task you would like to add'
                itemAdded = getInput(1, prompt=prompt, errorMessage=errorMessage, dataType=strType)
                self.add(itemAdded)
            # Remove Item
            elif menuChoice == 2:
                pass
            # Mark Item as completed
            elif menuChoice == 3:
                pass
            # Print List
            elif menuChoice == 4:
                self.printList()
        
        print('Exiting...')
        
someList = ToDoList()
someList.menu()
        
        