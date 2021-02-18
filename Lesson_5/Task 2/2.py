with open("text_file.txt") as text_file:
    number_lines = 0
    for lines in text_file:
        number_lines += 1

        flag = 0
        words = 0
        for el in lines:
            if el != ' ' and flag == 0:
                words += 1
                flag = 1
            elif el == ' ':
                flag = 0
        print(f"Number of words: {words}")

print(f"Number of lines in the file: {number_lines}")





