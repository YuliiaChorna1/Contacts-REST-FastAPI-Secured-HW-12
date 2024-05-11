import os
import signal
import uvicorn
import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager

import uvicorn.logging
from src.database.db import engine

from src.routes import contacts, auth

logger = logging.getLogger(uvicorn.logging.__name__)

@asynccontextmanager
async def lifespan(_):
    #startup initialization goes here
    logger.info("Knock-knock...")
    logger.info("Uvicorn has you...")
    yield
    #shutdown logic goes here    
    engine.dispose()
    logger.info("Good bye, Mr. Anderson")


app = FastAPI(lifespan=lifespan)

app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')

@app.get("/")
def read_root():
    return {"message": "Wake up!"}
    

if __name__ == '__main__':
    try:
        uvicorn.run("main:app", host='localhost', port=8000, reload=True)
    except KeyboardInterrupt:
        os.kill(os.getpid(), signal.SIGBREAK)
