# Day 2 – Problem Solving Techniques and Data Structures II

This repository contains my solutions for the Day 2 Python assignment on trees, hashing, graphs and the two-pointer and sliding-window patterns. Each question is in its own folder.

The assignment has three sets, with five questions in each set.

## What I'm working on

- Building binary search trees and printing the traversals.
- Writing a hash table with chaining and comparing it with dict.
- Modelling graphs and using BFS and DFS (shortest path, topological order, loop detection).
- Solving window problems with the sliding-window pattern.
- Using two pointers on sorted data.
- Writing unit tests for empty input and duplicates (Set 2).

## Assignment sets

### Set 1 – E-Commerce Catalogue and Traffic Analysis
This set covers a BST for product categories, a hash table for SKU look-up, a deployment-order graph for microservices, the busiest traffic window and gift-card pairs.

[Open Set 1](./Set-1-Ecommerce-Catalogue-Traffic/)

### Set 2 – Insurance Claims Processing
This set covers a BST of claim IDs, duplicate-claim detection with hashing, the approval-stage graph, claim-spike windows and merging two offices' sorted claim lists. Each question has unit tests.

[Open Set 2](./Set-2-Insurance-Claims/)

### Set 3 – Logistics Network and Delivery Windows
This set covers hub codes in a BST, double-scan checks with a hash map, fewest-hop routes and reachable hubs, the best 4-hour window and route palindromes.

[Open Set 3](./Set-3-Logistics-Network/)

## How the folders are organised

Each question has its own folder. Inside, you can find:

- A Python file named after the question, such as `category_bst.py` or `route_palindrome.py`.
- `output.txt`, which shows a sample run of the program.
- `flowchart.svg`, which shows the steps followed in the solution.

Each set also has a `SET-NOTES.md` file with the complexity and data-structure notes.

In Set 2 each folder also has a `test_*.py` file; its result is at the end of `output.txt`.

## Running

Open the folder for the question, open a terminal there and run its Python file, for example:

```bash
python category_bst.py
```

The programs only use Python's standard library, so no extra packages are needed. Timings in `output.txt` will change
from machine to machine.
