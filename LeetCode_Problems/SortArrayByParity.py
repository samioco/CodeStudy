
#SortArrayByParity.py

#1. sort arrow in odds and evens
#[3,1,2,4] -> [2,4,3,1]
#evens first

class Solution(object):
    def sortArrayByParity_lambdaComparator(self, A):
        A.sort(key = lambda x: x%2)
        return A

    def sortArrayByParity_TwoPass(self, A):
        return ([x for x in A if x%2==0] + [x for x in A if x%2==1])

    def sortArrayByParity_InPlace(self, A):
        """
        quicksort: using i and j
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A

mylist=[3,1,2,4]
print("""
Sort Array By Parity
Input: """, mylist,"\n")

sorted_list = Solution()

sorted_list.sortArrayByParity_lambdaComparator(mylist)
print("Output using sortArrayByParity_lambdaComparator: \nTime: O(N log N)\n",mylist,"\n")

sorted_list.sortArrayByParity_TwoPass(mylist)
print("Output using ([x for x in A if x%2==0] + [x for x in A if x%2==1]): \nTime: O(N)\n",mylist,"\n")

sorted_list.sortArrayByParity_InPlace(mylist)
print("Output usingsortArrayByParity_InPlace: \nTime: O(N) normally. Quicksort: O (N log N)\n",mylist,"\n")