# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:44:10 2020

@author: KaiMcGregor

Rewrote this code that I used from previous classes to get user input, ill streamline it as I use it more
If I do end up using it more

9/2/2020:
    Added classes to aid datatype and method application input
    removed walrus operators to aid backwards compatibility
    Changed the returnSpaces function to be more efficient (list comprehension instead of a loop)
10/26/2020:
    Added extrapolation to datatype and method lists to the convTable function,
    one or two rows (including a title row) represents this ex: [[dataTypeConstruct1, dataTypeConstruct2, dataTypeConstruct3]] ---->
    [[dataTypeConstruct1, dataTypeConstruct2, dataTypeConstruct3], [dataTypeConstruct1, dataTypeConstruct2, dataTypeConstruct3], [dataTypeConstruct1, dataTypeConstruct2, dataTypeConstruct3]]
    
    Added comparison operator switching to the getInput function
"""
import operator

#A class so I could stop using confusing list formats to indicate dataTypes
#Takes a constructor and args to perform and can return an object using that from input
class dataTypeConstruct():
    def __init__(self, constructor, args = []):
        self.__constructor = constructor
        self.__args = args
    
    def createObject(self, convValue):
        return self.__constructor(convValue, *self.__args)

#Container to simplify function inputs
#Applies class methods with input arguments to the input object
class methodApplier():
    def __init__(self, method, args = [], beforeConv = True):
        self.__method = method
        self.__args = args
        
        #Var to check if applying these methods before or after a data type conversion
        self.beforeConv = beforeConv
    
    def apply(self, inputVal):
        if hasattr(inputVal, self.__method):
            return getattr(inputVal, self.__method)(*self.__args)
        else:
            return None



#AttribList is formatted in this manner [['attribute1', [args1]], ['attribute2', [args2]]]
#dataType is formatted similarily but only takes one constructor and arg list [dataType, [args]]
#exitKeyword must be a string if it is used
#greaterEqual and lessEqual variables indicate if < is used or <= (>, >=)
def getInput(length, prompt, errorMessage, dataType = dataTypeConstruct(str), 
             lowerLimit = None, upperLimit = None, lessEqual = True, greaterEqual = True, acceptableInputList = None, exitKeyword = None, 
             methodList = [methodApplier('strip')]):
    
    compOperators = []
    if lessEqual:
        compOperators.append(operator.le)
    else:
        compOperators.append(operator.lt)
        
    if greaterEqual:
        compOperators.append(operator.ge)
    else:
        compOperators.append(operator.gt)
        
    returnList = []
    invalidInput = False
    
    while True:
        #Check if desired list length is reached, None meaning it stops when exitKeyword is entered
        if length != None:
            if len(returnList) == length:
                break
        
        if invalidInput:
            print(errorMessage)
            invalidInput = False
        
        try:
            #Get user input, changing prompt style depending on the number of items requested
            if length == 1:
                userInput = input(f'{prompt}: ')
            else:
                userInput = input(f'{prompt} {len(returnList) + 1}: ')
            
            
            #Applies object methods such as upper, lower, or strip to the input if applicable
            for method in methodList:
                #Value indicating if the method should be applied before or after data type conversion
                if method.beforeConv:
                    newVal = method.apply(userInput)
                    if newVal != None:
                        userInput = newVal
                
            #Exit if wanted and input matches
            if exitKeyword != None:
                if userInput == exitKeyword:
                    if length == 1:
                        return None
                    else:
                        break
            
            #Convert to wanted datatype
            userInput = dataType.createObject(userInput)
            
            #Applies object methods such as upper, lower, or strip to the input if applicable
            for method in methodList:
                #Value indicating if the method should be applied before or after data type conversion
                if method.beforeConv == False:
                    newVal = method.apply(userInput)
                    if newVal != None:
                        userInput = newVal
            
            #Add input if no contraints
            if acceptableInputList == None and lowerLimit == None and upperLimit == None:
                returnList.append(userInput)
            else:
                #Bounded by upper and/or lower limits
                if acceptableInputList == None:
                    if upperLimit == None:
                        if compOperators[1](userInput, lowerLimit):
                            returnList.append(userInput)
                        else:
                            #comp failed
                            invalidInput = True
                            continue
                    elif lowerLimit == None:
                        if compOperators[0](userInput, upperLimit):
                            returnList.append(userInput)
                        else:
                            #comp failed
                            invalidInput = True
                            continue
                    else:
                        if compOperators[0](lowerLimit, userInput) and compOperators[0](userInput, upperLimit):
                            returnList.append(userInput)
                        else:
                            #comp failed
                            invalidInput = True
                            continue
                            
                #Bounded by acceptable input list
                else:
                    if userInput in acceptableInputList:
                        returnList.append(userInput)
                    else:
                        #comp failed
                        invalidInput = True
                        continue
               
        #Datatype conversion error
        except ValueError:
            invalidInput = True
            
    #Return single object or whole list depending on list length
    if len(returnList) == 1:
        return returnList[0]
    else:
        return returnList
    

#function to return a blank string of a certain length
def returnSpaces(numSpaces):
    return ''.join([' ' for x in range(numSpaces)])


#tableList holds the table to be displayed
#align can be L, M, or R (Left, middle, right)
#changePrecTypes is a list to hold the datatypes that should have their display precision changed
def printTable(tableList, changePrecTypes = [float], valPrecision=2, align = 'L'):
    floatFormatString = f'{{:.{valPrecision}f}}'
    
    #Gets length of the longest string in each column
    largLenList = [0 for x in range(0, len(tableList[0]))]
    for row in tableList:
        for x in range(0, len(row)):
            if len(str(row[x])) > largLenList[x]:
                cellLen = len(str(row[x]))
                largLenList[x] = cellLen
                
    #Add two (for padding) to the list
    largLenList = [x + 2 for x in largLenList]
    
    
    for row in tableList:
        rowString = ''
        for x in range(0, len(row)):
            if type(row[x]) in changePrecTypes:
                row[x] = floatFormatString.format(row[x])
                if align == 'L':
                    rowString += f'{row[x]}{returnSpaces(largLenList[x] - len(row[x]))}'
                elif align == 'R':
                    rowString += f'{returnSpaces(largLenList[x] - len(row[x]))}{row[x]}'
                else:
                    spacesString = returnSpaces(largLenList[x] - len(row[x]))
                    #Odd spacing, puts the extra space on the right
                    if len(spacesString) % 2 == 1:
                        midPoint = int((len(spacesString) - 1) / 2)
                        spacesStringLeft = spacesString[:midPoint]
                        spacesStringRight = spacesString[:midPoint+1]
                        rowString += f'{spacesStringLeft}{row[x]}{spacesStringRight}'
                    else:
                        midPoint = int(len(spacesString) / 2)
                        spacesString = spacesString[:midPoint]
                        rowString += f'{spacesString}{row[x]}{spacesString}'
                        
            else:
                if align == 'L':
                    rowString += f'{row[x]}{returnSpaces(largLenList[x] - len(str(row[x])))}'
                elif align == 'R':
                    rowString += f'{returnSpaces(largLenList[x] - len(str(row[x])))}{row[x]}'
                else:
                    spacesString = returnSpaces(largLenList[x] - len(str(row[x])))
                    #Odd spacing, puts the extra space on the right
                    if len(spacesString) % 2:
                        midPoint = int((len(spacesString) - 1) / 2)
                        spacesStringLeft = spacesString[:midPoint]
                        spacesStringRight = spacesString[:midPoint+1]
                        
                        rowString += f'{spacesStringLeft}{row[x]}{spacesStringRight}'
                    else:
                        midPoint = int(len(spacesString) / 2)
                        spacesString = spacesString[:midPoint]
                        
                        rowString += f'{spacesString}{row[x]}{spacesString}'
                
        print(rowString)
        
#Converts datatypes in a list structured in table format to the corrosponding data type
#In dataTypeList. Inputting a dataTypeConstruct object will default the list to that type
#The methodList has the same format, with a list in each cell holding the methodApplier objects to be applied to each object
#Passing in a methodApplier object will default the list to those methods
#Passing None to methodList means no methods will be applied
def convTable(tableList, dataTypeList = dataTypeConstruct(int), methodList=None):
    #Formats the dataTypeList if a default dataType is entered
    if type(dataTypeList) == dataTypeConstruct:
        dataTypeList = [[dataTypeList for cell in row] for row in tableList]
    #Formats the dataTypeList if a standard is passed in representing the rest of the table
    elif type(dataTypeList) == list and len(dataTypeList) <= 2 and len(tableList) != len(dataTypeList):
        #Title row and data row present
        if len(dataTypeList) == 2:
            titleRow = dataTypeList[0]
            dataTypeList = [dataTypeList[1] for x in range(len(tableList)-1)]
            dataTypeList.insert(0, titleRow)
        #Only data row present
        else:
            dataTypeList = [dataTypeList[0] for x in range(len(tableList))]
    
    #Formats the methodList if a default method is entered
    if type(methodList) == methodApplier:
        methodList = [[[methodList] for cell in row] for row in tableList]
    elif type(methodList) == list and len(methodList) <= 2 and len(tableList) != len(methodList):
        #Title row and data row present
        if len(methodList) == 2:
            titleRow = methodList[0]
            methodList = [methodList[1] for x in range(len(tableList)-1)]
            methodList.insert(0, titleRow)
        #Only data row present
        else:
            methodList = [methodList[0] for x in range(len(tableList))]
            
    #Iterate through the table rows
    rowNum = 0
    while rowNum < len(tableList):
        cellNum = 0
        while cellNum < len(tableList[rowNum]):
            
            #Apply before conversion methods
            if methodList != None:
                for method in methodList[rowNum][cellNum]:
                    if method.beforeConv:
                        newVal = method.apply(tableList[rowNum][cellNum])
                        if newVal != None:
                            tableList[rowNum][cellNum] = newVal
                
            try:
                dataType = dataTypeList[rowNum][cellNum]
                tableList[rowNum][cellNum] = dataType.createObject(tableList[rowNum][cellNum])
                
                #Apply after conversion methods
                if methodList != None:
                    for method in methodList[rowNum][cellNum]:
                        if method.beforeConv == False:
                            newVal = method.apply(tableList[rowNum][cellNum])
                            if newVal != None:
                                tableList[rowNum][cellNum] = newVal
            except ValueError:
                pass
            
            cellNum += 1
        rowNum += 1