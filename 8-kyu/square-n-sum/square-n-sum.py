def square_sum(numbers):
    new_arr = []
    for each in numbers:
        new_num = each**2
        new_arr.append(new_num)
    return sum(new_arr)