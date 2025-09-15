import os
import subprocess

# запускаем утилиту
res = subprocess.run("driverquery", capture_output=True, text=True, encoding="cp866")

# создается новый файл с результатами запуска
try:
    with open("driverquery-output.txt", "w", encoding="utf-8") as f:
        f.write(res.stdout)
except FileNotFoundError:
    print("Файл не найден")
except OSError:
    print("Ошибка операционной системы")
except UnicodeDecodeError:
    print("Ошибка кодирования текста")
except Exception as e:
    print(e)

# из нового файла выводятся только строки где есть тип драйверов File System
try:
    with open("driverquery-output.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            if "File System" in line:
                print(line, end="")
except Exception as e:
    print(e)


