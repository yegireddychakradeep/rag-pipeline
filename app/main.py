from fastapi import FastAPI
from app.routers.postPdf import router as post_router


app = FastAPI (
    title="rag system"
)

app.include_router(router = post_router)

@app.get("/")
async def root():
    return "Welcome to main"