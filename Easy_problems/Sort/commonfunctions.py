import random
def initarray() -> list[int]:
    range_from = 0
    range_to = 0
    init_arr = []
    range_len = 0
    range_len = int(input('Input the length of the sorted array '))
    if range_len == 0:
        print('Range Length cannot be 0')
        exit()
    range_from = int(input('Input the start of the range '))
    range_to = int (input('Input the end of the range '))
    if range_from >= range_to:
        print('Range cannot be made')
        exit()
    for i in range(range_len):
        init_arr.append(random.randint(range_from,range_to))
    return init_arr