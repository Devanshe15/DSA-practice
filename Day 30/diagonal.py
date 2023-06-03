def find_diagonal_numbers(matrix, queries):
    diagonal_numbers = []
    n = len(matrix)
    
    for query in queries:
        x = query
        found = False
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == x:
                    diagonal_numbers.append(i + j + 1)
                    found = True
                    break
            if found:
                break
        if not found:
            diagonal_numbers.append(-1)
    
    return diagonal_numbers

n = int(input("Enter the number of rows: "))
q = int(input("Enter the number of queries: "))

matrix = []
for _ in range(n):
    row = list(map(int, input("Enter the values for a row: ").split()))
    matrix.append(row)

queries = []
for _ in range(q):
    query = int(input("Enter a query value: "))
    queries.append(query)

diagonal_nums = find_diagonal_numbers(matrix, queries)

print("Diagonal numbers:")
for num in diagonal_nums:
    print(num)