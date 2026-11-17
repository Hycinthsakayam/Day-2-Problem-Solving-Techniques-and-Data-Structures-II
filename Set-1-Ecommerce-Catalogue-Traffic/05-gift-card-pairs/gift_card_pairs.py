"""Task 5 - all pairs of order values that add up to a gift-card value, using two pointers on a sorted list."""


def pairs_with_sum(values, target):
    i, j = 0, len(values) - 1
    pairs = []
    while i < j:
        s = values[i] + values[j]
        if s == target:
            pairs.append((values[i], values[j]))
            left, right = values[i], values[j]
            while i < j and values[i] == left:     # skip repeated values so each pair is listed once
                i += 1
            while i < j and values[j] == right:
                j -= 1
        elif s < target:
            i += 1
        else:
            j -= 1
    return pairs


orders = sorted([199, 249, 299, 349, 499, 499, 599, 650, 750, 899, 999, 1001, 1250, 1350, 1499, 1501, 1751, 1801])
print("Sorted order values:", orders)
for card in [2000, 1000, 3000, 50]:
    found = pairs_with_sum(orders, card)
    print(f"\nGift card Rs.{card}: {len(found)} pair(s)")
    for a, b in found:
        print(f"  {a} + {b} = {card}")

print("\nTime O(n) after sorting (each step moves one pointer), space O(1).")
print("Checking every pair would be O(n^2).")
