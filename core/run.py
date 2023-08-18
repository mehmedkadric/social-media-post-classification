from fastapi import FastAPI
from api.theme import router as theme_router

app = FastAPI()
app.include_router(theme_router)
