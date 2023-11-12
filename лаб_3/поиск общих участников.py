def find_common_participants(a, b, c=','):
    a1 = set(a.split(c))
    b1 = set(b.split(c))
    ab = sorted(a1.intersection(b1))
    return ab
    # TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result=find_common_participants(participants_first_group,participants_second_group,'.')
print(result)# TODO Провеьте работу функции с разделителем отличным от запятой
