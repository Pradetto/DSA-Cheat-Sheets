# Here are the common patterns / templates I used in my studies:
# 1) Backtracking
# 2) Sorting Algorithms
# 3) Binary Trees, Traversals and BST Recursive/Iterative Implementation
# 4) Graphs / Grids
# 5) Heaps & Priority Queues

from collections import deque
print(
    '******************************************************************************')
print('Backtracking Solutions:')
'''

This is the first batch I am solving:

Combinations
Permutations I
Permutations II
Subsets 1
Subsets II
Combination Sum
Combination Sum II
'''


'''

Combinations Question

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
'''


'''
This is the general backtracking format
choose-
explore-
unchoose-
'''


# Solution One

class Solution:
    def combine(self, n, k):
        res = []

        def helper(start, combo):
            if len(combo) == k:
                res.append(combo.copy())

            for i in range(start, n+1):
                combo.append(i)
                helper(i+1, combo)
                combo.pop()

        helper(1, [])
        return res


s = Solution()
print('Solution 1:')
print(s.combine(4, 2), '\n')

# Solution Two


class Solution2:
    def combine(self, n, k):
        res = []
        self.dfs(range(1, n+1), k, 0, [], res)
        return res

    def dfs(self, nums, k, index, path, res):
        if k == 0:
            res.append(path)

        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)


s = Solution2()
print('Solution 2')
print(s.combine(4, 2), '\n')


'''
Permutations I

It follows this format
Choose
Explore
Unchoose



Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


Pattern - you have to use a for loop going through all the indexes in the provided numbers. You then add one to the combo then for the rest of the number you exclude which you added and pass those options back into the recursive function with the combination
'''

# Solution 3


class Solution3:
    def permute(self, nums):
        res = []

        def helper(combo, options):
            if len(combo) == len(nums):
                res.append(combo)
            for i in range(len(options)):
                helper(combo + [options[i]], options[:i] + options[i+1:])

        helper([], nums)
        return res


s = Solution3()
print('Solution 3')
print(s.permute([1, 2, 3]), '\n')


# Solution 4

class Solution4:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


s = Solution4()
print('Solution 4')
print(s.permute([1, 2, 3]), '\n')


# print('C++ Example to understand recursion')


# def permute2(nums):
#     res = []

#     def helper(nums, i):
#         if i == len(nums) - 1:
#             res.append(nums)

#         for j in range(i, len(nums)):
#             nums[i], nums[j] = nums[j], nums[i]
#             helper(nums, i+1)
#             nums[i], nums[j] = nums[j], nums[i]
#     helper(nums, 0)
#     return res


# print(permute2([1, 2, 3]))

'''
Permutations II

Choose
Explore
Unchoose

The key difference here is you want unique solutions because there might be duplicate numbers.


Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

Pattern - you have to use a for loop going through all the indexes in the provided numbers. You then add one to the combo then for the rest of the number you exclude which you added and pass those options back into the recursive function with the combination. Except for here you have to check if it has been visited or not to ensure you are not duplicating. Clever way is using set
'''

# Solution 5


class Solution5:
    def permuteUnique(self, nums):
        res = []

        def helper(combo, options):
            if len(combo) == len(nums):
                res.append(combo)

            visited = set()
            for i in range(len(options)):
                if options[i] not in visited:
                    visited.add(options[i])
                    helper(combo + [options[i]], options[:i] + options[i+1:])

        helper([], nums)
        return res


s = Solution5()
print('Solution 5')
print(s.permuteUnique([1, 1, 2]), '\n')


class Solution6:
    def permuteUnique(self, nums):
        res, visited = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return

        for i in range(len(nums)):
            if not visited[i]:
                # here should pay attention
                if i > 0 and not visited[i-1] and nums[i] == nums[i-1]:
                    continue
                visited[i] = True
                self.dfs(nums, visited, path+[nums[i]], res)
                visited[i] = False


s = Solution6()
print('Solution 6')
print(s.permuteUnique([1, 1, 2]), '\n')


'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
Accepted
1,123,259
Submissions


Pattern: The answer is ordeless and you do not want duplicates this is the classic increase the index by 1 choose it then unchoose it and make another recursive call to continue on moving through the list
***either you pick a number or you do not so think index with subsets***



def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(i,combo):
        if i >= len(nums):
            res.append(combo.copy())
            return

        combo.append(nums[i])
        backtrack(i+1,combo)
        combo.pop()
        backtrack(i+1,combo)
    
    backtrack(0,[])
    return res
