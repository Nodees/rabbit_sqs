import boto3
import uuid

class SQS:

    @staticmethod
    def send_message():
        sqs = boto3.client('sqs')

        queue_url = ''

        # Gerar um UUID exclusivo para o MessageDeduplicationId.
        # O UUID é uma forma simples de garantir que cada mensagem tenha um ID exclusivo,
        # evitando duplicação de mensagens no SQS FIFO.
        message_deduplication_id = str(uuid.uuid4())

        # Envia a mensagem para a fila FIFO com os parâmetros necessários
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageAttributes={  # Atributos adicionais da mensagem
                'Title': {
                    'DataType': 'String',  # Tipo do dado
                    'StringValue': 'The Whistler'  # Valor do dado
                },
                'Author': {
                    'DataType': 'String',
                    'StringValue': 'John Grisham'
                },
                'WeeksOn': {
                    'DataType': 'Number',
                    'StringValue': '6'
                }
            },
            MessageBody=(  # Corpo da mensagem que será enviada
                'Information about current NY Times fiction bestseller for '
                'week of 12/11/2016.'
            ),
            MessageGroupId='test',  # ID do grupo da mensagem. Necessário para fila FIFO.
            MessageDeduplicationId=message_deduplication_id  # ID de deduplicação. Precisa ser único para cada mensagem.
        )

        return response

