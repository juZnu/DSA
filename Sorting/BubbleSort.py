#BUBBLE SORT
#Compares two numbers in the list and then swaps the elements 
#Time Complexity : O(N LogN)
#Space Complexity : O(1)

def BubbleSort(inputList,ascending = True):
    for i in range(len(inputList)):
        for j in range(i, len(inputList)):
            if ascending:
                if inputList[i] > inputList[j]:
                    inputList[i],inputList[j] = inputList[j],inputList[i]
            else:
                if inputList[i] < inputList[j]:
                    inputList[i],inputList[j] = inputList[j],inputList[i]
    return inputList

print(BubbleSort([2,1,8,9,4,6]))