"""
Algorithm
1. Initialize a 3x3 2d array
2. Passed it as an argument for a function to find the maximum value
3. Initialize a variable that will contain the current max value
4. Outer loop will access the rows while inner loop will compare elements inside the row
5. Outer loop will have 3 iterations until it finishes and returns the max value
6. The returned value gets printed

Pseudocode
START
    function(arr)
    {
        max = 0
        for (int i = 0; i < arr.length; i++)
        {
            for (int j = 0; j < arr[i].length; j++)
                if arr[i][j] > max_value
                    max = arr[i][j]
        }
    }
    
    two_d = [[1,2,3], [4,5,6], [7,8,9]]
    print(findMax(two_d))
END    
"""

def findMax(arr):
    max_val = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > max_val:
                max_val = arr[i][j]  

    return max_val        
        
    
twoD_arr = [[50, 60, 70], [1, 2, 3], [45,67,89]]

print("3D array:", twoD_arr)
print("Maximum value is:", findMax(twoD_arr))
