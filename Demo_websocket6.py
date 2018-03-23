
# Please set sslopt to {"cert_reqs": ssl.CERT_NONE}.
import websocket
from websocket import create_connection
import ssl
ws = websocket.WebSocketApp("wss://echo.websocket.org")
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

