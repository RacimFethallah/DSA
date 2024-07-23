def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map = {}
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    for c in sorted_s:
        map[c] = map.get(c, 0) + 1
    for c in sorted_t:
        if c not in map or map[c] == 0:
            return False
        map[c] -= 1

    return True


if __name__ == "__main__":
    s = "aacc"
    t = "ccac"
    isAnagram(s, t)

