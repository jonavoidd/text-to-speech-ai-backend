from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.websocket_route import websocket_endpoint
import uvicorn
import os

app = FastAPI(title="Voice to Text AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://text-to-speec-ai-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.websocket("/ws")(websocket_endpoint)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Use Render's assigned port
    uvicorn.run(app, host="0.0.0.0", port=port)
