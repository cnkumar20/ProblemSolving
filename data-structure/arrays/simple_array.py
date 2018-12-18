import math as math
def testListFunction(input_list):
    return max(input_list)

def get_median(input_list):
    sorted_list = sorted(input_list)
    length = len(sorted_list)
    if length%2 is not 0:
        return sorted_list[math.floor(length/2)]
    else:
        print(sorted_list)
        print(sorted_list[int(length/2-1)] ," ",sorted_list[math.floor(length/2)])
        return (sorted_list[int(length/2-1)] + sorted_list[math.floor(length/2)])/2

def merge_two_list_sorted(list1,list2):
    length = len(list2)
    i=0
    j=0
    newlist =list()
    while(i < len(list1) and j < len(list2)):
        if(list1[i] <= list2[j]):
            newlist.append(list1[i])
            i = i+1
        else:
            newlist.append(list2[j])
            j = j+1
    if(i < len(list1)):
        newlist.extend(list1[i:])
    if(j < len(list2)):
        newlist.extend(list2[j:])
    return newlist

if __name__=="__main__":
    arr = [1,2,-3,4,5,6]
    print(arr[2:4])
    print(testListFunction([78,23,84,12,-18,89]))
    print(get_median([78,23,84,12,-18,89,13]))
    print(get_median([78,23,84,12,-18,89,13,11]))
    print(merge_two_list_sorted([1,2,6,8],[2,3,3,5]))
