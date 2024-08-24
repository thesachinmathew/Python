#find the common elements in three sorted array
def fin(a, b, c):
    return sorted(set(a) & set(b) & set(c))
print(fin([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]))

#find the length of the longet increasing subsequents in the given array
def l(nums):
    from bisect import bisect_left
    lst = []
    for num in nums:
        pos = bisect_left(lst, num)
        if pos == len(lst): lst.append(num)
        else: lst[pos] = num
    return len(lst)
print(l([10, 9, 2, 5, 3, 7, 101, 18]))

#find the majority elements in an array the apears more than n/2 times
def maj(n):
    from collections import Counter
    c = max(set(n), key=n.count)
    return c if n.count(c) > len(n) // 2 else None
print(maj([3, 3, 4, 2, 4, 4, 2, 4, 4]))

#wap to find the min num of jumps to reach the end of an array where each elm is the min jump length
def mj(arr):
    j, f, e = 0, 0, 0
    for i in range(len(arr) - 1):
        f = max(f, i + arr[i])
        if i == e:
            j += 1
            e = f
            if e >= len(arr) - 1: break
    return j
print(mj([2,3,4,2,3,4,2]))  

#longest common sudseqeunts
def lcs(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if s1[i - 1] == s2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
print(lcs("abcde", "ace"))
