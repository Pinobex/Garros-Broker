import paho.mqtt.client as mqtt
import time

# Configurações do broker
BROKER_ADDRESS = "0.0.0.0"
PORT = 1884
TOPIC = "test/topic"

# Cria instância do cliente MQTT
client = mqtt.Client("teste", protocol = mqtt.MQTTv5)

# Conecta ao broker
client.connect(BROKER_ADDRESS, PORT, keepalive=60)

# Inicia o loop de rede em segundo plano
#client.loop_start()

try:
    while True:
        message = input("Digite a mensagem para enviar (ou 'exit' para sair): ")
        if message.lower() == 'exit':
            break
        client.publish(TOPIC, message)
        print(f"Mensagem publicada no tópico {TOPIC}: {message}")
        time.sleep(1)  # Pequeno delay opcional
except KeyboardInterrupt:
    print("\nInterrompido pelo usuário.")
finally:
    client.loop_stop()
    client.disconnect()
    print("Cliente MQTT desconectado.")