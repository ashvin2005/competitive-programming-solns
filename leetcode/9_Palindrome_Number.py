"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
- -2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        if y[::]==y[::-1]:
            return True
        else :
            return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    x1 = 121
    print(f"Input: x = {x1}")
    print(f"Output: {solution.isPalindrome(x1)}")
    print(f"Expected: True\n")
    
    # Test case 2
    x2 = -121
    print(f"Input: x = {x2}")
    print(f"Output: {solution.isPalindrome(x2)}")
    print(f"Expected: False\n")
    
    # Test case 3
    x3 = 10
    print(f"Input: x = {x3}")
    print(f"Output: {solution.isPalindrome(x3)}")
    print(f"Expected: False\n")
    
    # Additional test case
    x4 = 0
    print(f"Input: x = {x4}")
    print(f"Output: {solution.isPalindrome(x4)}")
    print(f"Expected: True")
