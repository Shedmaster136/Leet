import random

def sortrange(sort_arr: list[int]) -> list[int]:
    for i in range(len(sort_arr)):
        for j in range(len(sort_arr)):
            if i==j:
                continue
            if sort_arr[i] < sort_arr[j]:
                swap_buf = sort_arr[j]
                sort_arr[j] = sort_arr[i]
                sort_arr[i] = swap_buf
    return sort_arr
1

if __name__ == '__main__':
    RangeFrom = 0
    RangeTo = 0
    SortArr = []
    RangeLen = 0
    RangeLen = int(input('Input the length of the sorted array '))
    if RangeLen == 0:
        print('Range Length cannot be 0')
        exit()
    RangeFrom = int(input('Input the start of the range '))
    RangeTo = int (input('Input the end of the range '))
    if RangeFrom >= RangeTo:
        print('Range cannot be made')
        exit()
    for i in range(RangeLen):
        SortArr.append(random.randint(RangeFrom,RangeTo))
    print("Unsorted array:" + str(SortArr))
    print("Sorted array: " + str(sortrange(SortArr)))
    


