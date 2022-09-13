# [Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:

![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)
```
Input: text = "nlaebolko"
Output: 1
```
Example 2:

![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)
```
Input: text = "loonbalxballpoon"
Output: 2
```
Example 3:
```
Input: text = "leetcode"
Output: 0
```
Solution
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chardict = {'b': 0, 'a': 0, 'l': 0, 'o':0, 'n':0}
        for char in text:
            if char in chardict:
                chardict[char] += 1
        chardict['l'] = chardict['l'] // 2
        chardict['o'] = chardict['o'] // 2

        return min(chardict.values())
```

