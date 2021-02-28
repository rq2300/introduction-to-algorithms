def find_max_crossing_subarray(a: list, low: int, mid: int, high: int) -> tuple:
    left_sum = -1000
    max_left = mid
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += a[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i

    right_sum = -1000
    max_right = mid + 1
    current_sum = 0
    for i in range(mid + 1, high + 1):
        current_sum += a[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i

    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(a: list, low: int, high: int) -> tuple:
    """
    Divide and Conquer approach with running time of T(n) = 2T(n/2) + O(n) = O(n lg n) (lg = log of base 2)
    """
    if low == high:  # Base case
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(a, low, mid)
        right_low, right_high, right_sum = find_max_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def find_max_subarray_linear(a: list) -> tuple:
    """
    Non Divide and Conquer approach and no recursion. Running time of T(n) = O(n).
    Exercise 4.1-5
    """

    left = right = max_left = max_right = 0
    max_sum = 0
    current_sum = 0
    while right != len(a):
        if current_sum <= 0:
            left = right
            current_sum = a[right]
        else:
            current_sum += a[right]

        if current_sum > max_sum:
            max_sum = current_sum
            max_left = left
            max_right = right

        right += 1
    return (max_left, max_right, max_sum)


if __name__ == "__main__":
    # price_change = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    price_change = [
        -62,
        -60,
        -68,
        -28,
        -22,
        -41,
        -8,
        -11,
        -61,
        62,
        -70,
        -4,
        90,
        -79,
        59,
        -55,
        76,
        -95,
        95,
        -98,
        99,
        100,
        84,
        68,
        -76,
        75,
        97,
        -93,
        19,
        46,
    ]
    print(
        "Divide and Conquer approach:",
        find_max_subarray(price_change, 0, len(price_change) - 1),
    )
    print("Linear approach (sliding window):", find_max_subarray_linear(price_change))
