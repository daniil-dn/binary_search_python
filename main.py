def naive_search(lt, target):
    # example = [1, 3, 10, 12, 15]
    for i in range(len(lt)):
        if lt[i] == target:
            return i
    return -1
