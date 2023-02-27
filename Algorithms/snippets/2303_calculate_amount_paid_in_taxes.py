def calculate_tax(brackets, income):
    out = 0
    prev = 0
    for up, pct in brackets:
        up = min(up, income)
        out += (up - prev) * pct / 100
        prev = up
    return out


print(calculate_tax(brackets=[[3, 50], [7, 10], [12, 25]], income=10))
