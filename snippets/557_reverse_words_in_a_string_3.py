def reverse_words(s):
    return ' '.join([i[::-1] for i in s.split(' ')])


print(reverse_words("Let's take LeetCode contest"))