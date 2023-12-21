"""

@Author: Omkar Bhise

@Date: 2023-12-02 11:30:30

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-02 5:30:00

@Title :  two number sum equal to the target or not

"""
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""


def check_target():
    """
           Description:
               it checks the sum of two numbers equal to the target or not
               it takes the O(n2) time complexity
           Parameter:
               None

           Return: None
           """
    nums = [2, 9, 11, 15]
    target = 9

    for i in range(len(nums)):
        for j in range(i + 1, len(nums), 1):
            if nums[i] + nums[j] == target:
                print(i, " ", j)
                return
    print("Target not found in the list ")


def check_target_1():
    """
    Description:
        it checks the sum of two numbers is equal to the target or not
    Parameter:
        None

    Return: None
    """
    num = [2, 7, 11, 15]
    target = 9
    num.sort()
    i = 0
    j = len(num) - 1

    flag = 1
    while i < j:

        if (num[i] + num[j]) == target:
            print(i, " ", j)
            flag = 0
            break
        elif num[i] + num[j] < target:
            i += 1
        else:
            j -= 1

    if flag == 1:
        print("Target is not percent inside the list ")


if __name__ == '__main__':
    check_target()
    check_target_1()
