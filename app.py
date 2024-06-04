from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)


@app.route('/hello', methods=['GET','POST'])
def predict():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True,port=8080)  # You can set debug to False in production
