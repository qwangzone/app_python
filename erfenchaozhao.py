def bin_search(data_list, val):
    low = 0                         # 最小数下标
    high = len(data_list) - 1       # 最大数下标
    while low <= high:
        mid = (low + high) // 2     # 中间数下标
        print(mid)
        if data_list[mid] == val:   # 如果中间数下标等于val, 返回
            return mid
        elif data_list[mid] > val:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:                       # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return "不存在"                  # val不存在, 返回None
ret = bin_search([1, 2,3,4,5,6,7,8,9,10], 10)
print(ret)