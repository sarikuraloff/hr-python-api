from fastapi import FastAPI
from pydantic import BaseModel
from calc import calculate_compensation

app = FastAPI()

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
    result = calculate_compensation(
        d1=data.d1,
        d2=data.d2,
        used_old=data.used_work,
        used_new=data.used_cal,
        prog_old=data.prog_old,
        prog_new=data.prog_new,
        bs_old=data.bs_old,
        bs_new=data.bs_new,
    )
    return result
