import tkinter as tk
import psutil
import time
import sqlite3
import os
import threading

seconds = 0
running = False

# Три функции описывающие таймер по нажатию на кнопку начать запись
def update_timer():
    global seconds
    if running:
        seconds += 1
        minutes = seconds // 60
        display = f"{minutes:02}:{seconds % 60:02}"
        time_label.config(text=display)
        window.after(1000, update_timer)  

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    global running, seconds
    running = False
    seconds = 0  # Обнуляем таймер после нажатия кнопки
    time_label.config(text="00:00")

# Две функции для показа и скрытия кнопок для записи в БД
def showe_stop_button():
    start_button.pack_forget()
    stop_button.pack()
    time_label.pack()
    start_timer()
    
def showe_start_button():
    stop_button.pack_forget()
    start_button.pack()
    time_label.pack_forget()
    stop_timer()

# Функция для создания базы данных и таблицы
def create_db():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(script_dir, 'data.db'))
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_stats (
    cpu_usage REAL,
    memory REAL,
    disk REAL
)''')
    
    conn.commit()
    conn.close()

# Функция для выборки всех данных из таблицы
def fetch_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(script_dir, 'data.db'))
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM system_stats')
    records = cursor.fetchall()

    conn.close()
    
    return records

# Функция для отображения записей из таблицы 
def show_records():
    records = fetch_data()

    records_window = tk.Toplevel(window)
    records_window.title("Записи из базы данных")

    listbox = tk.Listbox(records_window, width=50)
    listbox.pack(padx=10, pady=10)

    for record in records:
        listbox.insert(tk.END, record)

    # Закрытие окна
    records_window.protocol("WM_DELETE_WINDOW", records_window.destroy)

# Функция для записи в бд
def write_to_db():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(script_dir, 'data.db'))
    cursor = conn.cursor()

    # Проверяем по событию была ли нажата кнопка стоп запись
    while not stop_event.is_set():
        cursor.execute('''
                    INSERT INTO system_stats (cpu_usage, memory, disk)
                    VALUES (?, ?, ?)
                    ''', (cpu_usage, memory_used, disk_used))
        conn.commit()
        time.sleep(int(interval_entry.get()))

    cursor.close()
    
# Функции запуска и останавки потока для записи данных в бд
def start_thread():
    showe_stop_button()
    global stop_event
    stop_event = threading.Event()
    thread = threading.Thread(target=write_to_db)
    thread.start()

def stop_thread():
    showe_start_button()
    stop_event.set()

# Обновление основного окна приложения 
def update_stats():
    global cpu_usage
    global memory_used
    global disk_used
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    cpu_label.config(text=f"ЦП: {cpu_usage}%")
    memory_label.config(text=f"ОЗУ: {memory.percent}% ({memory.used // (1024 ** 2)}MB из {memory.total // (1024 ** 2)}MB)")
    disk_label.config(text=f"ПЗУ: {disk.percent}% ({disk.used // (1024 ** 2)}MB из {disk.total // (1024 ** 2)}MB)")
    
    window.after(update_interval.get() * 1000, update_stats)   

    memory_used = memory.used // (1024 ** 2)
    disk_used = disk.used // (1024 ** 2)

# Установка интервала получения данных
def set_update_interval():
    try:
        interval = int(interval_entry.get())
        if interval > 0:
            update_interval.set(interval) 
    except ValueError:
        pass

# Создание основного окна и описание эелоементов окна
window = tk.Tk()
window.title("Монитор системных ресурсов")

update_interval = tk.IntVar(value=1)

cpu_label = tk.Label(window, text="ЦП: 0%")
cpu_label.pack()

memory_label = tk.Label(window, text="ОЗУ: 0%")
memory_label.pack()

disk_label = tk.Label(window, text="ПЗУ: 0%")
disk_label.pack()

interval_label = tk.Label(window, text="Интервал обновления (сек):")
interval_label.pack()

interval_entry = tk.Entry(window)
interval_entry.pack()
interval_entry.insert(0, "1")

set_interval_button = tk.Button(window, text="Установить интервал", command=set_update_interval)
set_interval_button.pack()

start_button = tk.Button(window, text="Начать запись", command=start_thread)
start_button.pack()

stop_button = tk.Button(window, text="Остановить запись", command=stop_thread)
stop_button.pack_forget()

time_label = tk.Label(window, text="00:00", font=("Helvetica", 48))
time_label.pack_forget()

window.title("Запись в базу данных")
create_db()

showe_db_button = tk.Button(window, text='БД', command=show_records)
showe_db_button.pack()

# Начинаем обновление
update_stats()

window.mainloop()