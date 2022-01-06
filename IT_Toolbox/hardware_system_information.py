#!/bin/python3

import psutil
import platform
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Convert bytes to a proper, human-readable format, e.g.
    bytes to megabytes(MB) or bytes to gigabytes(GB)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

print('='*40, "System Information", "="*40)
uname = platform.uname();
print(f"System: {uname}")
print(f"Node: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Boot Time
print('='*40, "Boot Time", '='*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# CPU Info
print('='*40, "CPU Info", '='*40)
## Number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))

# CPU Frequencies
cpufreq = psutil.cpu_freq()
print(f"Max frequency: {cpufreq.max:.2f}Mhz")
print(f"Min frequency: {cpufreq.min:.2f}Mhz")
print(f"Current frequency: {cpufreq.current:.2f}Mhz")

# CPU Usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"\tCore {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# Memory Information
print(f"="*40, "Memory Information", "="*40)
## get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
## get the swap memory details
print('='*40, "Swap", '='*40)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")

# Disk Information
print('='*40, "Disk Information",'='*40)
## get all disk partitions
print("Partitions and Usage:")
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"\tMountpoint: {partition.mountpoint}")
    print(f"\tFilesystem Type: {partition.fstype}")
    
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        pass

    print(f"\tTotal Size: {get_size(partition_usage.total)}")
    print(f"\tUsed: {get_size(partition_usage.used)}")
    print(f"\tFree: {get_size(partition_usage.free)}")
    print(f"\tPercentage: {partition_usage.percent}%")
## get IO statistics for boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

# Network Information
print('='*40, "Network Information", '='*40)
## get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == "AddressFamily.AF_INET":
            print(f"\tIP Address: {address.address}")
            print(f"\tNetmask: {address.netmask}")
            print(f"\tBroadcast IP: {address.broadcast}")
        elif str(address.family) == "Address.Family.AF_PACKET":
            print(f"\tMac Address: {address.address}")
            print(f"\tNetmask: {address.netmask}")
            print(f"\tBroadcast MAC: {address.broadcast}")
## get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total bytes sent: {get_size(net_io.bytes_sent)}")
print(f"Total bytes received: {get_size(net_io.bytes_recv)}")
