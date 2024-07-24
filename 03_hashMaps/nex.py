# most frequent numbers
def topKFrequent(nums, k: int):
    result = []
    frequence = {}
    for n in nums:
        frequence[n] = frequence.get(n, 0) + 1

    newf = dict(sorted(frequence.items(), key=lambda item: item[1], reverse=True))
    preresult = list(newf.keys())
    for i in range(k):
        result.append(preresult[i])

    return result


if __name__ == "__main__":
    nums = [3, 0, 1, 0]
    k = 2
    result = topKFrequent(nums, k)
