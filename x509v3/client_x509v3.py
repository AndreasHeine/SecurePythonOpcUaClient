from opcua import Client, ua

url = "opc.tcp://127.0.0.1:4840"
client = Client(url)

client.set_user("user1")
client.set_password("pw1")
client.set_security_string("Basic256Sha256,SignAndEncrypt,cert.pem,key.pem")
client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"

client.connect()
print(f"Connected to: {url}")

servicelevel_node = client.get_node("ns=0;i=2267")

servicelevel_node_value = servicelevel_node.get_value()
print(servicelevel_node_value)

client.disconnect()