'''

# Solution 7


class Solution7:
    def subsets(self, nums):
        res = []
        combo = []

        def helper(i):
            if i >= len(nums):
                res.append(combo.copy())
                return  # you must put return for this methodology to work

            combo.append(nums[i])
            helper(i+1)
            combo.pop()
            helper(i+1)

        helper(0)
        return res


s = Solution7()
print('Solution 7')
print(s.subsets([1, 2, 3]), '\n')


# Solution 8

class Solution8:

    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)


s = Solution8()
print('Solution 8')
print(s.subsets([1, 2, 3]), '\n')


'''
90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

Time Complexity rough estimate of upper bound: n * 2^n // Explanation: 2^n is equivalent to the number of subsets we are going to have for a list length 2^len(array) you get solo n for how long can each subset be well it can be of length of the list >>>>>>>>> FACT CHECK THIS NOW WITH THE NEW PROBLEM ADDED

when you sort it is nlogn time which is less than the time complexity of the equation so it is fine




'''

# Solution 9


class Solution9:
    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret

    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)


s = Solution9()
print('Solution 9')
print(s.subsetsWithDup([1, 2, 2]), '\n')


print('Subsets II')


def subsetsWithDup(nums):
    def backtrack(i, combo):
        res.append(combo.copy())
        for j in range(i, n):
            if j > i and nums[j] == nums[j-1]:
                continue
            combo.append(nums[j])
            backtrack(j+1, combo)
            combo.pop()

    res = []
    n = len(nums)
    nums.sort()
    backtrack(0, [])
    return res


print(subsetsWithDup([1, 2, 2]), '\n')

'''
Combination Sum I

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''


