# Computer Science: Big O Notation

**Question:** Why is O(n log n) better than O(n²) for sorting?

---

**Goal:** Understand why algorithms with O(n log n) time complexity outperform those with O(n²) as the amount of data increases.

**Plain Language:**
Imagine you have to organize a deck of cards. If you use a slow method (like O(n²)), every time you add more cards, the time it takes grows massively. If you have 10 cards, it takes 100 steps. If you have 100 cards, it takes 10,000 steps! A faster method (O(n log n)) works much smarter. It divides the deck into smaller piles, sorts them quickly, and puts them back together. As your deck grows, the time it takes grows much slower, saving a huge amount of effort.

**Steps:**
1. **What is 'n'?**
   In Big O notation, 'n' represents the size of the input. For sorting, 'n' is the number of items you need to sort.
2. **Understanding O(n²):**
   Algorithms like Bubble Sort or Insertion Sort compare every item with almost every other item. 
   - Mathematically, if $n = 1000$, the number of operations is roughly $1000 \times 1000 = 1,000,000$.
   - The growth is quadratic; double the input, and the time quadruples.
3. **Understanding O(n log n):**
   Algorithms like Merge Sort or Quick Sort use a "divide and conquer" strategy. They repeatedly split the data in half (which takes $\log_2(n)$ steps) and then merge them by looking at each item 'n' times.
   - If $n = 1000$, $\log_2(1000)$ is roughly 10.
   - The operations are roughly $1000 \times 10 = 10,000$.
4. **The Comparison:**
   For $n = 1000$:
   - O(n²): ~1,000,000 steps.
   - O(n log n): ~10,000 steps.
   The O(n log n) approach is roughly 100 times faster for just a thousand items.

**Check:**
Is $n \log n$ always smaller than $n^2$? Yes, for any $n > 1$, $\log n$ is strictly less than $n$. Therefore, multiplying $n$ by $\log n$ will always yield a smaller result than multiplying $n$ by $n$. 

**Takeaway:**
O(n log n) is better than O(n²) because it scales efficiently. As data sizes grow into the millions or billions, an O(n²) algorithm becomes impractically slow, while an O(n log n) algorithm remains manageable thanks to the power of dividing the problem in half logarithmically.
