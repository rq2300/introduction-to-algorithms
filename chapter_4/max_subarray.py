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
    for i in range(mid + 1, high):
        current_sum += a[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i

    return (max_left, max_right, left_sum + right_sum)


if __name__ == "__main__":
    price_change = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(find_max_crossing_subarray(price_change, 0, len(price_change) // 2, len(price_change)))