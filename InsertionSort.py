def Sort(A):
		for i in range(1, len(A)):
			val = A[i]
			j = i
			while A[j-1] > val and j >= 1:
				A[j] = A[j-1]
				j = j-1
			A[j] = val
		return A

A = [6, 8, 1, 7, 10, 9, 5, 3, 4]
print("Before sorting: ", A)
print("After sorting: ", Sort(A)) 