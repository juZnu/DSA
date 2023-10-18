#SELECTION SORT
#swap the minimum value into the position then move to the next index
#Time Complexity : O(N^2)
#Space Complexity : O(1)

def SelectionSort(inputList,ascending= True):
    for i in range(len(inputList)):
        mid_index = i
        for j in range(i+1,len(inputList)):
            if ascending and inputList[mid_index] > inputList[j]:
                mid_index = j
            elif (not ascending) and inputList[mid_index] < inputList[j]:
                mid_index = j
        if mid_index != i:
            inputList[i],inputList[mid_index] = inputList[mid_index],inputList[i]
    return inputList

print(SelectionSort([2,1,5,4,8,9,6,3],ascending= False))