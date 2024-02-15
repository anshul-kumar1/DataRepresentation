# Question 1
def put(val :int, hm: list) -> list:
    index = val % 7
    hm[index].append(val)
    return hm

# counts the number of occurences by utilizing a hashmap
def frequency_count(l: list) -> list:
    hm = [[] for elem in range(7)]
    for i in l:
        put(i, hm)

    dict = {}
    final = []
    for bucket in hm:
        temp = {x:bucket.count(x) for x in bucket} # counting of the elements in each bucket
        dict.update(temp)

    sorted_dict = sorted(dict.keys()) # O(N log N)

    for elem in sorted_dict:
        final.append((elem, dict.get(elem)))

    return final

# Question 2
class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.preorder = [] #keeping the option of looking at the binary tree in a list form

    # inserts an element into the binary tree appropriately
    def insert(self, n: int):
        if n < self.val:
            if self.left:
                self.left.insert(n)
            else:
                self.left = BinaryTree(n)
        else:
            if self.right:
                self.right.insert(n)
            else:
                self.right = BinaryTree(n)

    # checks if an element is in the binary tree
    def isIn(self, n: int) -> bool:
        if n == self.val:
            return True
        elif n < self.val:
            if self.left:
                return self.left.isIn(n)
            else:
                return False
        else:
            if self.right:
                return self.right.isIn(n)
            else:
                return False

    # converts the binary tree to a list
    def toList(self, bt):
        if bt:
            self.preorder.append(bt.val)
            self.toList(bt.left)
            self.toList(bt.right)
        return self.preorder


# finds the ancestor of a node in a binary tree
def ancestor(bt: BinaryTree, n: int) -> list:
    path = []
    curr = bt
    # uses temp value 'curr' to traverse the bst
    while curr:
        path.append(curr.val)
        if n == curr.val:
            return path
        else:
            if n < curr.val:
                curr = curr.left
            else:
                curr = curr.right

    return []


# finds the descendant of a node in a binary tree
def descendant(root: BinaryTree, n: int) -> list:
    if root:
        # following the general properties of a bst
        if root.val == n:
            return root.toList(root)[1:] # removing the root element as it is not a descendent
        elif n < root.val:
            return descendant(root.left, n)
        else:
            return descendant(root.right, n)
    else:
        return []

# Question 3
# Uses the insert function and makes a tree from a list
def build_tree(l: list):
    tree = BinaryTree(l[0])
    i = 1
    while i < len(l):
        tree.insert(l[i])
        i = i + 1
    return tree

# retuns the intersection of two lists
def intersect_bst(A: list, B: list) -> list:
    if len(A) == 0 or len(B) == 0:
        return []
    tree_A = build_tree(A)
    tree_B = build_tree(B)
    final = []
    for elem in A:
        # checks if the element in one tree exists in the other
        if tree_B.isIn(elem):
            final.append(elem)
    return final

def difference_bst(A: list, B: list) -> list:
    # Handling edge cases
    if len(A) == 0 and len(B) == 0:
        return []
    if len(A)==0:
        return B
    if len(B)==0:
        return A

    tree_A = build_tree(A)
    tree_B = build_tree(B)
    final = []
    for elem in A:
        # checks if the element in one tree exists in the other
        if not tree_B.isIn(elem):
            final.append(elem)
    for elem in B:
        # checks if the element in one tree exists in the other
        if not tree_A.isIn(elem):
            final.append(elem)
    return final

# checks if the given two lists are the same by comparing the trees
def equals_bst(A: list, B: list) -> bool:
    if len(A) == 0 and len(B) == 0:
        return True
    elif len(A) == 0 or len(B) == 0:
        return False

    tree_A = build_tree(A)
    tree_B = build_tree(B)
    for elem in tree_A.toList(tree_A):
        if elem not in tree_B.toList(tree_B):
            return False # When an element that does not exist in the Tree is encountered, it returns false
    return True

class HashTable:
    def __init__(self,buckets):
        # length of the hashtable
        self.buckets = buckets
        # initializing as a 2d array for chaining
        self.table = [[] for elem in range(buckets)]

    # hash function for every table is unique
    def hash_function(self, k: int) -> int:
        return k % self.buckets

# inserts a number into a hastable while preserving the hashtable
def insert(element: int, A: HashTable) -> HashTable:
    index = A.hash_function(element)
    A.table[index].append(element)
    return A

# checks if an element is in the hashtable by locating in a specific bucket
def isIn(element: int, A: HashTable) -> HashTable:
    index = A.hash_function(element)
    if element in A.table[index]:
        return True
    else:
        return False

# finds the element and deletes it
def delete(element: int, A: HashTable) -> HashTable:
    try:
        index = A.hash_function(element)
        A.table[index].remove(element)
        return A
    except ValueError:
        print("Value Error Caught, element not in table") # catches when the element does not exist

# uses the insert function and builds a hashmap from a list
def build_ht(l: list, buckets: int) -> HashTable:
    ht = HashTable(4)
    for elem in l:
        insert(elem, ht)
    return ht

# Question 5
# finds the intersection between 2 lists by taking advantage of hashtables
def intersection_ht(A: list, B: list) -> list:
    if len(A) == 0 or len(B) == 0: # cases for empty lists also handled
        return []
    ht_A = build_ht(A, 4) # 4 buckets constant as stated in the homrwork
    ht_B = build_ht(B, 4)
    final = []
    for elem in A:
        if isIn(elem, ht_B): # checks if the element is in hashtable B (O(1))
            final.append(elem)
    return final

def difference_ht(A: list, B: list) -> list:
    if len(A) == 0 and len(B) == 0: # cases for empty lists also handled
        return []
    if len(A) == 0:
        return B
    if len(B) == 0:
        return A

    ht_A = build_ht(A, 4)
    ht_B = build_ht(B, 4)
    final = []
    for elem in A:
        if not isIn(elem, ht_B):
            final.append(elem)
    for elem in B:
        if not isIn(elem, ht_A):
            final.append(elem)
    # went over both lists to find the elements that are not common in either.
    return final

def equal_ht(A: list, B: list) -> bool:
    if len(A) == 0 and len(B) == 0:
        return True
    if len(A) == 0 or len(B) == 0:
        return False
    ht_A = build_ht(A, 4)
    ht_B = build_ht(B, 4)

    for elem in A:
        if not isIn(elem, ht_B):
            return False # When an element that does not exist in the hashtable is encountered, it returns false

    return True

# Test cases #

# Question 1
print(frequency_count([]))
print(frequency_count([1]))
print(frequency_count([1,1,1,1,1,1,2,1,1,1,1,1,1,1,1]))
print(frequency_count([1,2,3,4,5,6]))
print(frequency_count([10,9,8,7,6,5,4,3,2,1]))

# Question 5
l1 = [1,2,3,4,5,6,7]
l2 = [7,6,5,4,3,2]

print(intersect_bst(l1, l2))
print(difference_bst(l1,l2))
print(equals_bst(l1, l2))