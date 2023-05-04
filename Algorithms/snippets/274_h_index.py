import heapq


def h_index(citations):
    neg_citations = [-c for c in citations]
    heapq.heapify(neg_citations)

    out = 0
    tmp = 1
    while tmp <= len(citations):
        v = heapq.heappop(neg_citations)
        if -v < tmp:
            break
        else:
            out = tmp
        tmp += 1
    return out


print(h_index([11, 15]))
