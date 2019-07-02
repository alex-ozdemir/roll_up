import math

def roll_up_cost(h, n, t):
    return (7 * h + 19176 + (2 * h + 768) * math.ceil(math.log2(n))) * t

def merkle_pct(h, n, t):
    return (2 * h + 768) * math.ceil(math.log2(n)) * t / roll_up_cost(h, n, t) * 100

print(f'depth\tmax entries\tconstraints\t% merkle')
print(f'-----\t-----------\t-----------\t--------')
for i in range(4,21,4):
    print(f'{i}\t{2**i:,}\t{roll_up_cost(54560, 2**i, 1):,}\t{merkle_pct(54560, 2**i, 1):.0f}')
