def multiples_of_seven(start, end):
    for num in range(start, end + 1):
        if num == 28:
            continue
        if num % 7 == 0:
            print(num)
multiples_of_seven(1, 50)