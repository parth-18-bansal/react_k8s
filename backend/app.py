from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# database connection
db = pymysql.connect(
    host = 'mysql-service',
    user = 'root',
    password = 'root',
    database = 'app_db'
)

@app.route("/submit" , methods=['POST'])
def submit():
    data = request.json
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    email = data.get('email')
    confirmEmail = data.get('confirmEmail')
    city = data.get('city')
    phoneNumber = data.get('phoneNumber')

    with db.cursor() as cursor:
        sql = """
        INSERT INTO users (first_name, last_name, email, confirm_email, city, phone_number)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql,(firstName,lastName,email,confirmEmail,city,phoneNumber))

    db.commit()

    return jsonify({'message': 'Data inserted successfully'})


@app.route("/")
def hello():
    return "Hello from Flask in Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
