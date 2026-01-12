#Python sets
myset = {"shoes", "Trousers", "Hoodies", "socks"}
print(myset)
            #output {"Socks", "Trousers", "Shoes", "Hoodies"}


#True and 1, False and 0
myset = {"shoes", "Trousers", 1, True, "Hoodies", 0, "socks", False}
print(myset)
            #output {False, 1, 'Hoodies', 'shoes', 'Trousers', 'socks'}


#length of a set
myset = {"shoes", "Trousers", 1, 0, True, "Hoodies", "socks", False}
print(len(myset))
            #output 6


#Duplicates are ignorde
set1 = {"apple", "banana", "apple", "cherry"}
set2 = {1, 5, 5, 7, 9, 3}
set3 = {True, 1, 0, False, False}
print(set1)
print(set2)
print(set3)
            #output {'apple', 'banana', 'cherry'}
                   # {1, 3, 5, 7, 9}
                   # {0, True}


#mixed data types
mixedset = {"abc", 134, 1, "Goat", True, 45, 0, "male"}
print(mixedset)
            # output {'abc', 1, 0, 'male', 'Goat', 134, 45}