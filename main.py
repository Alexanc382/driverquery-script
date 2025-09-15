import os
import subprocess

# запускаем утилиту
res = subprocess.run("driverquery", capture_output=True, text=True, encoding="cp866")
print(res.stdout)

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



