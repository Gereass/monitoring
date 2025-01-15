import app.interface_app as interface_app
import app.resource_monitor as resource_monitor

def set_update_stats(window):
    '''Функция для обновления отображаемых изменений'''
    def update_stats():
        cpu_usage = resource_monitor.get_cpu_usage()
        memory = resource_monitor.get_memory_usage()
        disk = resource_monitor.get_disk_usage()
        
        interface_app.cpu_label.config(text=f"ЦП: {cpu_usage}%")
        interface_app.memory_label.config(text=f"ОЗУ: {memory['percent']}% ({memory['used']}MB из {memory['total']}MB)")
        interface_app.disk_label.config(text=f"ПЗУ все: {disk['percent']}% ({disk['used']}MB из {disk['total']}MB)")
        interface_app.disk_label_write.config(text=f"Операции записи: {disk['write']}MB)")
        interface_app.disk_label_read.config(text=f"Операции чтения: {disk['read']}MB)")
        
        window.after(interface_app.update_interval.get() * 1000, update_stats)  
    
    update_stats()

def set_interval():
    '''Функцтя дя установки интервала получения данных'''
    try:
        interval = int(interface_app.interval_entry.get())
        if interval > 0:
            interface_app.update_interval.set(interval) 
    except ValueError:
        pass