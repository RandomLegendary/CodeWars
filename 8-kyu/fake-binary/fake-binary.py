def fake_bin(x):
    arr = list(x)
    for each in arr:
        each_int = int(each)
        if each_int < 5:
            place = arr.index(each)
            arr[place] = 0
        else:
            place = arr.index(each)
            arr[place] = 1
            
    print(arr)
    return "".join(str(x) for x in arr)