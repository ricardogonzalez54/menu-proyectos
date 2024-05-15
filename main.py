from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse      #Permite proyectar el index
from fastapi.middleware.cors import CORSMiddleware            #Permite corregir errores de navegador diciendo que no tienes permisos para hacer peticiones
from fastapi.staticfiles import StaticFiles                   #Permite montar la carpeta static
from starlette.responses import RedirectResponse

app = FastAPI()

# Permitir solicitudes Cross-Origin Resource Sharing  (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Permitir conexiones desde cualquier origen
    allow_methods=['*'],  # Permitir todos los métodos HTTP
    allow_headers=['*'],  # Permitir todas las cabeceras
     #allow_credentials=True #No funciona si las otras tres están en ['*']
)

# Montar la carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para servir el archivo HTML principal
@app.get("/menu")
async def get_index():
    return FileResponse("static/index.html")

#redirect
@app.get("/redirect")
async def redirectToMap():
    return RedirectResponse(url="http://192.168.31.22:5353")

# Funcionalidad para las solicitudes POST
@app.post("/menuPost")
async def post_data(request_data: dict):
    print("Entró al endpoint2 el mensaje")
    print(request_data)
    # publish.single("proyectores", request_data, hostname=mqtt_broker, port=mqtt_port)
    # return {"message": f"Image URL sent to MQTT broker. \nurl = {url}"}
    return "POST OK"





