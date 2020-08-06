def compute_income(deposit, interest_rate, amount_months):
    s = deposit * (1 + interest_rate / (12 * 100)) ** amount_months
    return s - deposit


x = float(input())
k = float(input())
n = int(input())
s = compute_income(x, k, n)
print('%4.0f' % s)
