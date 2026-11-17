"""Task 2 - hash map of parcel tracking numbers and a check for parcels scanned twice at the same hub."""
from collections import defaultdict

scans = [
    ("TRK7001", "MAA", "08:02"), ("TRK7002", "MAA", "08:05"), ("TRK7001", "BLR", "13:40"),
    ("TRK7003", "BOM", "09:10"), ("TRK7002", "MAA", "08:31"),       # TRK7002 scanned twice at MAA
    ("TRK7004", "DEL", "10:00"), ("TRK7003", "PNQ", "15:20"), ("TRK7005", "HYD", "11:11"),
    ("TRK7004", "DEL", "10:02"), ("TRK7004", "DEL", "10:09"),       # three scans at DEL
    ("TRK7001", "BLR", "13:45"), ("TRK7006", "CCU", "12:30"),
]

tracking = defaultdict(list)          # tracking number -> list of (hub, time)
double = defaultdict(list)            # (tracking, hub) -> times, only when > 1
seen_at_hub = {}

for trk, hub, time in scans:
    tracking[trk].append((hub, time))
    key = (trk, hub)
    if key in seen_at_hub:
        if not double[key]:
            double[key].append(seen_at_hub[key])
        double[key].append(time)
    else:
        seen_at_hub[key] = time

print("Tracking look-up:")
for trk in ["TRK7001", "TRK7003", "TRK9999"]:
    print(f"  {trk}: {tracking.get(trk, 'not found')}")

print("\nParcels scanned more than once at the same hub:")
for (trk, hub), times in double.items():
    print(f"  {trk} at {hub}: {len(times)} scans at {', '.join(times)}")

print("\nA dict gives O(1) average look-up by tracking number. The (tracking, hub) key finds repeat scans")
print("in a single pass: O(n) time and O(n) space for n scans.")
