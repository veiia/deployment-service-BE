import uvicorn
from fastapi import FastAPI

from app.api.v1.container import containers_router
from app.api.v1.manage import manage_router

app = FastAPI()

app.include_router(manage_router)
app.include_router(containers_router)


@app.on_event("startup")
async def startup() -> None:
    pass


@app.on_event("shutdown")
async def shutdown() -> None:
    pass


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", host="0.0.0.0", port=8088, log_level="info", reload=True
    )
