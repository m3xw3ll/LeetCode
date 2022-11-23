# [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

- For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more 
than once in a DNA molecule. You may return the answer in any order.

Example 1:
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
```
Example 2:
```
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
```
Solution
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        out = set()
        for i in range(0, len(s) - 9):
            if s[i:i+10] in seen:
                out.add(s[i:i+10])
            seen.add(s[i:i+10])
        return list(out)
```