class Solution10:
    def combinationSum(self, candidates, target):
        res = []

        def helper(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            if i >= len(candidates) or total > target:
                return

            combo.append(candidates[i])
            helper(i, combo, total + candidates[i])
            combo.pop()
            helper(i+1, combo, total)

        helper(0, [], 0)
        return res


s = Solution10()
print('Solution 10')
print(s.combinationSum([2, 3, 6, 7], 7))


'''
Combination Sum II


Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''


class Solution11:
    def combinationSum2(self, candidates, target):
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
        # candidates.sort()
        # res = []

        # def helper(start, combo, target):
        #     if target == 0:
        #         res.append(combo.copy())

        #     if target <= 0:
        #         return

        #     prev = -1
        #     for i in range(start, len(candidates)):
        #         if candidates[i] == prev:
        #             continue
        #         combo.append(candidates[i])
        #         helper(start + 1, combo, target-candidates[i])
        #         combo.pop()
        #         prev = candidates[i]

        # helper(0, [], target)
        # return res

s = Solution11()
print('\nSolution 11')
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))


# def lengthOfLongestSubstring(s):
#     seen = {}
#     l = 0
#     longest = 0

#     for r in range(len(s)):
#         if s[r] not in seen:
#             # you add by one since if the left pointer was 0 and your r is at index 3 it would actually be 4 characters instead of 3
#             longest = max(longest, r-l + 1)
#         else:
#             if seen[s[r]] < l:  # last example demonstrates the importance of this case2: s[r] is not inside the current window, we can keep increase the window
#                 longest = max(longest, r-l+1)
#             else:
#                 l = seen[s[r]]+1
#         seen[s[r]] = r
#     return longest


# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("tmmzuxt"))  # explains the if seen[s[r]]<l part
print('******************************************************************************')
print("Sorting Solutions")

'''
Here are some random sorting and searching templates that are important to remember

'''

'''
Bubble Sort
Time: O(n^2)
Space: O(1)
'''

print('Bubble Sort')


def bubble(arr):
    for i in range(len(arr)-1):
        while arr[i] < arr[i+1] and i < len(arr):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubble([5, 2, 1, 34, 2, 123, 34]))

'''
Insertion Sort
Time: O(n^2)
Space: O(1)

Good for nearly sorted list or short lists can almost run O(n)
'''

print('\nInsert Sort')


def insert(arr):
    for i in range(len(arr)):
        sort_val = arr[i]
        while i > 0 and arr[i-1] > sort_val:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i - 1
    return arr


print(insert([5, 2, 1, 34, 2, 123, 34]))

'''
Merge Sort
Time: O(nlogn)
Space: O(n)
'''

print('\nMerge Sort')


def merge(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    l_arr = arr[:mid]
    r_arr = arr[mid:]
    return mergeTwo(merge(l_arr), merge(r_arr))


def mergeTwo(a, b):
    li = 0
    ri = 0
    res = []

    while li < len(a) and ri < len(b):
        if a[li] < b[ri]:
            res.append(a[li])
            li += 1
        else:
            res.append(b[ri])
            ri += 1
    return res + a[li:] + b[ri:]


print(merge([5, 8, 9, 6, 4, 56, 765, 4, 324, 54, 6, 56, 9]))


'''
Quick Sort
Time: O(nlogn) // O(n^2) worst case
Space: O(logn)

be careful if picked bad pivot this runs in terribel time
'''
# pi stands for partition index

print('\nQuick Sort')


def quicksort(l, r, arr):
    if len(arr) == 1:
        return arr
    if l < r:
        pi = partition(l, r, arr)
        quicksort(l, pi-1, arr)
        quicksort(pi+1, r, arr)
    return arr


def partition(l, r, arr):
    pivot, ptr = arr[r], l
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    arr[ptr], arr[r] = arr[r], arr[ptr]
    return ptr


example = [4, 5, 1, 2, 3]
print(quicksort(0, len(example)-1, example))

'''
Heap Sort
Time: O(nlogn)
Space: O(1)


Explanation:
So essentially you need a complete binary tree (means there is no gaps in between them) if the tree is not a max heap or min heap you can preform heapify which reads the bottom of the tree and then bubbles up the min or max numbers depending upon what you are trying to do for both sides of the binary tree eventually it will be a min heap or max heap. This takes O(logn) time since it is only half the numbers you are touching. FYI 2^(h+1) -1  is amount of nodes of  a full binary tree. If you don't even have a tree you have to create one from scratch. So there are two steps for heap sort build the tree and the delete the top nodes and it builds a sorted list. Building the tree is O(n) time hence the O(nlogn) time complexity. To do the sort you delete the min or max node. From there you take the last element of the complete binary tree and place it at the root. You then preform the swaps to make it a min or max heap again bubble down that while creating a max/min heap. **** Look up how the bubble down method works on bigger trees. You then delete a node again and repeat the process. This is why it is good for priority queues super efficient on time and space

Probably wont be asked how to implement a heap from scratch but it is good to know how it works conceptually
'''

# # Python program for implementation of heap Sort probably not needed but good conceptually

# # To heapify subtree rooted at index i.
# # n is size of heap


# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2

#     # See if left child of root exists and is
#     # greater than root
#     if l < n and arr[i] < arr[l]:
#         largest = l

#     # See if right child of root exists and is
#     # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r

#     # Change root, if needed
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # swap

#     # Heapify the root.
#     heapify(arr, n, largest)

# # The main function to sort an array of given size


# def heapSort(arr):
#     n = len(arr)

#     # Build a maxheap.
#     # Since last parent will be at ((n//2)-1) we can start at that location.
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     # One by one extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # swap
#         heapify(arr, i, 0)


# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d" % arr[i]),

'''
Radix Sort - haven't learned
Counting Sort - haven't learned
'''

print('******************************************************************************')
print('Binary Trees, Traversals and BST Recursive/Iterative Implementation')

'''
Inorder Traversal Steps (Recursive and Iterative):

1) Visit Left Subtree Recursively
2) Visit Root (or Subtree root)
3) Visit right Subtree Recursively

Trick:

    +
   / \
  A   B

Result: A+B

Below is an implementation of in-order traversal for the following list [10, 14, 19, 27, 31, 35, 42]
'''

print('\nInorder BST')


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        node = Node(data)
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorderTraversalRecursive(self, root):
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.data)
            inorder(root.right)

        inorder(root)
        return res

        # Recursive Option Two (returns None at the end):
        # if root is None:
        #     return
        # self.inorderTraversalRecursive(root.left)
        # print(root.data, end=' ')
        # self.inorderTraversalRecursive(root.right)

        # REVIST THIS Recursive call and how it works
        # if root:
        #     res = self.inorderTraversal(root.left)
        #     res.append(root.data)
        #     res = res + self.inorderTraversal(root.right)
        # return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# root.printTree()
answer = [10, 14, 19, 27, 31, 35, 42]
print('Answer should be:\n', answer)
print(root.inorderTraversalRecursive(root))

'''
Pre-Order Traversal
1) Visit Root
2) Visit Left Subtree Recursively
3) Visit Right Subtree Recursively
Trick:

    +
   / \
  A   B

