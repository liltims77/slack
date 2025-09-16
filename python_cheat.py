
# Arrays / Lists

# Iterate through list
for num in nums:  
    ...

# Iterate with index
for i in range(len(nums)):  
    ...

# Reverse iteration
for i in range(len(nums)-1, -1, -1):  
    ...
################################################################################################################################
# Two pointers (start + end)
left, right = 0, len(nums)-1
while left < right:
    ...
    left += 1
    right -= 1

# Sliding window
window_sum = 0
left = 0
for right in range(len(nums)):
    window_sum += nums[right]
    while window_sum > target:  # shrink window
        window_sum -= nums[left]
        left += 1


#####################################################################################################################################
# Strings


# Traverse
node = head
while node:
    print(node.val)
    node = node.next

# Detect cycle (Floyd’s)
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False

# Reverse linked list
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev



##################################################################################################################################################

# 🔹 Hash Map / Set

# Check duplicates
seen = set()
for x in nums:
    if x in seen: return True
    seen.add(x)

# Frequency count
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1



###########################################################################################################################################

# Binary Search

left, right = 0, len(nums)-1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1


###########################################################################################################################################

# 🔹 Recursion / DFS

def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)


####################################################################################################################

# 🔹 Dynamic Programming

# Fibonacci
dp = [0, 1]
for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])

##################################################################################################

nums.sort()              # in-place
sorted_nums = sorted(nums)  # new list


