#Python sets
myset = {"shoes", "Trousers", "Hoodies", "socks"}
print(myset)
            #output: {"Socks", "Trousers", "Shoes", "Hoodies"}


#True and 1, False and 0
myset = {"shoes", "Trousers", 1, True, "Hoodies", 0, "socks", False}
print(myset)
            #output: {False, 1, 'Hoodies', 'shoes', 'Trousers', 'socks'}


#length of a set
myset = {"shoes", "Trousers", 1, 0, True, "Hoodies", "socks", False}
print(len(myset))
            #output: 6


#Duplicates are ignored
set1 = {"apple", "banana", "apple", "cherry"}
set2 = {1, 5, 5, 7, 9, 3}
set3 = {True, 1, 0, False, False}
print(set1)
print(set2)
print(set3)
            #output: {'apple', 'banana', 'cherry'}
                   # {1, 3, 5, 7, 9}
                   # {0, True}


#mixed data types
mixedset = {"abc", 134, 1, "Goat", True, 45, 0, "male"}
print(mixedset)
            # output: {'abc', 1, 0, 'male', 'Goat', 134, 45}


#set constructor
myset = set(("shoes", "Trousers", "Hoodies", "socks"))
print(myset)
            #output: {'shoes', 'Hoodies', 'socks', 'Trousers'}

#Access items
myset = {"shoes", "Trousers", "Hoodies", "socks"}
for x in myset:
    print(x) #output: socks, Trousers, shoes, Hoodies

print("Trousers" in myset)
print("socks" not in myset)
            # Output:True
            #Output: False

# add() method
myset = {"shoes", "Trousers", "Hoodies", "socks"}
myset.add("Sheets")
print(myset) #Output: {'Trousers', 'shoes', 'Sheets', 'Hoodies', 'socks'}

# update() method
myset = {"shoes", "Trousers", "Hoodies", "socks"}
hiddenset = {"Xbox", "Soundbar", "Fridge"}
myset.update(hiddenset)
print(myset) #Output: {'Hoodies', 'socks', 'Xbox', 'Soundbar', 'Fridge', 'Trousers', 'shoes'}

#Example 2. update any as long as its iterable
myset = {"shoes", "Trousers", "Hoodies", "socks"}
mylist = ["Money", "Goods", "Commodities"]
myset.update(mylist)
print(myset) #Output: {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}

#Remove item from set => remove() method
currentset = {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}
currentset.remove("socks")
print(currentset)  #Output: {'shoes', 'Trousers', 'Hoodies', 'Goods', 'Commodities', 'Money'}

# Remove using => discard() method
#NB discard() does not raise an error in cases where an item does not exist
currentset = {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}
currentset.discard("socks")
print(currentset)  #Output: currentset = {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}

#Remove item using => pop() method
#This method removes random item
currentset = {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}
currentset.pop()
print(currentset) #Output : {'Commodities', 'socks', 'Money', 'Goods', 'shoes', 'Trousers'}
                # Any time it will remove different random item in the set

currentset = {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}
x = currentset.pop()
print (x) #Output: Commodities   #NB: Random item removed

#The clear() method 
myset = {"shoes", "Trousers", "Hoodies", "socks"}
myset.clear()
print(myset) #Output  set() 
            #NB empties the set
            #NB for del() method it will raise an error since it will erase the set completely

#Loop Sets
currentset = {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}
for x in currentset:
    print(x)

    #Or
for x in {'Trousers', 'Commodities', 'shoes', 'Goods', 'socks', 'Money', 'Hoodies'}:
    print(x) 
    #Output: 
        # Goods
        #Commodities
        #Hoodies
        #Trousers
        #socks
        #shoes
        #Money

#Join Sets => .union() method
set1 = {34, 89, 12, 92}
set2 = {"abc", "dfg", "otp"}
set3 = set1.union (set2)
print(set3)  #Output: {34, 'otp', 89, 'abc', 12, 'dfg', 92}

    #OR
set1 = {34, 89, 12, 92}
set2 = {"abc", "dfg", "otp"}
set3 = set1 | set2
print(set3) #Output {34, 'otp', 89, 'abc', 12, 'dfg', 92}
            #NB this produces a sort of "NEW" set but with same items in sets involved.

#Join Multiple sets
set1 = {45, 56,907, 89, 90}
set2 = {"abc", "dft", "vga"}
set3 = {"maize", "apple", "carrots"}
set4 = {"planet", "space"}
set5 = set1.union(set2, set3,set4)

print(set5)

   #OR
set1 = {45, 56,907, 89, 90}
set2 = {"abc", "dft", "vga"}
set3 = {"maize", "apple", "carrots"}
set4 = {"planet", "space"}
set5 = set1| set2 | set3| set4

print(set5)
#Output: {'maize', 'planet', 'abc', 'space', 'dft', 907, 45, 'carrots', 'apple', 'vga', 56, 89, 90}
#NB |OPERATOR joins only a set to another set(s) unlike .union

