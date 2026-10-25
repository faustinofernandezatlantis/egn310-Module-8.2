import time
import streamlit as st
from engine import Trie, LRUCache

st.set_page_config(
    page_title="Autocomplete & Recent Queries Engine",
    page_icon="🔍",
    layout="wide"
)

# Initialize Trie and LRU Cache in Streamlit session state
if "trie" not in st.session_state:
    st.session_state.trie = Trie()
    st.session_state.lru = LRUCache(capacity=5)

    # Pre-populate with initial dataset
    sample_dataset = [
        ("algorithm", 150),
        ("array", 120),
        ("binary search", 95),
        ("binary search tree", 110),
        ("breadth first search", 85),
        ("depth first search", 80),
        ("dynamic programming", 130),
        ("graph", 75),
        ("hash table", 140),
        ("heap", 105),
        ("linked list", 115),
        ("merge sort", 90),
        ("priority queue", 100),
        ("quicksort", 95),
        ("recursion", 125),
        ("stack", 110),
        ("trie", 200),
    ]
    for word, freq in sample_dataset:
        st.session_state.trie.insert(word, freq)

st.title("🔍 Search Autocomplete & Recent Queries Engine")
st.write("A custom **Trie** and **LRU Cache** implementation with real-time performance metrics.")

# Sidebar Controls
st.sidebar.header("Data Management")

# Add Word Form
with st.sidebar.expander("➕ Add Word to Trie", expanded=True):
    with st.form("add_word_form"):
        new_word = st.text_input("Word / Query")
        new_freq = st.number_input("Initial Frequency Rank", min_value=1, value=10)
        submit_word = st.form_submit_button("Add Word")

        if submit_word and new_word:
            st.session_state.trie.insert(new_word, int(new_freq))
            st.success(f"Added '{new_word}' with rank {new_freq}!")
            st.rerun()

# Main Search Interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("⚡ Live Autocomplete Search")
    query = st.text_input("Type a prefix:", placeholder="e.g., bi, search, trie...")

    if query:
        # Measure Trie Autocomplete Execution Time
        start_time = time.perf_counter_ns()
        suggestions = st.session_state.trie.autocomplete(query, k=5)
        end_time = time.perf_counter_ns()

        lookup_time_ms = (end_time - start_time) / 1e6

        # Record search query in LRU Cache
        st.session_state.lru.put(query.lower().strip(), f"{len(suggestions)} suggestions found")

        st.markdown(f"**Top Suggestions for '{query}':**")
        if suggestions:
            for idx, word in enumerate(suggestions, 1):
                st.write(f"{idx}. `{word}`")
        else:
            st.info("No matching suggestions found.")

        # Performance Metric
        st.metric(label="Lookup Latency (O(K))", value=f"{lookup_time_ms:.4f} ms")

with col2:
    st.subheader("📜 Recent Search History (LRU Cache)")
    history = st.session_state.lru.get_history()

    if history:
        for idx, (term, details) in enumerate(history, 1):
            st.write(f"**{idx}.** `{term}` — *{details}*")
    else:
        st.info("No search history yet.")

    st.markdown("---")
    st.write(f"**Total Dataset Words:** `{len(st.session_state.trie)}`")