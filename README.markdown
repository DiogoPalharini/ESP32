# 📡 Projeto ESP32 + WebSocket + Sensor DHT11

Este projeto faz a leitura de dados de temperatura e umidade via sensor DHT11, e os envia via WebSocket para um servidor local usando um ESP32.

## 📁 Estrutura do Projeto

```
ESP32/
├── async_websocket_client/   # Necessário enviar para o ESP32
├── server.py                 # Servidor WebSocket Python
├── index.html                # Página HTML opcional para exibir dados
├── tt.py                     # Código principal do ESP32
└── README.md
```

## 🚀 Requisitos

- ESP32 com MicroPython instalado
- Sensor DHT11
- Python 3 instalado no PC (para rodar o servidor)
- Rede Wi-Fi comum entre PC e ESP32
- Biblioteca `websockets` no Python (`pip install websockets`)

## 📲 Subindo o código para o ESP32

1. Instale o Thonny (ou use `mpremote`, `ampy`, etc.).
2. Conecte seu ESP32 via USB.
3. Abra o Thonny, selecione a placa como ESP32 com MicroPython.
4. Envie para o ESP32 os seguintes arquivos:
   - `tt.py` → renomeie como `main.py`
   - A pasta inteira `async_websocket_client`
5. **⚠ É fundamental que essa pasta esteja no mesmo nível de** `main.py` **dentro do ESP32.**
6. Para isso, no Thonny:
   - Clique com o botão direito na pasta → Upload to /
7. Verifique que `main.py` e `async_websocket_client/` estão no root do ESP32.

## 🌐 Configurando IP e Wi-Fi

No arquivo `main.py` (antigo `tt.py`), altere as seguintes linhas para sua rede:

```python
SSID = "SEU_WIFI"
PASSWORD = "SENHA_WIFI"
ws_url = "ws://IP_DO_PC:8765"
```

Para descobrir o IP do seu PC, execute no terminal:

- Windows: `ipconfig`
- Linux/macOS: `ifconfig`

Pegue o IP da interface conectada ao Wi-Fi. Exemplo: `192.168.140.217`

## 🖥️ Executando o servidor WebSocket

No seu PC, execute o arquivo `server.py`:

```bash
python server.py
```

Você verá no terminal mensagens como:

```
Servidor WebSocket rodando na porta 8765...
Cliente conectado.
Mensagem recebida: {"umidade": 41, "temperatura": 23}
```

## 🧪 Testes

Após iniciar o servidor e reiniciar o ESP32, você deverá ver os dados sendo enviados periodicamente.

Se houver quedas na conexão, verifique:

- A força do Wi-Fi
- Se o IP está correto
- Se a pasta `async_websocket_client` foi realmente enviada ao ESP32
- Logs de erro no Thonny