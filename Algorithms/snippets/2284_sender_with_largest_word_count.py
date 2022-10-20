from collections import defaultdict


def largest_word_count(messages, senders):
    wrd_cnt = defaultdict(int)
    for message, person in zip(messages, senders):
        wrd_cnt[person] += len(message.split())

    maxi = max(wrd_cnt.values())

    out = sorted([name for name, words in wrd_cnt.items() if words == maxi], reverse=True)
    return out[0]


print(largest_word_count(messages=["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"],
                         senders=["Alice", "userTwo", "userThree", "Alice"]))
