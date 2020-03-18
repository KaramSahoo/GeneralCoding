def circularBinarySearch(arr, n, key):
	pivot = findPivot(arr, 0, n-1)

	if pivot == -1:
		return binarySearch(arr, 0, n-1, key)

	if arr[pivot] == key:
		return pivot
	if arr[0] <= key:
		return binarySearch(arr, 0, pivot-1, key)
	return binarySearch(arr, pivot+1, n-1, key)

def findPivot(arr, low, high):
	if high < low:
		return -1
	if high == low:
		return low

	mid = int((low+high)/2)
	if mid < high and arr[mid] > arr[mid+1]:
		return mid
	if mid > low and arr[mid] < arr[mid-1]:
		return mid-1
	if arr[low] > arr[mid]:
		return findPivot(arr, low, mid-1)
	return findPivot(arr, mid+1, high)

def binarySearch(arr, low, high, key):
	if high < low:
		return -1

	mid = int((low+high)/2)
	if arr[mid] == key:
		return mid
	if key > arr[mid]:
		return binarySearch(arr, mid+1, high, key)
	return binarySearch(arr, low, mid-1, key)

arr = [40,50,60,70,80,90,0,10,20,30]
key = int(input("Enter key : "))
print("Index of the key is : ", circularBinarySearch(arr, len(arr), key))