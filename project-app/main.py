import uvicorn
from fastapi import FastAPI

from core.router import main_router
from core.settings import settings

app = FastAPI()
app.include_router(main_router, prefix=settings.api.prefix)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
