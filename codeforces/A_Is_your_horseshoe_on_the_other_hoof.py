"""
A. Is your horseshoe on the other hoof? - Codeforces

Valera the Horse is going to the party. He has been following the fashion trends lately, 
so he is going to wear all his four horseshoes to the party. Valera has four horseshoes, 
and each horseshoe has a color (which is a positive integer).

Valera is wondering how many horseshoes he needs to buy additionally to ensure that all 
four horseshoes have different colors. You need to find the answer to his question.

Input:
The first line contains four space-separated integers s1, s2, s3, s4 (1 ≤ si ≤ 10^9) — 
the colors of Valera's horseshoes.

Output:
Print the number of horseshoes Valera needs to buy.

Example 1:
Input: 1 7 3 3
Output: 1
Explanation: Valera has horseshoes with colors 1, 7, 3, 3. Since two horseshoes have the same color (3), 
he needs to buy 1 additional horseshoe to have 4 different colors.

Example 2:
Input: 1 2 3 4
Output: 0
Explanation: All horseshoes already have different colors.
"""

def solve():
    s1, s2, s3, s4 = map(int, input().split())
    number_to_buy = 4 - len(set([s1, s2, s3, s4]))
    print(number_to_buy)

if __name__ == "__main__":
    solve()

# Test cases (uncomment to test locally)
"""
Test Case 1:
Input: 1 7 3 3
Expected Output: 1

Test Case 2:
Input: 1 2 3 4
Expected Output: 0

Test Case 3:
Input: 1 1 1 1
Expected Output: 3
"""