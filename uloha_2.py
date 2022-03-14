def line_counter (path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    count_lines = text.count("\n") + 1
    return count_lines

result = line_counter("/Users/nicolgotzova/Documents/Ukoly/Data/data2.txt")
print (result)
