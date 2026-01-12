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


#Duplicates are ignorde
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
