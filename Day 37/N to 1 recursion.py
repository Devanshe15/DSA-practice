def print_numbers(n):
    if n <= 0:
        return
    print(n)
    print_numbers(n - 1)
n = int(input('enter the no.'))
print_numbers(n)
