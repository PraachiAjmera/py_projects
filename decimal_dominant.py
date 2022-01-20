def findMajority(arr, n):

    maxCount = 0
    index = -1
    for i in range(n):

        count = 0
        for j in range(n):

            if(arr[i] == arr[j]):
                count += 1
        if(count > maxCount):

            maxCount = count
            index = i

    if (maxCount > n//10):
        print("The Decimal Dominant is:", arr[index])

    else:
        print("No Majority Element")

if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1, 2, 1, 9]
    n = len(arr)

    findMajority(arr, n)
