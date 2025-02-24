"""
Ricardo Alfredo Calvo Perez
23/02/2025
Problem: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""
import os
os.system('cls')


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def linked_list_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def list_to_linked_list(self, lst):

        node = ListNode()
        current = node

        for val in lst:
            current.next = ListNode(val)
            current = current.next

        return node.next

    def addTwoNumbers(self, n1, n2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Reverse the lists to get the numbers in the correct order
        l1 = self.linked_list_to_list(n1)[::-1]
        l2 = self.linked_list_to_list(n2)[::-1]

        # Convert the lists to strings and then to integers
        # For every number in the list, convert it to a string 'map(str, l{n})'
        # Join it to the rest of the numbers in the list "''.join(...)"
        # Then convert the resulting string to an integer 'int(...)'

        num1 = int(''.join(map(str, l1)))
        num2 = int(''.join(map(str, l2)))

        # Add the two numbers
        sum = num1 + num2

        # Convert the sum to a list
        # For every digit in the sum, convert it to a string 'map(str, sum)'
        # Then convert the resulting string to an integer 'int(...)'

        return self.list_to_linked_list(list(map(int, str(sum)))[::-1])

# Test cases


testCases = [
    # l1, l2, expected
    [[2, 4, 9], [5, 6, 4, 9], [7, 0, 4, 0, 1]],
    [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
    [[2, 4, 3, 9], [5, 6, 4], [7, 0, 8, 9]],
    [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
    [[9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
    [[0], [0], [0]],
    [[1], [1], [2]],
    [[9], [9], [8, 1]],
    [[9], [1], [0, 1]],
    [[1], [9], [0, 1]],
    [[1], [9, 9, 9, 9], [0, 0, 0, 0, 1]],
    [[9, 9, 9, 9], [1], [0, 0, 0, 0, 1]],
    [[9, 9, 9, 9], [9], [8, 0, 0, 0, 1]],
    [[9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 1]],
    [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9], [8, 9, 9, 9, 9, 9, 9, 1]],
]

solution = Solution()


for i, testCase in enumerate(testCases):
    l1, l2, expected = testCase
    l1_linked = solution.list_to_linked_list(l1)
    l2_linked = solution.list_to_linked_list(l2)
    expected_linked = solution.list_to_linked_list(expected)

    result = solution.addTwoNumbers(l1_linked, l2_linked)
    result_list = solution.linked_list_to_list(result)
    expected_list = solution.linked_list_to_list(expected_linked)

    print(f"Test {i+1}: {'✅ Passed' if result_list == expected_list else '❌ Failed'} - Output: {result_list}, Expected: {expected_list}")
