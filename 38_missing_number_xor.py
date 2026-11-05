def missing_number(numbers):
    n = len(numbers)
    result = n

    for i in range(n):
        result ^= i ^ numbers[i]

    return result