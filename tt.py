import network
import time
import dht
import machine
import ujson
import uasyncio as asyncio

# Importa a classe AsyncWebsocketClient do módulo copiado
from async_websocket_client import AsyncWebsocketClient

# =====================================================
# Função para conectar à rede WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando à rede WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(0.5)
    print("Conexão estabelecida:", wlan.ifconfig())
    return wlan

# =====================================================
# Configurações de rede e sensor
SSID = "InHomeMac"         # Substitua pelo nome da sua rede
PASSWORD = "kt@2z9sxcv"     # Substitua pela sua senha WiFi
ws_url = "ws://192.168.1.237:8765"  # Altere para o IP/porta do seu servidor WebSocket
sensor_pin = 5           # Número do pino onde o DHT11 está conectado

# =====================================================
# Função para ler o sensor DHT11
def read_sensor():
    sensor = dht.DHT11(machine.Pin(sensor_pin))
    sensor.measure()
    return {"temperatura": sensor.temperature(), "umidade": sensor.humidity()}

# =====================================================
# Função assíncrona para enviar os dados do sensor via WebSocket
async def send_sensor_data():
    client = AsyncWebsocketClient()
    print("Realizando handshake com", ws_url)
    await client.handshake(ws_url)
    print("Handshake completo. Conexão aberta!")
    
    # Loop para enviar os dados a cada 2 segundos
    while True:
        try:
            data = read_sensor()
            msg = ujson.dumps(data)
            print("Enviando dados:", msg)
            await client.send(msg)
            await asyncio.sleep(2)
        except Exception as e:
            print("Erro ao enviar dados:", e)
            await asyncio.sleep(5)

# =====================================================
# Função principal: conecta no WiFi e executa o envio dos dados
def main():
    connect_wifi(SSID, PASSWORD)
    asyncio.run(send_sensor_data())

# =====================================================
if __name__ == "__main__":
    main()
