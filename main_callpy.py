from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse  # Importa JSONResponse
import subprocess

app = FastAPI()

@app.route("/ejecutar-script/", methods=["POST", "GET"])
async def ejecutar_script(request: Request):
    if request.method == "POST":
        try:
            proceso = subprocess.Popen(["python", "loadnewdata.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            proceso.stdin.write(b'1\n')  # Envía una respuesta "sí" al script
            proceso.stdin.close()
            resultado = proceso.communicate()
            resultado_stdout = resultado[0].decode()
            resultado_stderr = resultado[1].decode()

            if proceso.returncode == 0:
                return JSONResponse(content={"resultado": resultado_stdout})  # Devuelve una respuesta JSON
            else:
                return JSONResponse(content={"error": resultado_stderr}, status_code=500)  # Devuelve una respuesta JSON con un código de estado 500

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    elif request.method == "GET":
        # Manejar la solicitud GET aquí si es necesario
        return JSONResponse(content={"mensaje": "Esta es una solicitud GET"})
