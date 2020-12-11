from typing import  Dict
from pydantic import BaseModel
from datetime import date,datetime

class ReservaInDB(BaseModel):
	idReserva: int = 0
	NroDocum: int
	Nombre: str
	Celular: int
	Email: str
	FechaReserva: datetime = datetime.now()
	FechaIngreso: date
	FechaSalida: date
	NumPersonas: int = 1

database_reservas = Dict[int, ReservaInDB]

database_reservas = {1: ReservaInDB(**{"idReserva": 1,
									   "NroDocum": 123456,
									   "Nombre": "Eli",
									   "Celular": 3004444444,
									   "Email": "eli@eli.com",
									   "FechaReserva": '2020-12-10 19:20:20.000000',
									   "FechaIngreso": '2020-12-23',
									   "FechaSalida": '2021-01-01',
									   "NumPersonas": 2}),
					2: ReservaInDB(**{"idReserva": 2,
									   "NroDocum": 100200,
									   "Nombre": "Rafa",
									   "Celular": 3005555555,
									   "Email": "rafa@rafa.com",
									   "FechaReserva": '2020-12-10 19:30:30.000000',
									   "FechaIngreso": '2021-01-02',
									   "FechaSalida": '2021-01-11',
									   "NumPersonas": 2})}

generator = {"id":2}

#Métodos que necesito dentro de la funcionalidad del API
def save_reserva(reserva: ReservaInDB):
	generator["id"] = generator["id"] + 1
	reserva.idReserva = generator["id"]
	reserva.FechaReserva = datetime.now()
	database_reservas[reserva.idReserva]=reserva
	return reserva

def getInfoReserva(idReserva: int):
	if idReserva in database_reservas.keys():
		return database_reservas[idReserva]
	else:
		return None

def buscarDisponibilidad(reserva: ReservaInDB):
	ingreso_deseado = reserva.FechaIngreso
	salida_deseada = reserva.FechaSalida

	for element in database_reservas.values():
		ingreso = element.FechaIngreso
		salida = element.FechaSalida
		if (ingreso_deseado>ingreso) & (ingreso_deseado>=salida) & (salida_deseada>ingreso) & (salida_deseada>salida):
			disponible = True
		elif (ingreso_deseado<ingreso) & (ingreso_deseado<salida) & (salida_deseada<=ingreso) & (salida_deseada<salida):
			disponible = True
		else: return False
	return disponible