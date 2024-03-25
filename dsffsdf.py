from csv import *

array = []

with open("students.csv", encoding="utf8") as file_csv:
    reader_csv = reader(file_csv)
    for el in reader_csv:
        array.append(el)
        if "Хадаров Владимир" in el[1]:
            print(f"Ты получил: {el[-1]}, за проект - {el[-3]}")

classes = ""

for el in array[1:]:
    classes += el[-2] + " "

classes = list(set(classes[:-1].split()))
classes_score_dict = {}

for el_1 in classes:
    middle_value = []
    for el_2 in array:
        if el_1 == el_2[-2] and el_2[-1] != "None":
            middle_value.append(int(el_2[-1]))
        if el_1 == el_2[-2] and el_2[-1] == "None":
            middle_value.append(0)
    classes_score_dict[el_1] = round(sum(middle_value) / len(middle_value), 3)

array_update = []

for el in array:
    change = el
    if el[-1] == "None":
        change[-1] = classes_score_dict[el[-2]]
        array_update.append(change)
    else:
        array_update.append(change)

with open("student_new.csv", "w", encoding="utf8", newline="") as file_result:
    writer = writer(file_result)
    for el in array_update:
        writer.writerow(el)