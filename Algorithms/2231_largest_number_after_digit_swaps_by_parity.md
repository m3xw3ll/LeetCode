# [Largest Number After Digit Swaps by Parity](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/)

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits
or both even digits).

Return the largest possible value of num after any number of swaps.

Example 1:
```
Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
```
Example 2:
```
Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
```
Solution
```python
class Solution:
    def largestInteger(self, num: int) -> int:
        evens = list()
        odds = list()
        out = 0
        a = [int(x) for x in str(num)]

        for i in a:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        evens = sorted(evens)
        odds = sorted(odds)

        for i in range(len(a)):
            if a[i] % 2 == 0:
                out = out * 10 + evens.pop()
            else:
                out = out * 10 + odds.pop()
        return out
```