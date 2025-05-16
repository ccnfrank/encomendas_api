from fastapi import APIRouter
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])


@order_router.get("/")
async def funcao():
    return {"first_msg":"iniciar construcao api"}
    




