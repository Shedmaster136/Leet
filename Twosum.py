import random
RangeFrom = 0
RangeTo = 0
SortArr = []
RangeLen = 0
RangeLen = int(input('Input the length of the sorted array'))
if RangeLen == 0:
    print('Range Length cannot be 0')
    exit()
RangeFrom = int(input('Input the start of the range'))
RangeTo = int (input('Input the end of the range'))
if RangeFrom >= RangeTo:
    print('Range cannot be made')
    exit()
for i in range(RangeLen):
    SortArr.append(random.randint(RangeFrom,RangeTo))
print(SortArr)
