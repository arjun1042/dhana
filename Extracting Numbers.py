class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        
        num = 0  # Initialize the current number
        total_sum = 0  # Initialize the sum of numbers
        
        for char in A:
            if char.isdigit():  # If the character is a digit, add it to the current number
                num = num * 10 + int(char)
            else:
                total_sum += num  # If a non-digit character is encountered, add the current number to the total sum
                num = 0  # Reset the current number
        
        total_sum += num  # Add the last number
        
        return total_sum

# Test cases
solution = Solution()
print(solution.solve("a12b34c"))  # Output: 46
print(solution.solve("123"))





"""Problem Description
 
 

Given a string A. The string contains alphanumeric characters.
Find the sum of all numbers present in it.

Note: All the numbers will fit in a 32-bit signed integer.


Problem Constraints
1 <= |A| <= 105


Input Format
The first and only argument is a string A.


Output Format
Return an integer.


Example Input
Input 1:
A = "a12b34c"
Input 2:

A = "123"


Example Output
Output 1:

46
Output 2:

123


Example Explanation
Explanation 1:
The numbers are 12, 34.
12 + 34 = 46
Explanation 2:

The only number is 123."""
