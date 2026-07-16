from fastapi import FastAPI
import platform
import socket
import psutil

app = FastAPI(
    title="AI DevOps Monitoring Dashboard",
    version="1.0.0",
    description="Monitor system metrics and analyze them using AI."
)


@app.get("/")
def root():
    return {
        "message": "THIS IS MY NEW VERSION 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/system")
def system_info():
    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.release(),
        "processor": platform.processor(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
    }