# Most Nodes Algorithm

A command-line tool that, given a weighted graph and a time budget, finds a path visiting as many distinct vertices as possible without exceeding the budget.  
Under the hood, it runs a depth-first search (DFS) with memoized “best-so-far” pruning: whenever it’s impossible to beat the current record (even optimistically), it backtracks immediately.

---

## 📋 Requirements

- **Python** ≥ 3.8  
- **Windows 11** (for the provided `.exe`); or any OS with Python 3.8+ to run the script directly.

---

## 🗂️ Contents

Place the following files together in a single folder:

- **`most_nodes_algorithm.exe`**  
  Precompiled Windows executable.  
- **`most_nodes_algorithm.py`**  
  (Optional) Python source—run with `python most_nodes_algorithm.py`.  
- **`graph_values.txt`**  
  Input file describing the graph and time limit.  
- **`README.md`**  
  This document.

---

## 🚀 Usage

### Windows executable

```batch
cd <folder_containing_files>
most_nodes_algorithm.exe graph_values.txt
