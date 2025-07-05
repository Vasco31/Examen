from ncclient import manager

# Datos de conexión al router CSR1000v
router = {
    "host": "192.168.56.102",  # IP del CSR1000v según tu captura
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

# XML para cambiar el hostname con apellidos
hostname_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>MOYA_OSORIO_DIAZ</hostname>
  </native>
</config>
"""

# XML para crear la interfaz loopback 11 con IP 11.11.11.11/32
loopback_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# Conexión y envío de configuraciones
with manager.connect(**router) as m:
    print("Conectado al router CSR1000v mediante NETCONF.\n")

    # Cambiar hostname
    hostname_response = m.edit_config(target="running", config=hostname_config)
    print("Respuesta al cambio de hostname:\n", hostname_response)

    # Crear Loopback 11
    loopback_response = m.edit_config(target="running", config=loopback_config)
    print("Respuesta a la creación de Loopback 11:\n", loopback_response)
