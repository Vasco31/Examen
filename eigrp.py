from netmiko import ConnectHandler
from getpass import getpass

# Conexión al router
router = {
    'device_type': 'cisco_ios',
    'host': '10.0.2.5',  # IP del CSR1000v
    'username': 'cisco',
    'password': 'cisco123',
    'secret': 'cisco123'
}

# Conectar al router
net_connect = ConnectHandler(**router)
net_connect.enable()

print("\n🔁 Conexión establecida.")

# Configurar EIGRP nombrado IPv4/IPv6
config_commands = [
    "router eigrp examen_mamamia",
    "address-family ipv4 unicast autonomous-system 100",
    "af-interface default",
    "passive-interface default",
    "no passive-interface Loopback22",
    "exit-address-family",
    "address-family ipv6 unicast autonomous-system 100",
    "af-interface default",
    "passive-interface default",
    "no passive-interface Loopback22",
    "exit-address-family"
]
output_config = net_connect.send_config_set(config_commands)
print("\n📦 Configuración EIGRP aplicada:")
print(output_config)

# Ejecutar comandos show
commands = {
    "🔍 EIGRP config": "show running-config | section eigrp",
    "📋 IP interfaces": "show ip interface brief",
    "🧾 Running-config": "show running-config",
    "🖥️  Version": "show version"
}

for desc, cmd in commands.items():
    print(f"\n{desc}")
    print(net_connect.send_command(cmd))

net_connect.disconnect()
