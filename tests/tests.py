from sra import Client

client = Client()

v = client.fetch('animal/bird')

print(v)