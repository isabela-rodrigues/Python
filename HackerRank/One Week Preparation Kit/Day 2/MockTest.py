def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0
    
    for i in range(n):
        for j in range(n):

            top_left = matrix[i][j]
            top_right = matrix[i][2 * n - j - 1]
            bottom_left = matrix[2 * n - i - 1][j]
            bottom_right = matrix[2 * n - i - 1][2 * n - j - 1]
            
            max_value = max(top_left, top_right, bottom_left, bottom_right)
            
            max_sum += max_value
    
    return max_sum