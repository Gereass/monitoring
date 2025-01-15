import sqlite3
import os
import tkinter as tk
import time
import threading
import app.interface_app as interface_app
import app.resource_monitor as resource_monitor

from app.timer_work import showe_stop_button, showe_start_button


def create_db():
    '''Функция для создания базы данных и таблицы''' 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(script_dir, 'data.db'))
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_stats (
    cpu_usage REAL,
    memory REAL,
    disk_all REAL,
    disk_io_write REAL,
    disk_io_read REAL
    )''')
    
    conn.commit()
    conn.close()

def fetch_data():
    '''Функция для поиска всех записей в БД'''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(script_dir, 'data.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM system_stats')
    records = cursor.fetchall()
    conn.close()

    return records

def show_records():
    '''Функция для вывода всех записей в БД'''
    records = fetch_data()

    records_window, listbox = interface_app.list_records()

    for record in records:
        listbox.insert(tk.END, record)

    # Закрытие окна
    records_window.protocol("WM_DELETE_WINDOW", records_window.destroy)

def write_to_db():
    '''Функция для записи в бд'''
    script_dir = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(os.path.join(script_dir, 'data.db'))
    cursor = conn.cursor()

    '''Проверка события нажатия кнопка остановить запись'''
    while not stop_event.is_set():
        cpu = resource_monitor.get_cpu_usage()
        memory = resource_monitor.get_memory_usage()
        disk = resource_monitor.get_disk_usage()
        cursor.execute('''
                    INSERT INTO system_stats (cpu_usage, memory, disk_all, disk_io_write, disk_io_read)
                    VALUES (?, ?, ?, ?, ?)
                    ''', (cpu, memory['used'], disk['used'], disk['write'], disk['read']))
        conn.commit()
        time.sleep(int(interface_app.interval_entry.get()))

    cursor.close()

def start_thread():
    '''Функции запуска потока для записи данных в БД'''
    showe_stop_button()
    global stop_event
    stop_event = threading.Event()
    thread = threading.Thread(target=write_to_db)
    thread.start()

def stop_thread():
    '''Функции остановки потока для записи данных в БД'''
    showe_start_button()
    stop_event.set()
        