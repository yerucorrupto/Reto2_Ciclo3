from pydantic import BaseModel
from datetime import date,datetime

class ReservaIn(BaseModel):
	idReserva: int
	NroDocum: int
	Nombre: str
	Celular: int
	Email: str
	FechaReserva: datetime
	FechaIngreso: date
	FechaSalida: date
	NumPersonas: int


class ReservaOut(BaseModel):
	idReserva: int
	NroDocum: int
	Nombre: str
	Celular: int
	Email: str
	FechaReserva: datetime
	FechaIngreso: date
	FechaSalida: date
	NumPersonas: int