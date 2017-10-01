import os.path, time
from datetime import date, datetime

name_of_file = 'example.txt'
defined_line = 'tytur'
defined_date = 1392965229.0

creation_date = os.stat(name_of_file).st_birthtime
print(time.ctime(creation_date), '\n')

if creation_date - defined_date > 0:
    f = open(name_of_file, 'r')
    file = f.read().split("\n")
    f.close()
    print(file, '\n')
    neighbors = ""

    for str in file:
        check = str.find(defined_line)
        if check != -1:
            line_number = file.index(str)
            full_name = os.path.abspath(name_of_file)

            if line_number == 0:
                neighbors += file[line_number + 1] + " " + file[line_number + 2]
            elif line_number == file.count:
                neighbors += file[line_number - 2] + " " + file[line_number - 1]
            else:
                neighbors += file[line_number - 2] + " " + file[line_number - 1] + " / "
                neighbors += file[line_number + 1] + " " + file[line_number + 2]

            print("\n Полное имя файла: ", full_name, "\n",
                  "Дата создания файла: ", time.ctime(creation_date), "\n",
                  "Номер строки: ", line_number + 1, "\n",
                  "Содержимое этой строки: ", file[line_number], "\n",
                  "Содержимое соседних строк: ", neighbors, "\n"
                  )

        else:
            print("Совпадения в строке ", str, " не найдены!")






