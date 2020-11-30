# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:36:10 2020

@author: KaiMcGregor
"""
from dataStructures.linkedqueue import LinkedQueue
from dataStructures.linkedlist import LinkedList
import os

def getStrInput(prompt, errorMessage):
    while True:
        userInput = input(f'{prompt} ').strip()
        if userInput != '':
            return userInput.upper()
        else:
            print(errorMessage)
            
def getIntInput(prompt, errorMessage, lowerLimit, upperLimit):
    while True:
        try:
            userInput = int(input(f'{prompt} ').strip())
            if lowerLimit <= userInput <= upperLimit:
                return userInput
            else:
                print(errorMessage)
        except ValueError:
            print(errorMessage)

class ToDoList():
    def __init__(self):
        self.uncompletedList = LinkedQueue()
        self.completedList = LinkedList()
        
        
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


def menu(todoList):
    menuChoice = 1 #instantiating to enter the loop
    while menuChoice != 7:
        # Get user menu choice
        prompt = 'Would you like to:\n(1) Add an item\n(2) Remove an item\n(3) Complete an item\n(4) Import tasks from a file\n(5) Print the list\n(6) Save list to a file\n(7) Exit the program\n\nEnter Choice:'
        errorMessage = 'Input must be between 1 and 7 (inclusive)'
        menuChoice = getIntInput(prompt=prompt, errorMessage=errorMessage, lowerLimit=1, upperLimit=7)
        
        # Add Item
        if menuChoice == 1:
            # Get the task to add
            prompt = 'Enter the task you would like to add:'
            errorMessage = 'Input cannot be empty'
            itemAdded = getStrInput(prompt=prompt, errorMessage=errorMessage)
            
            # Add the task
            todoList.uncompletedList.add(itemAdded)
            
        # Delete an item
        elif menuChoice == 2:
            # Unavailable if list is empty
            if todoList.uncompletedList.isEmpty():
                print('The list is empty!')
            else:
                # Get the task to delete
                prompt = 'Enter the name of the task you would like to delete:'
                errorMessage = 'Input cannot be empty'
                itemDeleted = getStrInput(prompt=prompt, errorMessage=errorMessage)
                
                # Check if the task is in the list and reprompt if necessary
                while itemDeleted not in todoList.uncompletedList:
                    print('That item is not in the list.. try again.')
                    itemDeleted = getStrInput(prompt=prompt, errorMessage=errorMessage)
                    
                # Remove task
                todoList.uncompletedList.remove(itemDeleted)
                
        # Mark Item as completed
        elif menuChoice == 3:
            # Unavailable if list is empty
            if todoList.uncompletedList.isEmpty():
                print('The list is empty!')
            
            # Use queue method if list is only 1 in size
            elif todoList.uncompletedList.size == 1:
                itemCompleted = todoList.uncompletedList.pop()
                todoList.completedList.add(itemCompleted)
                print(itemCompleted + ' is now completed')
                
            else:
                # Choose task completion method
                promptChoice = 'Would you like to mark as completed:\n(1) ' + todoList.uncompletedList.peek() + '\n(2) Another item\n\nEnter Choice:'
                errorMessage = 'Input must be between 1 and 2 (inclusive)'
                userChoice = getIntInput(prompt=promptChoice, errorMessage=errorMessage, lowerLimit=1, upperLimit=2)
                
                if userChoice == 1:
                    itemCompleted = todoList.uncompletedList.pop()
                    todoList.completedList.add(itemCompleted)
                    print(itemCompleted + ' is now completed')
                    
                elif userChoice == 2:
                    promptItemChoice = 'Enter the name of the task you would like to mark as completed:'
                    errorMessage = 'Input cannot be empty'
                    itemCompleted = getStrInput(prompt=promptItemChoice, errorMessage=errorMessage)
                    
                    while itemCompleted not in todoList.uncompletedList:
                        print('That item is not in the list.. try again.')
                        itemCompleted = getStrInput(prompt=promptItemChoice, errorMessage=errorMessage)
                        
                    todoList.completedList.add(itemCompleted)
                    todoList.uncompletedList.remove(itemCompleted)
                    print(itemCompleted + ' is now completed')
                    
        # Import from file
        elif menuChoice == 4:
            pass
        
        # Print List
        elif menuChoice == 5:
            prompt = 'Would you like to display:\n(1) The uncompleted list\n(2) The completed list\n(3) Both\n\nEnter Choice:'
            errorMessage = 'Input must be between 1 and 3 (inclusive)'
            displayChoice = getIntInput(prompt=prompt, errorMessage=errorMessage, lowerLimit=1, upperLimit=3)
            
            if displayChoice == 1:
                todoList.printList([todoList.uncompletedList])
                
            elif displayChoice == 2:
                todoList.printList([todoList.completedList])
                
            elif displayChoice == 3:
                todoList.printList([todoList.completedList, todoList.uncompletedList])
                
        # Print to file
        elif menuChoice == 6:
            # Choose list to save and validate input
            while True:
                choice = input("Would you like to save\n(1) The uncompleted list\n(2) The completed list\n\nEnterChoice: ").strip()
                
                try:
                    choice = int(choice)
                    if choice == 1 or choice == 2:
                        break
                    else:
                        print("Please enter 1 or 2")
                except ValueError:
                    print("Please enter 1 or 2")
                    
            # Get and validate filename input
            goodName = 0
            while goodName == 0:
                fileName = input("What is the name of the file you want to write to: ").strip()
                if len(fileName) > 0:
                    goodName = 1
            
            # Write to file        
            file = open(fileName, "w")
            if (choice == 1):
                for item in todoList.uncompletedList:
                    file.write('%s\n' % item)
                    
            elif (choice == 2):
                for item in todoList.completedList:
                    file.write('%s\n' % item)
                    
            file.close()
        
            
    print('Exiting...')





def main():
    someList = ToDoList()
    menu(someList)

if __name__ == '__main__':
    main()


        
