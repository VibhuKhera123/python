def add_matrices(matrix_a, matrix_b):
  if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
    raise ValueError("The two matrices must have the same dimensions.")

  result = []
  for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[0])):
      row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

  return result


def main():
  # Get the dimensions of the matrices from the user.
  rows = int(input("Enter the number of rows: "))
  columns = int(input("Enter the number of columns: "))

  # Get the elements of the first matrix from the user.
  matrix_a = []
  for i in range(rows):
    row = []
    for j in range(columns):
      num = int(input("Enter the element at row {} column {}: ".format(i + 1, j + 1)))
      row.append(num)
    matrix_a.append(row)

  # Get the elements of the second matrix from the user.
  matrix_b = []
  for i in range(rows):
    row = []
    for j in range(columns):
      num = int(input("Enter the element at row {} column {}: ".format(i + 1, j + 1)))
      row.append(num)
    matrix_b.append(row)

  # Add the two matrices and print the result.
  sum_matrix = add_matrices(matrix_a, matrix_b)
  print("The sum of the two matrices is:")
  for row in sum_matrix:
    print(row)


if __name__ == "__main__":
  main()
