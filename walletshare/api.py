from fastapi import FastAPI

from walletshare.api.router import router

app = FastAPI()
app.include_router(router, prefix='/api')
