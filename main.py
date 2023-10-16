from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
SERVER_NAME = "Data-Scientist IA"
# Configurar el origen permitido en CORS (solo necesario si estás trabajando en desarrollo local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajusta esto según tus necesidades de seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connected_clients = set()

@app.websocket("/chat/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    connected_clients.add(websocket)

    try:
        # Inicio de la conversación desde el servidor
        await websocket.send_text(f"{SERVER_NAME}: Welcome, ¿Ready to start? 'Yes (1)' or 'no (2)'.")

        while True:
            user_response = await websocket.receive_text()
            if user_response == '1':
                await websocket.send_text(f"{SERVER_NAME}: Has iniciado la conversación.")
            elif user_response == '2':
                await websocket.send_text(f"{SERVER_NAME}: No has iniciado la conversación.")
            else:
                await websocket.send_text(f"{SERVER_NAME}: Respuesta no válida. Por favor, responde con 'si (1)' o 'no (2)'.")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

@app.get("/", response_class=HTMLResponse)
async def read_item():
    with open("static/index.html") as f:

        return HTMLResponse(content=f.read())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
