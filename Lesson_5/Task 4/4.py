translation = {'One': 'odin', 'Two': 'dva', 'Three': 'tri', 'Four': 'chetyre'}
result = []
with open("t_file.txt") as f:
    for line in f:
        key = line.split(' - ')
        if key[0] in translation:
            word = translation[key[0]]
            result.append(word +' - '+ key[1])

with open("t_file_new.txt", 'w') as new_f:
    new_f.writelines(result)



