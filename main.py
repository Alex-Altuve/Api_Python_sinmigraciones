from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConection
from schema.user_schema import UserSchema


app = FastAPI()
conn = UserConection()
#para inscluir rutas
# app.include_router(user)


@app.get("/api/user",tags=["Usuario"], status_code= HTTP_200_OK)
def obtener_usuarios():
   item = []
   for data in conn.read_all():
      dictionary = {}
      dictionary["id"] = data[0]
      dictionary["name"] =data[1]
      dictionary["phone"] = data[2]
      item.append(dictionary)
 
   return item

@app.post("/api/user", tags=["Usuario"], status_code=HTTP_201_CREATED)
def crear_usuario(user_data: UserSchema):
   data = user_data.dict()
   data.pop("id")
   conn.write(data)
   return Response(status_code=HTTP_201_CREATED)

@app.get("/api/user/{id}",tags=["Usuario"], status_code= HTTP_200_OK)
def obtener_usuario(id: str):
   dictionary = {}
   data = conn.read_one(id)
   dictionary["id"] = data[0]
   dictionary["name"] =data[1]
   dictionary["phone"] = data[2]

   return dictionary

@app.delete("/api/user/{id}", tags=["Usuario"], status_code=HTTP_204_NO_CONTENT)
def eliminar_usuario(id: str):
   conn.delete(id)
   return Response(status_code=HTTP_204_NO_CONTENT)

@app.put("/api/user/{id}", tags=["Usuario"], status_code=HTTP_204_NO_CONTENT)
def actualizar_usuario(user_data: UserSchema, id: str):
   data = user_data.dict()
   data["id"] = id
   conn.uptade(data)
   return Response(status_code=HTTP_204_NO_CONTENT)