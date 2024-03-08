# Problem Statement: From a string S, find the number of letters sequences such that the number of distinct
# letters within each set is equal to K

# You can use a simple sliding window approach to loop through S and check if the distinct letters within the window is equal to K
# However, you will run into time limit exceeded error

k = int(input())
s = input()

count = 0

slength = len(s)

# Use a sliding window and extract the distinct letters
for start in range(slength):
    index = start                       # start is the left slides and index is the right slider
    distinct = set()                    # to get distinct letters and faster computation times
    distinctlen = 0                     # to count the number of distinct letters

    while index < slength:
        if s[index] not in distinct:    # if the letter is distinct, add it to distinct
            distinct.add(s[index])
            distinctlen += 1            # to count the size of distinct
             
        if distinctlen == k:            # if the number of distinct letters = K, then increase the count
            count += 1
        elif distinctlen > k:           # once the number of distinct letters exceeds K, exit the loop
            break
        
        index += 1                      # to move the right slider


print(count)