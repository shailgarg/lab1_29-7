def get_matrix_input(name):
    print(f"Enter the number of rows and columns for matrix {name}:")
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    
    matrix = []
    print(f"Enter the elements of matrix {name}, one by one:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Element [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    
    return matrix, rows, cols

def multiply_matrices(a, a_rows, a_cols, b, b_rows, b_cols):
    if a_cols != b_rows:
        return None 
    
   
    result = [[0] * b_cols for _ in range(a_rows)]
    
    
    for i in range(a_rows):
        for j in range(b_cols):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(a_cols))
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    print("Matrix A:")
    a, a_rows, a_cols = get_matrix_input("A")
    
    print("Matrix B:")
    b, b_rows, b_cols = get_matrix_input("B")
    
    if a_cols != b_rows:
        print("Matrices cannot be multiplied due to incompatible dimensions.")
        return
    
    product = multiply_matrices(a, a_rows, a_cols, b, b_rows, b_cols)
    
    print("Product of matrices A and B:")
    print_matrix(product)

if __name__ == "__main__":
    main()
