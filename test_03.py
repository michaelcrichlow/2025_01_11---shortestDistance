def shortestDistance(s: str, char: str) -> list[int]:
    # guard clase
    if char not in s:
        raise Exception(f"ERROR: The char {char} is not in the string {s}.")

    local_array: list[int] = []
    search_distance = 0
    check_in_front = True
    check_behind = True

    for i in range(len(s)):
        # reset variables every loop
        search_distance = 0
        check_in_front = True
        check_behind = True

        while True:
            if i + search_distance >= len(s):
                check_in_front = False
            if i - search_distance < 0:
                check_behind = False

            if check_in_front:
                if s[i + search_distance] == char:
                    local_array.append(search_distance)
                    break
            if check_behind:
                if s[i - search_distance] == char:
                    local_array.append(search_distance)
                    break

            search_distance += 1

    return local_array


def main() -> None:
    print(shortestDistance('loveleetcode', 'e'))


if __name__ == '__main__':
    main()

# shortestDistance('loveleetcode', 'e') =>  [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#                                           [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
