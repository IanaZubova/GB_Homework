new_file = open ("file_w_numbers.txt", 'r+')
new_file.write("13 56 32 11 18")

for i in new_file:
    value = i.split(' ')

    print(sum(map(int, value)))


new_file.close()