class solution():
    def majorityElement(self, A, N):
        A.sort()
        if A.count(A[N//2])>N//2:
            return A[N//2]
        return -1
            