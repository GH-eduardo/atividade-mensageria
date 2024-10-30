import pika

# Cria uma conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Define a fila para a qual as mensagens serão enviadas
queue_name = 'minha-fila'
channel.queue_declare(queue=queue_name)

# Define a mensagem a ser enviada
message = 'Hello world'

# Envia a mensagem para a fila
channel.basic_publish(exchange='',
                      routing_key=queue_name,
                      body=message)

print(" [x] Enviado %r" % message)

# Fecha a conexão com o servidor RabbitMQ
connection.close()