from flask import Flask, request, render_template, redirect, url_for
from database import init_db, get_conn

app = Flask(__name__)

# Inicializa la base de datos al arrancar
init_db()

@app.route("/")
def index():
    conn = get_conn()
    cursor = conn.execute("SELECT COUNT(*) FROM inscritos")
    total = cursor.fetchone()[0]
    conn.close()
    return render_template("index.html", total=total)

@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    if request.method == "POST":
        nombre    = request.form.get("nombre")
        correo    = request.form.get("correo")
        invocador = request.form.get("invocador")
        rango     = request.form.get("rango")
        equipo    = request.form.get("equipo")

        conn = get_conn()
        conn.execute(
            """
            INSERT INTO inscritos(nombre, correo, invocador, rango, equipo)
            VALUES (?, ?, ?, ?, ?)
            """,
            (nombre, correo, invocador, rango, equipo)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("confirmacion", nombre=invocador))

    return render_template("inscripcion.html")

@app.route("/confirmacion")
def confirmacion():
    nombre = request.args.get("nombre")
    return render_template("confirmacion.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)