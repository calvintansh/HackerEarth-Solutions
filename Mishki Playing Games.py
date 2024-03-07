# Problem Statement: There are Q days of play and N sets of stone
# On each day, there will be a range of sets played which is from l to r sets of stone
# Which l to r sets of stone, Mishki and Hacker will alternate play with Mishki always starting first
# They will divide the a set of stone in half (floor) and if there is one left, the player will delete the set
# Mishki and Hacker will alternate plays till no sets are left and the player with no moves left loses.

# This problem can be solved with a simple for loop where you count the number of moves need to divide each set Qi in half
# till it becomes 1 and then delete it.
# However, you will run into time limit exceeded error

import math

n, q = map(int, input().split())

a = list(map(int, input().split()))

# Instead of running through each move, for each stone set Qi, find the number of moves needed for it to be reduced to 0.
# Then do a cumulative count of moves from Q1 since you will include all days within the range Q(l to r)
cumulative = [0]                                                            # to store the cumulative move count

for i in range(n):
    cumulative.append(cumulative[i] + math.floor(math.log2(a[i])) + 1)      # for each Qi set, take log2 of it to find the number of times it can be divided by 2, 
                                                                            # and add 1 since u need to delete the set. Then add it to the current cumulative sum.
for day in range(q):
    l, r = map(int, input().split())

    count = cumulative[r] - cumulative[l - 1]                               # Taking cumulative(r) - cumulative(l - 1) is the same as the sum of moves from l to r
    
    if count % 2 == 1:                                                      # Since Mishiki always start first, if the total moves is odd, the winner will be her
        print('Mishki')
    else:
        print('Hacker')