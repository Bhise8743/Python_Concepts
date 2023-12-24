
"""
Given an integer array, find k'th the smallest element in the array where k is a positive integer less than or equal to the
length of array.

Input : [7, 4, 6, 3, 9, 1], k = 3
Output: 4
Explanation: The 3rd smallest array element is 4

Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
Output: 4
Explanation: The 5th smallest array element is 4

"""



if __name__ == '__main__':
    l = [7, 4, 6, 3, 9, 1]
    k = 3
    l.sort(reverse=False)
    print(l[k - 1])