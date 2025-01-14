import update_interface 
import interface_app 

seconds = 0
running = False

# Две функции для показа и скрытия кнопок для записи в БД
def showe_stop_button():
    interface_app.start_button.pack_forget()
    interface_app.stop_button.pack()
    interface_app.time_label.pack()
    start_timer()
    
def showe_start_button():
    interface_app.stop_button.pack_forget()
    interface_app.start_button.pack()
    interface_app.time_label.pack_forget()
    stop_timer()

# Три функции описывающие таймер по нажатию на кнопку "начать запись"
def update_timer():
    global seconds
    if running:
        seconds += 1
        minutes = seconds // 60
        display = f"{minutes:02}:{seconds % 60:02}"
        interface_app.time_label.config(text=display)
        interface_app.window.after(1000, update_timer)  

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    global running, seconds
    running = False
    seconds = 0  # Обнуляем таймер после нажатия кнопки
    interface_app.time_label.config(text="00:00")