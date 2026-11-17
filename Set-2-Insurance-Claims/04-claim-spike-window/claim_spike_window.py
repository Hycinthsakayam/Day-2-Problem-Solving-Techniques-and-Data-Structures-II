"""Task 4 - longest run of consecutive days on which claims exceeded 100, using a sliding window."""


def longest_run_above(counts, limit=100):
    """returns (length, start_index) of the longest window where every day is above the limit"""
    best_len, best_start = 0, -1
    left = 0
    for right, value in enumerate(counts):
        if value <= limit:
            left = right + 1                 # window cannot contain this day, restart after it
        elif right - left + 1 > best_len:
            best_len, best_start = right - left + 1, left
    return best_len, best_start


if __name__ == "__main__":
    # daily claims in November 2026; a cyclone hits the region on 10 Nov
    daily = [42, 55, 61, 48, 120, 104, 58, 66, 70, 230, 410, 388, 302, 245, 180, 150, 98, 131, 112, 75,
             64, 101, 140, 99, 60, 58, 47, 52, 49, 44]
    print("Claims per day (1-30 Nov):")
    for week in range(0, 30, 10):
        print("  " + "  ".join(f"{d + 1:>2}:{c:>3}" for d, c in enumerate(daily[week:week + 10], start=week)))
    length, start = longest_run_above(daily)
    print(f"\nLongest run above 100: {length} days, {start + 1} Nov to {start + length} Nov")
    print(f"Claims in that run: {daily[start:start + length]}  (total {sum(daily[start:start + length]):,})")
    print("\nThe window grows while days stay above 100 and restarts after a quiet day.")
    print("Each day is visited once -> O(n) time, O(1) space.")
