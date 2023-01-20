# [Replace Words](https://leetcode.com/problems/replace-words/description/)

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's 
call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a 
new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the 
successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it 
with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:
```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```
Example 2:
```
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
```
Solution
```python
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        dic = set(dictionary)
        out = list()

        for w in words:
            root = False
            for i in range(len(w)):
                if w[:i+1] in dic:
                    root = True
                    out.append(w[:i+1])
                    break
            if not root:
                out.append(w)
        return ' '.join(out)
```