# TODO импортировать необходимые молули
import csv
import json

INPUT = "input.csv"
OUTPUT = "output.json"


def task() -> None:
    with open(INPUT) as f:
        lines = [line for line in csv.DictReader(f)]

    with open(OUTPUT, "w") as f:
        json.dump(lines, f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT) as output_f:
        for line in output_f:
            print(line, end="")
