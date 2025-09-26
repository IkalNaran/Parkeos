from flask import Flask, render_template

app = Flask(__name__)

@app.route("/adminqr")
def admin_qr():
    return render_template("Admin_qr.html")

@app.route("/codigoqr")
def codigo_qr():
    return render_template("codigo_qr.html")

@app.route("/crearcuenta")
def crear_cuenta():
    return render_template("crear_cuenta.html")

@app.route("/crearestudiante")
def crear_estudiante():
    return render_template("crear_estudiante.html")

@app.route("/crearprofesor")
def crear_profesor():
    return render_template("crear_profesor.html")

@app.route("/iniciodesesion")
def inicio_de_sesion():
    return render_template("inicio_de_sesion.html")

@app.route("/mapaestacionamiento")
def mapa_de_estacionamiento():
    return render_template("mapa_de_estacionamiento.html")

@app.route("/paneldeadmin")
def panel_de_admin():
    return render_template("panel_de_admin.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

if __name__ == "__main__":
    app.run(debug=True)