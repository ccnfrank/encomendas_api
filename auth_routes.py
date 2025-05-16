from fastapi import APIRouter
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def autent():
    """
    api criada publica por christian frank. todos user precisam de autenticacao \n
    caso voce ainda nao tenha recebido seu login / pass, entre em contato com ccnfrank@gmail.com
    
    """
    return {"msg":"rota autenticacao","autenticado":False}