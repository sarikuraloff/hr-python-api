from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from calc import calculate_compensation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalcRequest(BaseModel):
    d1: str
    d2: str
    used_work: float
    used_cal: float
    prog_old: int
    prog_new: int
    bs_old: int
    bs_new: int

@app.post("/calculate")
def calculate(data: CalcRequest):
    used_total = data.used_work + data.used_cal

    return calculate_compensation(
        d1=data.d1,
        d2=data.d2,
        used_total=used_total,
        prog_old=data.prog_old,
        prog_new=data.prog_new,
        bs_old=data.bs_old,
        bs_new=data.bs_new,
    )
