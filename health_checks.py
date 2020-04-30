import shutil
import psutil
from network import *

def check_disk(disk):
    du=shutil.disk_usage(disk)
    df=du.free/du.total *100
    return df >20

def check_cpu():
    use=psutil.cpu_percent(1)
    return use <75


if not check_disk("/") or not check_cpu():
    print("error")
elif check_localhost() and check_connectivity():
    print("okay")
else :
    print("net fail")