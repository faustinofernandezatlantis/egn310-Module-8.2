
```
# High-Performance Search Autocomplete & Recent Queries Engine

A real-time search auto-completion and recent search history engine engineered strictly using custom data structures without relying on high-level collection libraries.

## Core Data Structures & Complexity

### 1. Trie (Prefix Tree) for Autocomplete
- **Search & Insertion Time Complexity:** $O(K)$, where $K$ is the length of the prefix query string, making lookup performance completely independent of the total dataset size $N$.
- **Space Complexity:** $O(\Sigma \cdot N \cdot K)$, optimizing memory overhead through prefix sharing across stored terms.

### 2. LRU Cache (Doubly Linked List + Hash Map) for Recent History
- **Access, Insertion & Eviction Time Complexity:** Strict $O(1)$ constant time for updating and retrieving the user's $K$ most recent search queries.

## Structure Selection Justification

- **Why Trie over Binary Search Tree (BST)?**
  Searching for prefix matches in a standard Binary Search Tree requires $O(K \log N)$ comparison overhead and subtree traversals. A Trie navigates directly to the node corresponding to prefix `str` in $O(K)$ steps and inspects only valid descendants, delivering sub-millisecond lookup latency.
  
- **Why Doubly Linked List for LRU Cache over Dynamic Array?**
  Maintaining an LRU history buffer using a dynamic array requires $O(N)$ element shifting every time the least recently used query is evicted or moved to the front. A Doubly Linked List paired with a Hash Map guarantees $O(1)$ node removal and head insertion without array re-allocation.

## Setup & Execution Instructions

### Option 1: Live Demo on Streamlit Community Cloud
Access the deployed web application directly in your browser without any local installation:
🔗 **Live Application Link:** [INSERT YOUR STREAMLIT COMMUNITY CLOUD LINK HERE]

---

### Option 2: Running Locally

1. **Clone Repository:**
   ```
   git clone [https://github.com/faustinofernandezatlantis/egn310-Capstone.git](https://github.com/faustinofernandezatlantis/egn310-Capstone.git)
   cd egn310-Capstone

```

2. **Install Dependencies:**
```
pip install -r requirements.txt

```


3. **Run Application:**
```
streamlit run app.py

```



---

## How to Deploy to Streamlit Community Cloud (Step-by-Step)

1. Push all your project files (`app.py`, `engine.py`, and `requirements.txt`) to your public GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) using your GitHub account.
3. Click the **"New app"** button.
4. Select your repository (`egn310-Capstone`), branch (`main`), and set the Main file path to `app.py`.
5. Click **"Deploy!"**. Streamlit will build and host your web application automatically, generating a public URL you can share.

```

## Course Progression Summary (Modules 4–8)

* **Module 4:** Initial project proposal and Stack/Queue syntax validation engine.
* **Module 5:** Recursion hand-tracing and Timsort vs Quicksort/Merge Sort benchmark suite.
* **Module 6:** Binary Search Tree implementation with Streamlit web directory interface.
* **Module 7:** Custom Hash Table with dynamic resizing and data structure selection report.
* **Module 8:** Priority Queue ticket handling system and final Capstone delivery.

```
