from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timezone, timedelta
import os, pytz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticação aqui (pode ser adicionada posteriormente)
        # Por enquanto, apenas redirecionamos para a tela de aterrissagem
        return redirect(url_for('landing'))
    return render_template('login.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/get_server_time')
def get_server_time():
    # Obtém o horário atual no fuso horário de São Paulo (GMT-3)
    tz = pytz.timezone('America/Sao_Paulo')
    current_time = datetime.now(tz).strftime('%d/%m/%Y %H:%M:%S')
    return jsonify({'time': current_time})

@app.route('/file_upload')
def file_upload():
    return render_template('file_upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'fileInput' in request.files:
        file = request.files['fileInput']
        if file.filename != '':
            filename, file_extension = os.path.splitext(file.filename)
            file_info = {
                'filename': file.filename,
                'size': len(file.read()),
                'extension': file_extension
            }
            return render_template('file_upload.html', file_info=file_info)
    
    return redirect(url_for('file_upload'))

if __name__ == '__main__':
    app.run(debug=True)
