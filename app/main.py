from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.routes import router  # ✅ Import your router

app = FastAPI()

# Allow your frontend origin
origins = [
    "http://localhost:5173",
    # Add other frontend URLs if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Accept requests from these origins
    allow_credentials=True,
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all headers
)

app.include_router(router)  # ✅ Mount the router
