import psutil

def cpu_usage(interval=None):
    return psutil.cpu_percent(interval)

if __name__ == '__main__':
    print('The current CPU Percentage in use with a given interval of 0.1 is', cpu_usage(0.1), end='%\n')
