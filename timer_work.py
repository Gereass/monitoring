import work_on_interfeis as work_on_interfeis
import interfeis_app

seconds = 0
running = False

# Две функции для показа и скрытия кнопок для записи в БД
def showe_stop_button():
    interfeis_app.start_button.pack_forget()
    interfeis_app.stop_button.pack()
    interfeis_app.time_label.pack()
    start_timer()
    
def showe_start_button():
    interfeis_app.stop_button.pack_forget()
    interfeis_app.start_button.pack()
    interfeis_app.time_label.pack_forget()
    stop_timer()

# Три функции описывающие таймер по нажатию на кнопку "начать запись"
def update_timer():
    global seconds
    if running:
        seconds += 1
        minutes = seconds // 60
        display = f"{minutes:02}:{seconds % 60:02}"
        interfeis_app.time_label.config(text=display)
        interfeis_app.window.after(1000, update_timer)  

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    global running, seconds
    running = False
    seconds = 0  # Обнуляем таймер после нажатия кнопки
    interfeis_app.time_label.config(text="00:00")