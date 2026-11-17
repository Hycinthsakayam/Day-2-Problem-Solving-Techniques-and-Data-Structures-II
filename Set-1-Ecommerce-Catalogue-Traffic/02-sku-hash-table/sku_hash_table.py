"""Task 2 - hash table with chaining for SKU look-up, one collision, and comparison with the built-in dict."""
import random
import time


class HashTable:
    def __init__(self, size=1009):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        h = 0
        for ch in key:
            h = (h * 31 + ord(ch)) % self.size       # polynomial rolling hash
        return h

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        for k, v in self.buckets[self._hash(key)]:
            if k == key:
                return v
        return None


# --- collision demo on a tiny table ---
small = HashTable(size=7)
skus = {"SKU-1001": "Bluetooth Speaker", "SKU-1002": "USB-C Charger", "SKU-1003": "Wireless Mouse",
        "SKU-1004": "Basmati Rice", "SKU-1005": "Cold Pressed Oil", "SKU-1006": "Mixer Grinder",
        "SKU-1007": "Non-stick Tawa", "SKU-1008": "Running Shoes"}   # 8 keys, 7 buckets -> at least one collision
print("Small table with 7 buckets")
for sku, name in skus.items():
    small.put(sku, name)
    print(f"  put {sku} ({name:<17}) -> bucket {small._hash(sku)}")
collided = None
for i, b in enumerate(small.buckets):
    if len(b) > 1:
        print(f"Collision: bucket {i} holds {[k for k, _ in b]} as a chain")
        collided = collided or b[-1][0]
print(f"get {collided} -> {small.get(collided)} (found by walking the chain)")

# --- 100,000 SKUs: own table vs dict ---
N = 100_000
random.seed(4)
all_skus = [f"SKU-{i:06d}" for i in range(N)]
own, builtin = HashTable(size=131_071), {}
for i, sku in enumerate(all_skus):
    own.put(sku, i)
    builtin[sku] = i
queries = random.sample(all_skus, N)

start = time.perf_counter()
ok1 = sum(own.get(q) is not None for q in queries)
t_own = time.perf_counter() - start
start = time.perf_counter()
ok2 = sum(builtin.get(q) is not None for q in queries)
t_dict = time.perf_counter() - start

longest = max(len(b) for b in own.buckets)
print(f"\n{N:,} SKU look-ups")
print(f"  own chained hash table: {t_own:.4f} s  (found {ok1:,}, longest chain {longest})")
print(f"  built-in dict         : {t_dict:.4f} s  (found {ok2:,})")
print(f"  dict is about {t_own / t_dict:.0f}x faster (C implementation, open addressing)")
print("Both are O(1) on average; chaining degrades to O(n) only if many keys hash to one bucket.")
