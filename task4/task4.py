import sys


def min_steps_to_equal(numbers):
    if not numbers:
        return 0

    total_moves = 0
    numbers.sort()
    median = numbers[len(numbers) // 2]

    for number in numbers:
        total_moves += abs(number - median)

    return total_moves


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task4.py numbers")
    else:
        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            nums = [int(line.strip()) for line in file]
            result = min_steps_to_equal(nums)
            print(f"Минимальное количество ходов: {result}")
