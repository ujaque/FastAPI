from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

app = FastAPI()

# Iniciar el servidor: uvicorn users:app --reload

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [  User(id = 1, name = "David", surname= "Lopez", url = "ujaque.es", age = 39),
                User(id = 2, name = "Brais", surname = "Moure", url = "moure.dev",age = 20),
                User(id = 3, name = "Bu", surname = "Dev", url = "moure.com", age = 22)]

@app.get("/usersjson")
async def usersjson():
    return [{"id":1,"name":"David","surname":"Lopez","url":"ujaque.es", "age": 39},
            {"id":2,"name":"Brais","surname":"Moure","url":"moure.dev", "age": 20},
            {"id":3,"name":"Moure","surname":"Dev","url":"moure.com", "age": 22}]


@app.get("/users")
async def users():
    return users_list


#Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)



@app.post("/user/",response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    else:
        users_list.append(user)
        return user

@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user
    
@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            users_list[index] = user
            del users_list[index]
            found = True
    
    if not found:
        return {"error":"No se ha eliminado el usuario"}




def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}