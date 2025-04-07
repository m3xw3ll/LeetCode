def check_two_chessboards(coordinate1, coordinate2):
    c1_sum = int(ord(coordinate1[0].lower()) - ord('a') + 1) + int(coordinate1[1])
    c2_sum = int(ord(coordinate2[0].lower()) - ord('a') + 1) + int(coordinate2[1])
    return c1_sum % 2 == c2_sum % 2




print(check_two_chessboards(coordinate1 = "a1", coordinate2 = "c3"))