Result: +AB
'''

print('\nPreorder Traversal BST')


class Node2:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # node = Node2(data) # not recommended extra space for recursive calls that you don't always make

        if not self.data:  # checking if no root
            self.data = data
            return

        if self.data == data:  # checking for duplicate data in a binary search tree you disregard this
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = Node2(data)
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = Node2(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def preorderTraversalRecursive(self, root):
        res = []

        def preorder(root):
            if not root:
                return

            res.append(root.data)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res


root2 = Node2(27)
root2.insert(14)
root2.insert(35)
root2.insert(10)
root2.insert(19)
root2.insert(31)
root2.insert(42)
# root2.printTree()
answer = [27, 14, 10, 19, 35, 31, 42]
print('Answer should be:\n', answer)
print(root2.preorderTraversalRecursive(root2))


print('Iterative Version PreOrder Traversal')


class NodeIterative:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def insert(self, data):
        node = NodeIterative(data)

        if self.root == None:
            self.root = node
            self.numNodes += 1
            return

        cur = self.root
        while cur:
            if cur.data == data:
                return
            elif data < cur.data:
                if cur.left == None:
                    cur.left = node
                cur = cur.left
            elif data > cur.data:
                if cur.right == None:
                    cur.right = node
                cur = cur.right
            self.numNodes += 1

    def find(self, target):
        if self.root == None:
            return False

        cur = self.root
        while cur:
            if cur.data == target:
                return True
            elif target < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def preorderTraversal(self):
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.data)
            preorder(root.left)
            preorder(root.right)

        if self.root != None:
            preorder(self.root)

        return res


bst = BST()
bst.insert(27)
bst.insert(14)
bst.insert(35)
bst.insert(10)
bst.insert(19)
bst.insert(31)
bst.insert(42)
print(bst.preorderTraversal())

'''
Post-Order Traversal
1) Visit Left Subtree Recursively
2) Visit Right Subtree Recursively
3) Visit Root

Trick:

    +
   / \
  A   B

Result: AB+
'''

print('\nPostOrder Traversal BST')

class Node3:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        node = Node3(data)

        if not self.data:
            self.data = data
            return

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)  # this is a recursive insert(call)
                return
            self.left = node
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = node

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def postorderTraversalRecursive(self, root):
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.data)

        postorder(root)
        return res


root3 = Node3(27)
root3.insert(14)
root3.insert(35)
root3.insert(10)
root3.insert(19)
root3.insert(31)
root3.insert(42)
# root3.printTree()
answer = [10, 19, 14, 31, 42, 35, 27]
print('Answer should be:\n', answer)
print(root3.postorderTraversalRecursive(root3))

print('******************************************************************************')
print('Graphs/Grids')

'''
A classic grid questions that requires DFS or BFS.

200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

# Solving with DFS


def numIslands(grid):
    if not grid:
        return 0

    islands = 0
    rows, cols = len(grid), len(grid[0])

    # don't have to include grid
    def helper(grid, i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        helper(grid, i+1, j)
        helper(grid, i-1, j)
        helper(grid, i, j+1)
        helper(grid, i, j-1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                helper(grid, i, j)
                islands += 1
    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))


# Solving with BFS
def numIslands2(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(i, j):
        q = deque()
        visited.add((i, j))
        q.append((i, j))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for di, dj in directions:
                i, j = row + di, col + dj
                if (i) in range(rows) and (j) in range(cols) and grid[i][j] == "1" and (i, j) not in visited:
                    q.append((i, j))
                    visited.add((i, j))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs(i, j)
                islands += 1
    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands2(grid))


print('******************************************************************************')
print('Heaps and Priority Queues')

'''
Questions are usually with the something involving K i.e. merged k or k closest points

To solve these questions use the heapq module in python.

establish a priorityQ = []
pretty much you put everything into the heapq.heappush(pq,(node.val,id(node))) so that takes O(n) time

then you heapq.heappop(pq) to get the min value of the priority queue. Max Q is not supported so just make the numbers negative if needed
'''

'''
A popular Heap Question

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

Solution is blocked out because this was for linked lists
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         #id just generates a random value to associate the node
#         pq = []

#         for node in lists:
#             if node:
#                 heapq.heappush(pq, (node.val, id(node), node))

#         dummy = ListNode()
#         cur = dummy

#         while pq:
#             _, _, node = heapq.heappop(pq)
#             cur.next = node
#             if node.next:
#                 heapq.heappush(pq, (node.next.val, id(node.next), node.next))

#             cur = cur.next
#         return dummy.next


print('Practice answers below')
print("try the problems above here")
