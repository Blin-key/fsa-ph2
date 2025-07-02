from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Flask api</h1>'

@app.route('/api/health')
def healthcheck():
    return '{ status: "ok" }'

if __name__ == "__main__":
    app.run(debug=True)

