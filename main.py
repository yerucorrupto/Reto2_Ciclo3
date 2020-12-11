from db.reserva_db import ReservaInDB
from models.reserva_models import ReservaIn,ReservaOut
from db.reserva_db import save_reserva,getInfoReserva,buscarDisponibilidad
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

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