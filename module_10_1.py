import threading
from time import sleep, time

def format_time(seconds):
    """Форматируем время в формате часы:минуты:секунды.милисекунды."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds - int(seconds)) * 1000000)  # Для получения микросекунд
    return f"{hours:02}:{minutes:02}:{int(seconds):02}.{milliseconds:06}"

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # пауза на 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
start_time = time()

# Вызовы функции без потоков
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
end_time = time()
print(f"Работа без потоков: {format_time(end_time - start_time)}")

# Взятие текущего времени для потоков
start_time_threads = time()

# Настройка потоков
threads = []
file_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for args in file_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения работы потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_time_threads = time()
print(f"Работа с потоками: {format_time(end_time_threads - start_time_threads)}")