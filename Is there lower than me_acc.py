def lower_than_me(array):
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            return True
    return False

arr = input()
eval_arr = eval(arr)
result = lower_than_me(eval_arr)
print(result)
