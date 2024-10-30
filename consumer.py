import pika

# Cria uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define a fila da qual as mensagens serão recebidas
queue_name = 'minha-fila'
channel.queue_declare(queue=queue_name)

# Define a função de callback que será chamada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    print(" [x] Recebido %r" % body)

# Registra o callback para a fila
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Aguardando mensagens. Para sair, pressione CTRL+C')

# Começa a consumir as mensagens da fila
channel.start_consuming()