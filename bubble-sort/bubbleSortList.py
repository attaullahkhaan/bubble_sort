# Bubble Sort by List
def bubbleSort (myList):
    for i in range (0,len(myList) - 1):
        for j in range (0, len(myList) - 1 -i):
            if myList [j] > myList[j + 1]:
                myList [j] , myList[j +1] = myList [j +1] , myList[j]
    return myList
# theList = ['b','d','f','c','a','e','h','g']
theList = [2,1,4,3,5,6,8,7,10,9]
print (bubbleSort(theList))