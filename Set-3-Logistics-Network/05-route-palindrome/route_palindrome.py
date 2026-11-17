"""Task 5 - check with two pointers whether a delivery route is a palindrome of hub codes, ignoring case and separators."""
import re


def is_route_palindrome(route):
    """compares hub codes from both ends: 'MAA-BLR-maa' -> True"""
    hubs = [h.upper() for h in re.split(r"[^A-Za-z0-9]+", route) if h]
    i, j = 0, len(hubs) - 1
    while i < j:
        if hubs[i] != hubs[j]:
            return False, hubs, (i, j)
        i += 1
        j -= 1
    return True, hubs, None


def is_char_palindrome(text):
    """character-level check that skips separators without building a new string"""
    i, j = 0, len(text) - 1
    while i < j:
        if not text[i].isalnum():
            i += 1
        elif not text[j].isalnum():
            j -= 1
        elif text[i].lower() != text[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True


routes = ["MAA-BLR-HYD-BLR-MAA", "del > jai > Del", "BOM/PNQ/goi/pnq/bom", "MAA-BLR-HYD-MAA",
          "nag", "", "MAA - AAM"]
for r in routes:
    ok, hubs, where = is_route_palindrome(r)
    detail = "" if ok else f"  (mismatch {hubs[where[0]]} vs {hubs[where[1]]})"
    print(f"{r!r:<24} hubs {hubs!s:<38} hub palindrome: {str(ok):<5} char palindrome: {is_char_palindrome(r)}{detail}")

print("\nTwo pointers move from both ends towards the middle: O(n) time, O(1) extra space for the")
print("character check. 'MAA - AAM' is a palindrome by letters but not by hub codes.")
