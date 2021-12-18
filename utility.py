import os

def read_file(file_name, extension):
    with open(file_name+"."+extension, newline="") as f:
        data = f.readlines()
        return data

def clearConsole():
    command = 'clear' # for linux
    if os.name in ('nt', 'dos'):
        command = 'cls' # for windows
    os.system(command)