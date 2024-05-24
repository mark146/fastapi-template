import uvicorn

from dataclasses import asdict
from urllib.request import Request
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from api.v1.dto.response.ApiResponse import ApiResponse
from api.v1.router_v1 import router_v1


def include_cors(app):
    origins = [
        "*",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_exception(app):
    @app.exception_handler(Exception)
    async def custom_exception_handler(request: Request, exc: Exception):
        response = ApiResponse.error(str(exc))
        return JSONResponse(
            status_code=int(response.code),
            content=asdict(response),
        )


def include_router(app):
    app.include_router(router_v1, prefix="/v1")


def start_application() -> FastAPI:
    app = FastAPI(title="template api", version="1.0")

    app.router.redirect_slashes = False
    include_cors(app)
    include_router(app)
    include_exception(app)

    return app


app = start_application()
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
