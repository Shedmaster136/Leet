import random
def initarrayunique() -> list[int]:
    range_from = 0
    range_to = 0
    init_arr = []
    range_len = 0
    range_len = int(input('Input the length of the array '))
    if range_len == 0:
        print('Range Length cannot be 0')
        exit()
    range_from = int(input('Input the start of the range '))
    range_to = int (input('Input the end of the range '))
    if range_from >= range_to:
        print('Range cannot be made')
        exit()
    if range_to - range_from < range_len :
        print('Not enough values to fill the range')
    init_arr = random.sample(range(range_from, range_to), range_len)
    return init_arr


if __name__ == '__main__':
    nums = initarrayunique()
    print(nums)
    target = int(input())
    hashmap = {}
    for i, num in enumerate(nums):
        if (target - num in hashmap):
            print(hashmap[target-num], i)
        else:
            hashmap[num] = i

