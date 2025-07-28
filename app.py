from flask import Flask, render_template, request
from scanner import scan_network

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    ports = request.form['ports']
    result = scan_network(target, ports)
    return render_template('index.html', result=result)
