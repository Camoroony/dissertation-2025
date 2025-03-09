from fastapi import APIRouter, Response

router = APIRouter(
    prefix="/users"
)

@router.get("")
def index() :
    return Response ("Hello from the users router!")