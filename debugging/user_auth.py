from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return {"status": "success", "message": "Login successful"}
    else:
        return {"status": "error", "message": f"Invalid credentials for {username}"}  # Information Leak

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    response = authenticate_user(data["username"], data["password"])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
    