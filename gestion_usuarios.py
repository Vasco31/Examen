from flask import Flask, request, jsonify
import sqlite3
import hashlib

# Inicializa Flask
app = Flask(__name__)

# Inicializa base de datos y crea tabla si no existe
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

# Lista de usuarios válidos: nombres de los integrantes
usuarios_validos = ["Francisco Moya", "Vasco Osorio", "Bruno Díaz"]

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    nombre = data.get('nombre')
    password = data.get('password')

    if nombre not in usuarios_validos:
        return jsonify({"mensaje": "Usuario no autorizado."}), 403

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, password_hash))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": f"Usuario {nombre} registrado correctamente."})

@app.route('/')
def inicio():
    return "API de gestión de usuarios funcionando."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5800)
