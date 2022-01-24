def line_counter (path_to_file):
    file_open = open (path_to_file)
    text = file_open.read()
    file_open.close()
    count_lines = text.count("\n") + 1
    return count_lines

result = line_counter("/Users/nicolgotzova/Documents/Ukoly/Data/data2.txt")
print (result)
