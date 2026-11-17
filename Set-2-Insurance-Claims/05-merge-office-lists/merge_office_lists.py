"""Task 5 - merge two sorted claim lists from two regional offices with two pointers (no extra sorting)."""


def merge_sorted(a, b, key=lambda x: x):
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):        # '<=' keeps office A first on ties (stable)
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


if __name__ == "__main__":
    chennai = [("CLM1002", "2026-11-01"), ("CLM1007", "2026-11-03"), ("CLM1011", "2026-11-03"),
               ("CLM1020", "2026-11-08"), ("CLM1031", "2026-11-12")]
    bengaluru = [("CLM2001", "2026-11-02"), ("CLM2004", "2026-11-03"), ("CLM2010", "2026-11-09"),
                 ("CLM2015", "2026-11-10"), ("CLM2022", "2026-11-14"), ("CLM2030", "2026-11-15")]
    print("Chennai office  :", chennai)
    print("Bengaluru office:", bengaluru)
    merged = merge_sorted(chennai, bengaluru, key=lambda c: c[1])
    print("\nMerged by claim date:")
    for cid, date in merged:
        print(f"  {date}  {cid}")
    print(f"\n{len(chennai)} + {len(bengaluru)} = {len(merged)} claims, merged in one pass: O(n + m) time.")
    print("Calling sorted() on the joined list would be O((n + m) log(n + m)).")
