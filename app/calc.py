from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/calc/sqrt/<int:num>")
def sqrt(num):
    result = math.sqrt(num)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
