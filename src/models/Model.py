from database import connectdb as conn
from .entities import Entities as entities
import json

connection = conn.get_connection()
class Model:
    @classmethod
    def get_points(self):
        try:
            connectionMySQL = conn.get_connectionMySQL()
            cursor = connection.cursor()
            cursor.execute("select*from punto")
            res = cursor.fetchall()
            connectionMySQL.close()
            points = []
            for result in res:
                point = {
                    "id_punto": result[0],
                    "coord_x": result[1],
                    "coord_y": result[2]
                }
                points.append(point)
            return points
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_clientes(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("declare @clientes nvarchar(max) set @clientes = ( select p.id_cliente, p.cli_nombres, p.cli_apellidos, p.cli_telefono, p.cli_direccion, p.cli_fecha_registro, p.cli_email from cliente p for json auto ) select @clientes as clientes return")
            result = cursor.fetchone()
            connection.close()
            return result
        except Exception as ex:
            raise Exception(ex)