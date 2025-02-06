from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.src.routers import leagues_router, predictions_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=predictions_router, prefix="/prediction")
app.include_router(leagues_router)

@app.get("/")
async def root():
    return {"soccer-gurru api version": "0.0"}
