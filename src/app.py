# app.py  

from flask import Flask, render_template, request, redirect, url_for, flash  
from models import users  

app = Flask(__name__)  
app.secret_key = 'secreto'  # Para permitir el uso de sesiones y mensajes de flash  
notifications = []  

# Home y Login  
@app.route('/')  
def home():  
    return render_template('login.html')  

@app.route('/login', methods=['POST'])  
def login():  
    username = request.form['username']  
    password = request.form['password']  

    # Historia 1: Iniciar sesión  
    if username in users and users[username].password == password:  
        flash('Inicio de sesión exitoso')  
        return redirect(url_for('dashboard', username=username))  
    
    flash('Credenciales incorrectas')  
    return redirect(url_for('home'))  

# Dashboard  
@app.route('/dashboard/<username>', methods=['GET'])  
def dashboard(username):  
    user = users.get(username)  
    return render_template('dashboard.html', user=user)  

# Perfil  
@app.route('/profile/<username>', methods=['GET'])  
def profile(username):  
    user = users.get(username)  
    return render_template('profile.html', user=user)  

# Notificaciones (Historia 3)  
@app.route('/notifications', methods=['GET'])  
def view_notifications():  
    return render_template('notifications.html', notifications=notifications)  

# Añadir notificación  
@app.route('/add_notification', methods=['POST'])  
def add_notification():  
    notification = request.form['notification']  
    notifications.append(notification)  # Almacena la notificación  
    flash('Notificación añadida')  
    return redirect(url_for('view_notifications'))  

# Búsqueda de elementos (Historia 4)  
@app.route('/search', methods=['GET'])  
def search():  
    query = request.args.get('query')  
    # Implementar lógica de búsqueda en los elementos. Simulación:  
    items = ["Item1", "Item2", "Item3"]  
    filtered_items = [item for item in items if query in item]  
    return render_template('search_results.html', items=filtered_items)  

# Edición de perfil (Historia 5)  
@app.route('/edit_profile/<username>', methods=['POST'])  
def edit_profile(username):  
    new_email = request.form['email']  
    user = users.get(username)  
    if user:  
        user.email = new_email  # Actualiza el email del usuario en la simulación  
    flash('Perfil actualizado con éxito')  
    return redirect(url_for('profile', username=username))  

if __name__ == '__main__':  
    app.run(debug=True)