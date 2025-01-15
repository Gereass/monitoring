import app.interface_app as interface_app

seconds = 0
running = False

def showe_stop_button():
    '''изменение видимости кнопки Остановить запись'''
    interface_app.start_button.pack_forget()
    interface_app.stop_button.pack()
    interface_app.time_label.pack()
    start_timer()
    
def showe_start_button():
    '''изменение видимости кнопки Начать запись'''
    interface_app.stop_button.pack_forget()
    interface_app.start_button.pack()
    interface_app.time_label.pack_forget()
    stop_timer()

def update_timer():
    '''Обновление секундомера'''
    global seconds
    if running:
        seconds += 1
        minutes = seconds // 60
        display = f"{minutes:02}:{seconds % 60:02}"
        interface_app.time_label.config(text=display)
        interface_app.window.after(1000, update_timer)  

def start_timer():
    '''Запуск секундомера'''
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    '''Остановка секундомера'''
    global running, seconds
    running = False
    seconds = 0 
    interface_app.time_label.config(text="00:00")