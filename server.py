import asyncio
import json
import websockets

# Conjunto para armazenar clientes conectados
connected_clients = set()

async def broadcast(message):
    if connected_clients:
        await asyncio.gather(*(client.send(message) for client in connected_clients))

async def handler(websocket, path=None):
    print("Cliente conectado.")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print("Mensagem recebida:", message)
            await broadcast(message)  # retransmite para todos os clientes
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Servidor WebSocket rodando na porta 8765...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
