from fastapi                    import FastAPI
from fastapi.middleware.cors    import CORSMiddleware
from server.routes.users        import router as UserRouter
from server.routes.roles        import router as RoleRouter

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter, tags=["Usuarios"], prefix="/user")
app.include_router(RoleRouter, tags=["Roles"], prefix="/role")

@app.get("/", tags=["Root"])
async def read_root():
    return{
        "message" : "Buenas Tardes C&A"
    }