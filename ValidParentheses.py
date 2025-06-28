class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


# Valid Parentheses Problem: 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Solution:
#   Initialization:
#     i. Initialize an empty stack to store opening brackets.
#    ii. Create a dictionary (closeToOpen) to map each closing bracket to its correct opening bracket:")": "(", "]": "[", "}": "{"


# Working:
#   i. Iterate through each character in the string:
  
#   ii. If the character is a closing bracket:
#           a. Check if the stack is not empty and the top of the stack matches the corresponding opening bracket from the dictionary.
#           b. If it matches, pop the opening bracket from the stack.
#   iii. If it doesn't match or the stack is empty, return False (invalid).
  
#   iv. If the character is an opening bracket, push it onto the stack.
  
#   v. After the loop, check if the stack is empty:
#           a. If yes, return True (all brackets matched correctly).
#           b. If not, return False (some unmatched opening brackets remain)

