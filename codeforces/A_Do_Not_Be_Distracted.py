"""
A. Do Not Be Distracted! - Codeforces

Polycarp has 26 tasks. Each task is designated by a capital letter of the English alphabet.

The teacher gave Polycarp a string s of length n, consisting of uppercase English letters, 
which should be read as follows:
- if s[i] = s[i-1] (i > 1), then the i-th task is a continuation of the (i-1)-th task;
- if s[i] ≠ s[i-1] (i > 1), then the i-th task is not a continuation of the (i-1)-th task.

It is guaranteed that the first task is not a continuation of any other task.

Before Polycarp starts doing the tasks, he can rearrange the string s as he wishes. 
He wants to rearrange it so that he can do all the tasks, and each task must be done 
in one continuous segment (i.e., he cannot start doing task A, then do task B, then 
return to task A).

Your task is to determine whether Polycarp can rearrange the string s so that he can 
complete all tasks correctly.

Input:
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.
Each test case consists of two lines:
- The first line contains a single integer n (1 ≤ n ≤ 50) — the length of the string s.
- The second line contains the string s of length n, consisting of uppercase English letters.

Output:
For each test case, print "YES" if Polycarp can rearrange the string to complete all tasks, 
or "NO" otherwise.

Example:
Input:
4
3
ABA
4
ABAB
5
ABCAB
6
AAABBB

Output:
NO
NO
NO
YES

Explanation:
- ABA: Task A appears twice with task B in between, so it's impossible to do A continuously.
- ABAB: Both A and B appear twice with other tasks in between.
- ABCAB: Tasks A and B appear multiple times with other tasks in between.
- AAABBB: Can be rearranged as AAABBB (already valid) where each task appears continuously.
"""

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        l = []
        for i in range(1, n):
            if s[i] != s[i-1]:
                l.append(s[i-1])
            if s[i] in l:
                print("NO")
                break
        else:
            print("YES")

if __name__ == "__main__":
    solve()

# Test cases (uncomment to test locally)
"""
Test Case 1:
Input: 
4
3
ABA
4
ABAB
5
ABCAB
6
AAABBB

Expected Output:
NO
NO
NO
YES
"""
