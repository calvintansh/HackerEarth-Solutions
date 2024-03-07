# Problem Statement: There will be N cities in K groups. And there will be Q queries
# Each query Qi, you will have to count the number of seconds to get from X city to Y city
# You travel immediately within the group (0 s) but u need to use 1s to travel between groups

n, k = map(int, input().split())

# create a dictionary to link the city with its group
cg = {}

for group in range(k):
    row = list(map(int, input().split()))

    numcity = row[0]                            # the first value of each line indicates the number of cities in group Ki

    if numcity > 0:
        for seq in range(numcity):
            city = row[seq + 1]                 # from the second index onwards, it contains the city in group Ki
            cg[city] = group

q = int(input())

for j in range(q):
    x, y = list(map(int, input().split()))

    xloc = cg.get(x)                            # To get the group that city x is in
    yloc = cg.get(y)                            # To get the group that city y is in

    if xloc == yloc:                            # If they both belong to the same group, then there is no travel time
        print(0)
    else:
        forward = abs(xloc - yloc)              # To find the number of groups between x and y 
        backward = k - forward                  # But they can move in the opposite direction too
        print(min(forward, backward))           # To get the lower value
