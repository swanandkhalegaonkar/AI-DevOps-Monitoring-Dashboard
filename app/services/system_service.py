import platform
import socket
import psutil


def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)


def get_system_info():

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    return {

        "hostname": socket.gethostname(),

        "operating_system": platform.system(),

        "os_version": platform.release(),

        "processor": platform.processor(),

        "cpu": {

            "usage_percent": psutil.cpu_percent(interval=1),

            "physical_cores": psutil.cpu_count(logical=False),

            "logical_cores": psutil.cpu_count(logical=True)

        },

        "memory": {

            "total_gb": bytes_to_gb(memory.total),

            "used_gb": bytes_to_gb(memory.used),

            "available_gb": bytes_to_gb(memory.available),

            "usage_percent": memory.percent

        },

        "disk": {

            "total_gb": bytes_to_gb(disk.total),

            "used_gb": bytes_to_gb(disk.used),

            "free_gb": bytes_to_gb(disk.free),

            "usage_percent": disk.percent

        }

    }