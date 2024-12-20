# 0x01. Lockboxes
#### `Algorithm` `Python`

Must Know
For this project, you will need a solid understanding of several key concepts in order to develop a solution that can efficiently determine if all boxes can be opened. Here’s a list of concepts and resources that will be instrumental in tackling this project:

## Concepts Needed:
1. Lists and List Manipulation:
 - Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
 - [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)
2. Graph Theory Basics:
 - Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
 - [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)
3. Algorithmic Complexity:
 - Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
 - [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)
4. Recursion:
 - Some solutions might require a recursive approach to traverse through the boxes and keys.
 - [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)
5. Queue and Stack:
 - Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
 - Python [Queue]((https://www.geeksforgeeks.org/queue-in-python/)) and [Stack](https://www.geeksforgeeks.org/stack-in-python/) (GeeksforGeeks)
6. Set Operations:
 - Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
 - [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

By reviewing these concepts and utilizing these resources, you will be well-equipped to develop an efficient solution for this project, applying both your algorithmic thinking and Python programming skills.

### Additional Resources
[Mock Technical Interview](https://www.youtube.com/watch?v=V8DGdPkBBxg&ab_channel=JaneStreet)

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `20.04` LTS using python3 (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be documented
* Your code should use the `PEP 8` style (version `1.7.x`)
* All your files must be executable

## Tasks

[0. Lockboxes](./0-lockboxes.py)

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A `key` with the same number as a box opens that box
* You can assume all keys will be positive integers
	* There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```
```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

## Background

```
In the "Lockboxes" problem, the primary data structure used is a list of lists,
where each inner list represents a lockbox containing keys to other lockboxes.
The problem revolves around determining if all the boxes can be opened starting from the first box.
While the problem itself doesn't require advanced data structures or algorithms,
there are some fundamental concepts at play:
```

1. **Lists** (***Arrays***): `Lists` (or *arrays*) are used to represent the `lockboxes` and their contents.
Each list element represents a lockbox, and the contents of each lockbox are stored as elements within these lists.

2. **Graph Traversal** ([DFS](https://www.askpython.com/python/examples/depth-first-search-algorithm) or [BFS](https://www.askpython.com/python/examples/breadth-first-search-graph)): The core algorithmic concept in this problem is `graph traversal`. The lockboxes and their keys can be seen as `nodes` and edges in a graph.
You need to determine if there's a path from the first box to all other boxes. 
This can be accomplished using either `Depth-First Search (DFS)` or `Breadth-First Search (BFS)` algorithms to traverse the graph.

3. **Visited Flags**: To keep track of which boxes have been visited during the traversal, a `list` (or array) of `boolean values`, often referred to as "*visited flags*", is used.
Each element in this list corresponds to a box, and it is marked as `True` when the box is visited and `False` when it's not.

4. **Recursion** (*in some implementations*): Some solutions use recursive functions to traverse the graph.
In these implementations, a function is called recursively to explore each box's keys and continue the traversal.

5. **Loops Detection** (*in advanced implementations*): In more advanced versions of the problem,
you might need to implement a `loop detection mechanism` to handle cases where there are `circular dependencies` among the boxes.
This requires more complex algorithms and data structures like `sets` or `dictionaries` to detect loops.

## Depth-First Search

1. **Starting Point**: The `DFS` algorithm begins at a designated starting point,
which could be a specific node in a graph or a root node in a tree.

2. **Visited Nodes**: To keep track of which nodes have been visited,
a data structure (usually an `array` or `list`) called "`visited`" or "`seen`" is used.
Initially, all nodes are marked as `unvisited` or `False`.

3. **Depth-First Exploration**: The algorithm starts at the initial node and
explores as deeply as possible along each branch before backtracking.
Here are the steps for each node:

	a. **Visit the Node**: When a node is encountered, it is marked as `visited`.

	b. **Explore Unvisited Neighbors**: The algorithm then explores all unvisited neighboring nodes (adjacent nodes)
of the current node. It selects one neighbor and proceeds to visit it.

	c. **Recursion** or **Stack**: DFS can be implemented using either `recursion` or an explicit [stack data structure](https://www.askpython.com/python/python-stack).
In the `recursive` approach, the algorithm calls itself for each unvisited neighbor, effectively pushing
the current node onto a call stack. 
In the `stack-based` approach, an explicit stack data structure is used to manage the nodes to be explored.

	d. **Backtracking**: When all neighbors have been visited (or there are no unvisited neighbors),
the algorithm backtracks. This means it returns to the previous node (*if using recursion*) or `pops` nodes from the stack (*if using a stack*).

4. **Repeat**: Steps `3a` to `3d` are repeated until all nodes have been visited or until a specific target node or condition is reached.

5. **Result**: The `DFS` traversal may produce different results depending on the order of exploration. 
You can capture various types of information during the traversal, such as `pre-order` and `post-order traversal`, which help determine the sequence in which nodes were visited.

## Whiteboarding


