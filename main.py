from db.reserva_db import ReservaInDB
from models.reserva_models import ReservaIn,ReservaOut
from db.reserva_db import save_reserva,getInfoReserva,buscarDisponibilidad
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins=["http://localhost","http://localhost:8080","https://dummy-hotel-front.herokuapp.com",
"http://localhost.tiangolo.com","https://localhost.tiangolo.com",]

api.add_middleware(
    CORSMiddleware,allow_origins=origins,allow_credentials=True,
    allow_methods=["*"],allow_headers=["*"],)

@api.post("/hacer_reserva/")
async def hacer_reserva(reserva: ReservaIn):
	resultado = buscarDisponibilidad(reserva)
	if resultado:
		return save_reserva(reserva)
	else:
		raise HTTPException(status_code=400,
			detail="No se encuentra disponibilidad para esas fechas")

@api.get("/buscar-reserva/{idBuscado}")
async def buscar_reserva(idBuscado: int):
	resultado = getInfoReserva(idBuscado)
	if resultado:
		return resultado
	else:
		raise HTTPException(status_code=404, detail="La reserva no existe.")