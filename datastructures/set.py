'''
mySet = set() # you can initialize a set this way.
anotherSet = {"a", "b"} # you can also initialize a set like this.
#set will have basic functions like:
mySet.add(element)
mySet.remove(element)
If an element is added that already is present in the set the set remains the same
You can also get the length of a set with len(set)
You can join to sets with a union
mySet.union(anotherSet)
or you can union it with the | operator
mySet | anotherSet
You can get the intersection of a set (where both sets have the same elements) with
mySet.intersection(anotherSet)
or you can intersect it with the & operator
mySet & anotherSet
You can find the difference of one set with another using the difference method
mySet.difference(anotherSet)
or you can use the - operator
mySet - anotherSet
You can check if an element is in a set with the 
if element in mySet:
    #do something
You can also learn more comparisons and method with this link:
https://www.geeksforgeeks.org/sets-in-python/
'''