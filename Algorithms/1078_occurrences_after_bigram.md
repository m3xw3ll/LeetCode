# [Occurrences After Bigram](https://leetcode.com/problems/occurrences-after-bigram/)

Given two strings first and second, consider occurrences in some text of the form "first second third", where second 
comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

Example 1:
```
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
```
Example 2:
```
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
```
Solution
```python
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        out = []
        text = text.split()
        for i in range(len(text) - 2):
            if text[i] == first and text[i+1] == second:
                out.append(text[i+2])
        return out
```
