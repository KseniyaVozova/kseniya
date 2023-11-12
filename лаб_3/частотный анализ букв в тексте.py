def count_letters(text):
    slovar = {}
    for bukva in text.lower():
        if bukva.isalpha():
            slovar[bukva] = slovar.get(bukva, 0)+1
    return slovar

# TODO  Напишите функцию count_letters


def calculate_frequency(slovar1):
    slovar2 = sum(slovar1.values())
    slovar_1 = {}
    for kluch, znachenie in slovar1.items():
        chast = znachenie / slovar2
        slovar_1[kluch] = chast
    return slovar_1
# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

col_bukv = count_letters(main_str)
chast_bukv = calculate_frequency(col_bukv)
for kluch, znachenie in chast_bukv.items():
    print(f'{kluch}: {znachenie:.2f}')
# TODO Распечатайте в столбик букву и её частоту в тексте
