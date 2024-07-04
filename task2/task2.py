import sys
import math


def read_circle_data(path):
    with open(path, "r") as file:
        data = file.read()
        centre_x, centre_y = map(int, data[:2])
        radius = int(data[3])
    return (centre_x, centre_y), radius


def read_points_data(path):
    with open(path, "r") as file:
        data = file.readlines()
        points_list = []
        for line in data:
            x, y = map(int, line[:2])
            points_list.append((x, y))
        return points_list


def point_position(center, radius, point):
    distance = math.sqrt((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2)
    if distance > radius:
        return 2
    elif distance < radius:
        return 1
    else:
        return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py circle points")
    else:
        circle_file = sys.argv[1]
        points_file = sys.argv[2]

        centre, radius = read_circle_data(circle_file)
        points = read_points_data(points_file)

        for point in points:
            position = point_position(centre, radius, point)
            print(position)
