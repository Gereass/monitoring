import interfeis_app
import resource_monitor

def set_update_stats(window):
    def update_stats():
        cpu_usage = resource_monitor.get_cpu_usage()
        memory = resource_monitor.get_memory_usage()
        disk = resource_monitor.get_disk_usage()
        
        interfeis_app.cpu_label.config(text=f"ЦП: {cpu_usage}%")
        interfeis_app.memory_label.config(text=f"ОЗУ: {memory['percent']}% ({memory['used']}MB из {memory['total']}MB)")
        interfeis_app.disk_label.config(text=f"ПЗУ все: {disk['percent']}% ({disk['used']}MB из {disk['total']}MB)")
        interfeis_app.disk_label_write.config(text=f"Операции записи: {disk['write']}MB)")
        interfeis_app.disk_label_read.config(text=f"Операции чтения: {disk['read']}MB)")
        
        window.after(interfeis_app.update_interval.get() * 1000, update_stats)  
    
    update_stats()

# Установка интервала получения данных
def set_interval():
    try:
        interval = int(interfeis_app.interval_entry.get())
        if interval > 0:
            interfeis_app.update_interval.set(interval) 
    except ValueError:
        pass