from fastapi import FastAPI
from routes.user_routes import user
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)
app.include_router(user)

instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)