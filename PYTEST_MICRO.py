from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a POST route
@app.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()  # Get JSON from request body
    student_id = data.get("id")
    name = data.get("Name")

    # Example response
    return jsonify({
        "message": "Student added successfully",
        "id": student_id,
        "name": name
    }), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/db")
def test_db():
    conn = get_connection()
    return {"status": "DB Connected"}