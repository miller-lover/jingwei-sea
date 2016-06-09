with open('D:/workspace/dive-into-python/chinese.txt', encoding='utf-8') as a_file:
   a_file.seek(17)
   a_character = a_file.read(1)
   print(a_character)
