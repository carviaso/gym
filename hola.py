from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import sqlite3


app = Flask(__name__)


# sesion
app.secret_key = 'mysecretkey'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/clientes')
def clientes():
    # conn = pymysql.connect(host='localhost', user='root', passwd='desarrollo', db='gym')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('select id_socio, nombre, Telefono, Correoe, Miembro_desde from socio order by nombre')
    datos = cursor.fetchall()
    return render_template("clientes.html", clientes = datos )


@app.route('/agr_clientes')
def agr_clientes():
    return render_template("agr_clientes.html")


@app.route('/candidato')
def candidato():
    return render_template("candidato.html")


@app.route('/pagos')
def pagos():
    return render_template("pagos.html")


@app.route('/ventas')
def ventas():
    return render_template("ventas.html")


@app.route('/reportes')
def reportes():
    return render_template("reportes.html")


@app.route('/agrega_socio', methods=['POST'])
def agrega_socio():
    if request.method == 'POST':
        nombre = request.form['nom_socio']
        tel = request.form['tel']
        correoe = request.form['correoe']
        direccion = request.form['direccion']
        colonia = request.form['colonia']
        ciudad = request.form['ciudad']
        estado = request.form['estado']
        codpos = request.form['codpos']
        miembro = request.form['miembro']

        # conn = pymysql.connect(host='localhost', user='root', passwd='desarrollo', db='gym')
        conn = get_db_connection()
        cursor = conn.cursor()
        # cursor.execute('INSERT INTO socio (Nombre,Telefono,Correoe,Direccion,Colonia,Ciudad,Estado,Codpos,Miembro_desde) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (nombre, tel, correoe, direccion, colonia, ciudad, estado, codpos, miembro))
        cursor.execute('INSERT INTO socio (Nombre,Telefono,Correoe,Direccion,Colonia,Ciudad,Estado,Codpos,Miembro_desde) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)', (nombre, tel, correoe, direccion, colonia, ciudad, estado, codpos, miembro))
        conn.commit()
        flash('Socio Agregado')
    return redirect(url_for('clientes'))


@app.route('/ed_cliente/<string:id>')
def ed_cliente(id):
    # conn = pymysql.connect(host='localhost', user='root', passwd='desarrollo', db='gym')
    conn = get_db_connection()
    cursor = conn.cursor()
    # cursor.execute('select * from socio where id_socio = %s', (id))
    cursor.execute('select * from socio where id_socio =  ?', (id))
    dato=cursor.fetchall()
    return render_template("edi_clientes.html", cliente = dato[0] )


@app.route('/modifica_socio/<string:id>', methods=['POST'])
def modifica_socio(id):
    if request.method == 'POST':
        nombre = request.form['nom_socio']
        tel = request.form['tel']
        correoe = request.form['correoe']
        direccion = request.form['direccion']
        colonia = request.form['colonia']
        ciudad = request.form['ciudad']
        estado = request.form['estado']
        codpos = request.form['codpos']
        miembro = request.form['miembro']

        # conn = pymysql.connect(host='localhost', user='root', passwd='desarrollo', db='gym')
        conn = get_db_connection()
        # ORM9595 en workbench
        cursor = conn.cursor()
        # cursor.execute('update socio set Nombre=%s, Telefono=%s, Correoe=%s, Direccion=%s, Colonia=%s, Ciudad=%s, Estado=%s, Codpos=%s, Miembro_desde=%s where id_socio=%s', (nombre, tel, correoe, direccion, colonia, ciudad, estado, codpos, miembro,id))
        
        cursor.execute('update socio set Nombre= ?, Telefono= ?, Correoe= ?, Direccion= ?, Colonia= ?, Ciudad= ?, Estado= ?, Codpos= ?, Miembro_desde= ? where id_socio= ?', (nombre, tel, correoe, direccion, colonia, ciudad, estado, codpos, miembro,id))
        conn.commit()
        flash('Socio Actualizado')
    return redirect(url_for('clientes'))


@app.route('/bo_cliente/<string:id>')
def bo_cliente(id):
    # conn = pymysql.connect(host='localhost', user='root', passwd='desarrollo', db='gym')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('delete from socio where id_socio = {0}'.format(id))
    conn.commit()
    flash('Socio Eliminado')
    return redirect(url_for('clientes'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")


if __name__ == "__main__":
    app.run(debug = True)
 