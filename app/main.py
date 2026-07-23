from fastapi import FastAPI
from h11 import Request
from app.routers.health import router as health_router
from app.routers.system import router as system_router
from app.routers.metrics import router as metrics_router
from time import time
from app.logger import logger
from app.config import APP_NAME, APP_VERSION
from app.services.metrics_service import REQUEST_COUNT, REQUEST_DURATION
import time


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
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status={response.status_code} | "
        f"Duration={process_time:.3f}s"
    )

    REQUEST_COUNT.inc()

    REQUEST_DURATION.observe(process_time)

    return response