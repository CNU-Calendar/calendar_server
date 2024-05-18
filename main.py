import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.user import user_router


app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)

# if __name__ == "__main__":
#     print("http://127.0.0.1:8000/docs")
#     uvicorn.run(app, host="127.0.0.1", port=8000)
