# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    xx = sum(item["score"] * item["weight"] for item in data)
    yy = round(xx, 3)
    return yy

print(task())