#JOIN SET AND a TUPLE
x = {"a", "b", "c"}
y = (4, 2, 9)

z = x.union(y)
print(z) #Output: {2, 4, 9, 'b', 'a', 'c'}

#The update() method
set1 = {45, 56,907, 89, 90}
set2 = {"abc", "dft", "vga"}
set1.update(set2)

print(set1) #Output: {'dft', 'abc', 'vga', 56, 89, 90, 907, 45}

    #OR
set1 = {45, 56,907, 89, 90}
set2 = {"abc", "dft", "vga"}
set2.update(set1)

print(set2) #Output: {'dft', 'abc', 'vga', 907, 45, 56, 89, 90}

#Can also use |= insted of .update()
set1 = {45, 56,9077, 89, 98}
set2 = {"abcd", "dftk", "ovga"}
set1 |= set2 

print(set1) #Output: {'ovga', 98, 9077, 'dftk', 56, 89, 45, 'abcd'}  ...random indexing

#more samples
a = {7, 13, 4, 90}
b = {87, 16, 9}
c = {45, 87, 63}

a |= b | c  #logic operation formula

print(a) #output {4, 7, 9, 13, 45, 16, 87, 90, 63}

#More .update sample formula
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}

x.update(y, z)

print(x) #Ouput: {'banana', 'bluebird', 'cherry', 'microsoft', 'micra', 'google', 'apple'}

# intersection() method
# It Join sets but keep only the duplicates:
set1 = {"cat", "dog", "cow", "goat"}
set2 = {"goat", "lion", "hyena"}

setX = set1.intersection(set2)
print(setX) #Output: {'goat'}

# Use the & operator instead of the intersection() method => Same Result
set1 = {"cat", "dog", "cow", "goat"}
set2 = {"goat", "lion", "hyena"}

setX = set1 & set2
print(setX) #Output: {'goat'}

#example2
set1 = {45, 56, "abc", 907, 89, 90}
set2 = {"abc", "dft", "vga"}
set3 = {"maize", "abc", "apple", "carrots"}
set4 = {"planet", "abc", "space"}

results = set1.intersection(set2, set3, set4)
print(results) #Output {"abc"} 

    #OR
results = set1 & set2 & set3 & set4
print(results) #Output: {'abc'}

#The intersection_update() method
set1 = {45, 56, "abc", 907, 89, 90}
set2 = {"abc", "dft", "vga"}

set1.intersection_update(set2)
print(set1) #Output: {"abc"}   =>method removes the items that is not present in both sets

#set.intersection_update(set1, set2 ... etc)

    #OR use &= Operator  Shorter syntax (set &= set1 & set2 ... etc.)

set1 = {45, 56, "abc", "maize", 907, 89, 90}
set2 = {"abc", "dft", "maize","vga"}
set3 = {"maize", "abc", "apple", "carrots"}
set4 = {"planet", "maize","abc", "space"}

set1 &= set2 & set3 & set4
print(set1) #Output {'abc', 'maize'}

#The difference() method 
set1 = {45, "avocado", "abc", "orange", 907}
set2 = {"abc", "dft", 907, "maize","vga"}
set3 = {"maize", "abc", 45, "apple"}

x = set1.difference(set2, set3)        # => set.difference(set1, set2 ... etc.)

print(x) #Output {'orange', 'avocado'}  =>return a new set of items present in set1 but not present in other sets

        #OR rn (-)operator
x = set1 - set2 - set3          # => set - set1 - set2 .... etc.

print(x) #Output: {'orange', 'avocado'}

#The symmetric_difference() method => keep only the elements that are NOT present in both sets
set1 = {45, "avocado", "abc", "orange", 907}
set2 = {"abc", "dft", 45, 907, "orange", "maize","vga"}

x = set1.symmetric_difference(set2)       # =>set.symmetric_difference(set1)

print(x)   #Output: {'dft', 'maize', 'avocado', 'vga'}
            #NB this take arguments for only two sets 

            #OR use (^) operator
x = set1 ^ set2 
print(x)  #Output: {'maize', 'vga', 'avocado', 'dft'}

# The symmetric_difference_update() method   =>set.symmetric_difference_update(set1)
set1 = {45, "avocado", "abc", "orange", 907}
set2 = {"abc", "dft", 45, 907, "orange", "maize","vga"}

set1.symmetric_difference_update(set2)
print(set1) #Output: {'vga', 'maize', 'avocado', 'dft'}   => method to keep the items that are not present in both sets

        #OR shorter syntax Operator (^=)   =>set ^= set1 (formula)
set1 = {45, "avocado", "abc", "orange", 907}
set2 = {"abc", "dft", 45, 907, "orange", "maize","vga"}

set1 ^= set2

print(set1)   #Output: {'vga', 'maize', 'avocado', 'dft'}