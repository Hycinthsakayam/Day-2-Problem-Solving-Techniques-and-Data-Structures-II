"""Task 2 - detect duplicate or near-duplicate claims (same policy number and incident date, differing only in case or spacing)."""
import re


def normalise(policy_no):
    return re.sub(r"[\s\-_/]", "", policy_no).upper()


def find_duplicates(claims):
    """claims: list of (claim_id, policy_no, incident_date). Returns list of (original_id, duplicate_id)."""
    seen = {}
    dups = []
    for claim_id, policy, date in claims:
        key = (normalise(policy), date)
        if key in seen:
            dups.append((seen[key], claim_id))
        else:
            seen[key] = claim_id
    return dups


if __name__ == "__main__":
    claims = [
        ("CLM1001", "POL-HLT-2045", "2026-11-02"),
        ("CLM1002", "POL-MOT-7781", "2026-11-03"),
        ("CLM1003", "pol hlt 2045", "2026-11-02"),     # same as CLM1001, different case and spacing
        ("CLM1004", "POL-HLT-2045", "2026-11-09"),     # same policy, different incident -> not a duplicate
        ("CLM1005", "POLMOT7781",   "2026-11-03"),     # same as CLM1002
        ("CLM1006", "POL-HME-1200", "2026-11-05"),
        ("CLM1007", " Pol-Hme-1200 ", "2026-11-05"),   # same as CLM1006
    ]
    print(f"{'Claim':<9}{'Policy as typed':<18}{'Normalised key':<16}Incident")
    for cid, pol, date in claims:
        print(f"{cid:<9}{pol!r:<18}{normalise(pol):<16}{date}")
    print("\nDuplicates found:")
    for orig, dup in find_duplicates(claims):
        print(f"  {dup} duplicates {orig}")
    print("\nThe key is (normalised policy number, incident date) in a dict, so each check is O(1) on average.")
    print("Collisions: Python's dict uses open addressing - if two keys hash to the same slot it probes the")
    print("next slot and compares the full key, so different claims never get mixed up, only checked one extra time.")
