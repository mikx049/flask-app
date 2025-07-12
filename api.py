from flask import Flask, jsonify, request

app = Flask(__name__)
def main():
    @app.route("/api/data", methods=["GET"])
    def get_data():
        data = {
            "message": "Hello from Flask API!",
            "status": "success"
        }
        return jsonify(data)
    @app.route("/api/data", methods=["POST"])
    def post_data():
        data = request.json
        response = {
            "received": data,
            "status": "success"
        }
        return jsonify(response), 201
if __name__ == "__main__":
    app.run()