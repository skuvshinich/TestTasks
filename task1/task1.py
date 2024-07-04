import sys


def circ_array_path(n, m):
    circ_array = list(range(1, n + 1))
    way = ""

    index = 0
    while True:
        way += str(circ_array[index])
        index += m-1
        index %= len(circ_array)
        if index == 0:
            break
    return way


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python task1.py n m")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        result = circ_array_path(n, m)
        print(result)