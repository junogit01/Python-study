import kor_to_eng

name_list = []
with open("kor_names.txt", 'r', encoding='utf-8') as f:
    for line in f:
        name_list.append(line.strip())

name_list = [kor_to_eng.kor2eng(name) for name in name_list]

with open("eng_names.txt", 'w', encoding='utf-8') as f:
    for name in name_list:
        f.write(name + '!@#\n')