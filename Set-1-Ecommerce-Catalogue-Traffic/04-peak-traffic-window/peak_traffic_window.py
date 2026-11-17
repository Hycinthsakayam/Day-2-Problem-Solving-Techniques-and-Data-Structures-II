"""Task 4 - busiest continuous 3-hour window from requests-per-minute for 24 hours, using a sliding window."""
import math
import random
import time

random.seed(8)
# 1,440 minutes: low at night, a lunch bump and an evening sale peak around 20:00
rpm = [int(400 + 900 * math.exp(-((m - 780) / 90) ** 2) + 2600 * math.exp(-((m - 1200) / 110) ** 2)
           + random.randint(-80, 80)) for m in range(1440)]
K = 180
hhmm = lambda m: f"{m // 60:02d}:{m % 60:02d}"


def busiest_window(values, k):
    window = sum(values[:k])
    best, best_start = window, 0
    for end in range(k, len(values)):
        window += values[end] - values[end - k]         # add the new minute, drop the oldest
        if window > best:
            best, best_start = window, end - k + 1
    return best_start, best


def busiest_brute(values, k):
    return max(((s, sum(values[s:s + k])) for s in range(len(values) - k + 1)), key=lambda x: x[1])


print(f"Minutes recorded: {len(rpm)}   total requests: {sum(rpm):,}")
print("Hourly totals:")
for h in range(0, 24, 4):
    print("  " + "  ".join(f"{hh:02d}h {sum(rpm[hh * 60:(hh + 1) * 60]):>7,}" for hh in range(h, h + 4)))

start = time.perf_counter()
s, total = busiest_window(rpm, K)
t_slide = time.perf_counter() - start
start = time.perf_counter()
s2, total2 = busiest_brute(rpm, K)
t_brute = time.perf_counter() - start

print(f"\nBusiest 3-hour window: {hhmm(s)} - {hhmm(s + K)}  with {total:,} requests "
      f"(average {total / K:,.0f} per minute, peak minute {max(rpm[s:s + K]):,})")
print(f"Sliding window O(n)  : {t_slide * 1000:.3f} ms")
print(f"Brute force O(n*k)   : {t_brute * 1000:.3f} ms   same answer: {(s, total) == (s2, total2)}")
print("\nSize infrastructure for at least the peak-window average with headroom for the peak minute.")
