from flask import  render_template, request, redirect, url_for, flash
import database

mysql = database.mysql


def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    
    return render_template('index.html', contactos = data)


def addcontact():
    if request.method == 'POST':
        cur= mysql.connection.cursor()
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        if fullname == "":
            flash('Debes agregar un nombre')
            return redirect(url_for('home'))            
        if phone == "":
            flash('Debes agregar un telefono')
            return redirect(url_for('home'))   
        if email == "":
            return redirect(url_for('home')) 
        else:
            cur.execute('INSERT INTO contacts (name, phone, email) VALUES(%s,%s,%s)', 
            (fullname, phone, email))    
            mysql.connection.commit()
            flash('Contacto agregado con exito')
        return redirect(url_for('home'))    

def onecontact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', {id})
    data = cur.fetchall()
    print(data[0])
    return render_template('editar.html', editor = data[0])


def update():
    id = request.form['id']
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE contacts
            SET name = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email, phone, id))
    flash('Contacto actualizado')
    mysql.connection.commit()
    return redirect(url_for('home'))    
            
      

def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'. format(id))
    mysql.connection.commit()
    flash('usuario eliminado correcto')
    return redirect(url_for('home'))

