def transpose(matrix):
   
    rows = len(matrix)
    cols = len(matrix[0])
    
  
    transposed = [[0] * rows for _ in range(cols)]
    
 
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def get_matrix_input():
 
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
   
    matrix = []
    
   
    for i in range(rows):
        while True:
            try:
                
                row = list(map(int, input(f"Enter row {i + 1} ").strip().split(',')))
                if len(row) != cols:
                    print(f"Error: Row {i + 1} must have exactly {cols} columns. Try again.")
                else:
                    matrix.append(row)
                    break
            except ValueError:
                print("Invalid input. Please enter integer values separated by commas.")
    
    return matrix

# Main program
matrix = get_matrix_input()

if matrix:
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    transposed_matrix = transpose(matrix)

    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)
