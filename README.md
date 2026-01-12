# Python Sets

This project contains examples and explanations of Python sets and frozensets.

## Topics Covered
- Set creation
     Sets are written with curly brackets
     after creating a set, you cannot access its items using indexes since they are unordered
     1 and True are treated as same, also 0 and False
- add() method
    To add one item to a set use the add() method.
- Mutiple items use update() method
NB:The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

-  Use the pop() method to remove an item, but this method will remove a random item
-loop sets
-Join Loops using various methods
    Join a set and a tuple

-The update() method
    changes the original set, and does not return a new set.

-The intersection() method will return a new set, that only contains the items that are present in both sets.
    ## Use the & operator instead of the intersection() method => Same Result


- Set operations
- frozenset
- add vs update
- disjoint sets

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
