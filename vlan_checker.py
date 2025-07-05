vlan = input("Ingrese el número de VLAN: ")

if not vlan.isdigit():
    print("Error: Ingrese solo números.")
else:
    vlan_num = int(vlan)
    if 1 <= vlan_num <= 1005:
        print(f"La VLAN {vlan_num} está en el rango NORMAL (1-1005).")
    elif 1006 <= vlan_num <= 4094:
        print(f"La VLAN {vlan_num} está en el rango EXTENDIDO (1006-4094).")
    else:
        print(f"La VLAN {vlan_num} está fuera de los rangos permitidos (1-4094).")
