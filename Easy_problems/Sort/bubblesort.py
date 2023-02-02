from . import commonfunctions

def sortrange(sort_arr: list[int]) -> list[int]:
    for i in range(len(sort_arr)-1):
        for j in range(i+1, len(sort_arr)):
            if sort_arr[i] < sort_arr[j]:
                swap_buf = sort_arr[j]
                sort_arr[j] = sort_arr[i]
                sort_arr[i] = swap_buf
    return sort_arr



if __name__ == '__main__':
    sort_arr = commonfunctions.initarray()
    print("Unsorted array:" + str(sort_arr))
    print("Sorted array: " + str(sortrange(sort_arr)))
    


