#BUBBLE SORT
#Compares adjacent two numbers in the list and then swaps the elements 
#Time Complexity : O(N^2)
#Space Complexity : O(1)

def BubbleSort(inputList,ascending = True):

    for i in range(len(inputList)):
        swapped = False
        for j in range(i, len(inputList)-1):
            if ascending:
                if inputList[j] > inputList[j+1]:
                    inputList[j],inputList[j+1] = inputList[j+1],inputList[j]
                    swapped = True          
            else:
                if inputList[j] < inputList[j+1]:
                    inputList[j],inputList[j+1] = inputList[j+1],inputList[j]
        if not swapped:
                break
            
    return inputList

