from fastapi import FastAPI, APIRouter
from typing import List

from .identification import RIdentification


def include(app: FastAPI):
    way: List[APIRouter] = [RIdentification]

    for router in way:
        print(f"{router.prefix}: {router.tags}")
        app.include_router(router)
