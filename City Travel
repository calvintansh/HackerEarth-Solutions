# Problem Statement:
# You have to cover S distance in X steps except for 
# N exceptions where on certain days T, you will be travelling Y distance instead of X

# You can solve this program with a simple for loop running through the days and deducting
# X distances or Y distance if days == T, but you will run into time limit exceeded problems

import math # for math.ceil

s, x, n = map(int, input().split())

# To store T and Y
distance = []

for _ in range (n):
    t, y = map(int, input().split())
    distance.append([t, y])

distance.sort() # To ensure that T is in ascending order

# Case 1: When you can finish the distance S without using any Y
currentday = distance[0][0] # first T
prevday = currentday - 1 # the day before first T

currenttravel = prevday * x + distance[0][1] # the total distance travelled till first T

remaining = s - currenttravel # distance remaining after reaching first T

if remaining < 0: # if S is reached before first T, then there will be no Y distance covered
    days = math.ceil(s / x)
else: # Need to use T and Y
    i = 1 # index for Ti

    while i < n: # To loop through all T Y
        prevtravel = currenttravel # for distance travelled thus far till Ti

        currentday = distance[i][0]
        prevday = currentday - 1
        gapdays = prevday - distance[i-1][0] # days between the day before Ti and T(i-1)

        prevtraveltotal = prevtravel + gapdays * x # to find the distance travelled till the day before Ti

        currenttravel = prevtraveltotal + distance[i][1] # the distance travelled till Ti

        remaining = s - currenttravel # distance remaining after reaching Ti

        if remaining < 0:
            # Case 2: When you are able to reach S before Ti
            if (s - prevtraveltotal) < 0: 
                gapdays = math.ceil( (s - prevtravel) / x ) # find the number of days after T(i-1) that is needed to complete S
                days = distance[i-1][0] + gapdays # add it to T(i-1)

                break

            else: 
                # Case 3: When you reach S at Ti
                days = distance[i][0]

                break
        
        i += 1
    
    # Case 4: When you reach S after the last Ti
    if i == n:
        gapdays = math.ceil( (s - currenttravel) / x ) # find the number of days after T(last) that is needed to complete S
        days = distance[i-1][0] + gapdays

print(days)