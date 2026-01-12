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

-The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
    =>method removes the items that is not present in both sets

-The difference() method 
    =>will return a new set that will contain only the items from the first set that are not present in the other set.

-The symmetric_difference() method will keep only the elements that are NOT present in both sets.

-The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
- Set operations
- frozenset
- add vs update
- disjoint sets

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
