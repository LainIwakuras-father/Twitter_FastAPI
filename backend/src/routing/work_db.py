
db_router = APIRouter(prefix="/Api",tags=['Api'])

@db_router.get("/create_table")
async def create_table():
    try:
        await create_database()
        return JSONResponse({"message": "Models created!"}, status_code=201)
    except Exception as e:
        print(e)
        raise HTTPException(500, "Server error!")
    return JSONResponse({"message": "Models created!"}, status_code=201)

