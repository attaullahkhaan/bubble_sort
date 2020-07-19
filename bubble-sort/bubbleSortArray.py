# Bubble Sort by Array
arr = [27, 33, 51, 66, 23, 13, 57, 85]
n = len (arr)-2
for k in range (n):
    ptr = 0
    while ptr <= n - k:
        if arr [ptr] > arr [ptr + 1]:
            arr[ptr],arr[ptr+1]= arr[ptr + 1],arr[ptr]
        ptr += 1
print (arr) 