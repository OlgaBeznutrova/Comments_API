from fastapi import FastAPI

from conf.urls import router

app = FastAPI(title="Comments_API")
app.include_router(router)
