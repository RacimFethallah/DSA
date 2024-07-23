
def containsDuplicate(nums):
        numbers = {}

        for n in nums:
            if n in numbers:
                numbers[n] += 1
            else:
                numbers[n] = 1

        for n in numbers:
            if numbers[n] > 1:
                return True
            else:
                return False



if __name__ == '__main__':
     nums = [2,14,18,22,22]
     containsDuplicate(nums)