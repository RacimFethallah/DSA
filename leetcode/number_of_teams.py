def numTeams(rating) -> int:
    output = 0
    n = len(rating)
    for j in range(n):
        right_smaller = 0
        right_bigger = 0
        left_smaller = 0
        left_bigger = 0

        for i in range(j):
            if rating[i] < rating[j]:
                left_smaller += 1
            if rating[i] > rating[j]:
                left_bigger += 1

        for i in range(j + 1, n):
            if rating[i] > rating[j]:
                right_bigger += 1
            if rating[i] < rating[j]:
                right_smaller += 1

        if right_smaller > 1:
            output += right_smaller - 1
        if right_bigger > 1:
            output += right_bigger - 1

    return output


if __name__ == "__main__":
    rating = [2, 5, 3, 4, 1]
    print(numTeams(rating))
