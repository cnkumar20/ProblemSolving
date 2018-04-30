# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
def two_sum(array_of_numbers,target):
    res = list()
    hash_map = dict()
    for x in range(len(array_of_numbers)):
        if(array_of_numbers[x] in hash_map ):
            res.append(hash_map[array_of_numbers[x]])
            res.append(x)
            return res
        hash_map[target-array_of_numbers[x]]  = x


def main():
    array_of_numbers=[2, 7, 11, 15]
    target = 9
    print(two_sum(array_of_numbers,target))
    
if __name__ == '__main__':
    main()
