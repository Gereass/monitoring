import psutil

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    memory = psutil.virtual_memory()
    return {'percent' : memory.percent, 'used' : memory.used // (1024 ** 2), 'total' : memory.total // (1024 ** 2)}

def get_disk_usage():
    disk_all = psutil.disk_usage('/')
    disk_io = psutil.disk_io_counters(perdisk=False)
    return {'percent' : disk_all.percent,  'used' : disk_all.used // (1024 ** 2), \
            'total' : disk_all.total // (1024 ** 2), 'read' : disk_io.read_bytes  // (1024 ** 2),  'write' : disk_io.write_bytes  // (1024 ** 2)}