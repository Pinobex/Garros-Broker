import paho.mqtt.client as mqtt

# Configurações do broker
BROKER_ADDRESS = "0.0.0.0"  # Pode trocar pelo seu broker
PORT = 1884
TOPIC = "test/topic"

# Função chamada quando o cliente conecta com sucesso ao broker
def on_connect(client, userdata, flags, reason, properties):
    if reason == 0:
        print("Conectado ao broker com sucesso.")
        client.subscribe(TOPIC)
        print(f"Inscrito no tópico: {TOPIC}")
    else:
        print(f"Falha na conexão. Código de retorno: {reason} {properties}")

# Função chamada quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

# Criação do cliente MQTT
client = mqtt.Client("client_subscriber", protocol = mqtt.MQTTv5)

# Vinculando funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conexão ao broker
client.connect(BROKER_ADDRESS, PORT, keepalive=60)

# Inicia o loop para manter o cliente ativo e escutando
client.loop_forever()