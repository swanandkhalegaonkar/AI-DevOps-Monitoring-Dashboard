from fastapi import FastAPI


from app.routers.health import router as health_router
from app.routers.system import router as system_router
from time import time
from app.logger import logger
from app.routers.metrics import router as metrics_router
from app.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Monitor system metrics and analyze them using AI."
)

app.include_router(health_router)
app.include_router(system_router)
app.include_router(metrics_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI DevOps Monitoring Dashboard 🚀"
    }

@app.middleware("http")
async def log_requests(request, call_next):

    start = time()

    response = await call_next(request)

    duration = round(time() - start, 3)

    logger.info(
        "%s %s | Status=%s | Duration=%ss",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response   