import json
import sys


def read_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def create_values_dict(values_json):
    values_dictionary = {item['id']: item['value'] for item in values_json['values']}
    return values_dictionary


def fill_values(dictionary, tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = dictionary[test_id]
        if 'values' in test:
            fill_values(dictionary, test['values'])


def write_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py values tests report")
    else:
        values_file = sys.argv[1]
        tests_file = sys.argv[2]
        report_file = sys.argv[3]

        values_data = read_json(values_file)
        tests_data = read_json(tests_file)

        values_dict = create_values_dict(values_data)

        fill_values(values_dict, tests_data["tests"])

        write_json(tests_data, report_file)
