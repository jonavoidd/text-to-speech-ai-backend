from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from websocket import websocket_endpoint

app = FastAPI(title="Voice to Text AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.websocket("/ws")(websocket_endpoint)
