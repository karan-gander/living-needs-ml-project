from flask import Flask, jsonify,request;
import requests;
import mysql.connector
import random;
import json
from seed import generate_optimal_leave_time;

from datetime import datetime, timedelta;
from faker import Faker;

fake = Faker()



# Weahter Api URl 
apiKey = '00663f03ce04654f452d8d30b6166d9e';
API_URI='https://api.openweathermap.org/data/2.5/weather?q=jodhpur&appid=00663f03ce04654f452d8d30b6166d9e'




app = Flask(__name__)




def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Use this if Flask runs locally
        user="akshu",
        password="karan",
        database="ml_model",
        port=3308
        
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT DATABASE();")
    
    db = cursor.fetchone()
    conn.close()
    return jsonify({"Connected to Database": db[0]})



@app.route("/seed")
def seed():
    conn=get_db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT Patient_ID FROM patients;")
    patient_ids = [row[0] for row in cursor.fetchall()]
    # data=generate_doctor_data()
    
    for i in range(100):
        optimal_leave_time = generate_optimal_leave_time()
        cursor.execute("""
            INSERT INTO optimal_leave_time (Leave_ID,Optimal_Leave_Time)
            VALUES (%s,%s)
        """, (fake.uuid4(),optimal_leave_time['Optimal_Leave_Time'],))
    conn.commit()
    cursor.close()
    conn.close()
    # print("Travel data seeded successfully!")

    # connection.commit()
    # cursor.close()
    # connection.close()
    return "T data seeded successfully!"


@app.route("/getweatherdata",methods=['GET'])
def getWeather():

    response = requests.get(API_URI);

    if(response.status_code==200):

        data= response.json()

        return data
    else:
        return jsonify({"error": "Failed to fetch data", "status_code": response.status_code}), response.status_code







if __name__ == "__main__":
    app.run(debug=True)
