"""Task 4 - the 4-hour window with the highest average parcel count, using a sliding window."""

hourly = [120, 95, 80, 70, 65, 90, 210, 480, 760, 820, 790, 640, 560, 600, 710, 880, 940, 910, 720, 500, 380, 300, 220, 160]
K = 4


def best_window(counts, k):
    if k <= 0 or len(counts) < k:
        return None
    total = sum(counts[:k])
    best_total, best_start = total, 0
    for i in range(k, len(counts)):
        total += counts[i] - counts[i - k]
        if total > best_total:
            best_total, best_start = total, i - k + 1
    return best_start, best_total / k


print("Parcels per hour:")
for h in range(0, 24, 6):
    print("  " + "  ".join(f"{hh:02d}:00 {hourly[hh]:>4}" for hh in range(h, h + 6)))

start, avg = best_window(hourly, K)
print(f"\nBest 4-hour window: {start:02d}:00 - {start + K:02d}:00, average {avg:.1f} parcels/hour "
      f"({hourly[start:start + K]})")
print("Second peak (morning) for comparison:", best_window(hourly[:12], K))
print("\nThe window total is updated by adding the new hour and removing the oldest: O(n) time, O(1) space,")
print("instead of re-adding 4 values for every start hour.")
