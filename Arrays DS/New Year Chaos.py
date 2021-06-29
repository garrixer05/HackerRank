def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] != i+1:
            if i-1>=0 and q[i-1] == i+1:
                q[i-1],q[i] = q[i],q[i-1]                                       #We have to swap each time so tha our count will be accurate
                count+=1
            elif i-2>=0 and q[i-2] == i+1:
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = q[i-1]
                count+=2
            else:
                count = -1
                break



    if count<0:
        print('Too chaotic')
    else:
        print(count)
