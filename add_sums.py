# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def solution( nums, target):
    result=[]
    for i in range(len(nums)):
        for j in range(len(nums)):

            if i == j:
                continue

            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result
            if nums[i] + nums[j] > target:
                break


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print(solution(nums, target))

