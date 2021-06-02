'''
Given a 6x6 2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in arr , then print the maximum hourglass sum.
The array will always be 6x6 .
Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explaination:
The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
'''
def hourglassSum(arr):
    # Write your code here
    l = len(arr)
    sum0 = []
    sum1 = 0
    sum2 = 0
    sum3 = 0

    for i in range(l-2):

      for j in range(l-2):

          for k in range(j,l-3+j):
            sum1 += arr[i][k]
          for k in range(j+1,l-4+j):
            sum2 += arr[i+1][k]
          for k in range(j,l-3+j):
            sum3 += arr[i+2][k]
          sum0.append((sum1+sum2+sum3))
          sum1,sum2,sum3 = 0,0,0


    return max(sum0)
