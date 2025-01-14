import tkinter as tk
import work_on_interfeis
import database

def list_records():
    records_window = tk.Toplevel(window)
    records_window.title("Записи из базы данных")
    
    listbox = tk.Listbox(records_window, width=50 )
    listbox.pack(padx=10, pady=10)

    return records_window, listbox

def run_interfeis():
    work_on_interfeis.set_update_stats(window)
    window.mainloop()

# Работа с интерфейсом приложения
window = tk.Tk()
window.title("Монитор системных ресурсов")

cpu_label = tk.Label(window, text="ЦП: 0%")
cpu_label.pack()

memory_label = tk.Label(window, text="ОЗУ: 0%")
memory_label.pack()

disk_label = tk.Label(window, text="ПЗУ: 0%")
disk_label.pack()

disk_label_read = tk.Label(window, text="Операции записи: МБ")
disk_label_read.pack()

disk_label_write = tk.Label(window, text="Операции чтения: МБ")
disk_label_write.pack()
    
update_interval = tk.IntVar(value=1)
interval_entry = tk.Entry(window)
interval_entry.pack()
interval_entry.insert(0, "1")  

set_interval_button = tk.Button(window, text="Установить интервал", \
                                command=lambda: work_on_interfeis.set_interval())
set_interval_button.pack()   

start_button = tk.Button(window, text="Начать запись",\
                          command=lambda: database.start_thread())
start_button.pack()

stop_button = tk.Button(window, text="Остановить запись",\
                        command=lambda: database.stop_thread())
stop_button.pack_forget()

show_db_button = tk.Button(window, text='БД',\
                        command=lambda: database.show_records())
show_db_button.pack()

time_label = tk.Label(window, text="00:00", font=("Helvetica", 48))
time_label.pack_forget()