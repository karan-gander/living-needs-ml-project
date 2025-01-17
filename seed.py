from faker import Faker
import mysql.connector
import random
import uuid
from datetime import datetime, timedelta


fake = Faker()

# Function to generate patient data
def generate_patient_data():
    return {
        "Patient_ID": fake.uuid4(),
        "Patient_Age": random.randint(18, 90),
        "Patient_Gender": random.choice(['Male', 'Female']),
        "Patient_Location": fake.address()
    }

# Function to generate appointment data
def generate_appointment_data():
    appointment_date = fake.date_this_year()
    appointment_time = fake.time()
    check_in_time = (datetime.combine(appointment_date, datetime.strptime(appointment_time, '%H:%M:%S').time()) + timedelta(minutes=random.randint(0, 30))).strftime('%H:%M:%S')
    check_out_time = (datetime.strptime(check_in_time, '%H:%M:%S') + timedelta(minutes=random.randint(10, 60))).strftime('%H:%M:%S')
    waiting_time = random.randint(5, 30)

    return {
        "Appointment_ID": fake.uuid4(),
        "Appointment_Date": appointment_date,
        "Appointment_Time": appointment_time,
        "Consultation_Type": random.choice(['Routine', 'Follow-up', 'Emergency']),
        "Check-in_Time": check_in_time,
        "Check-out_Time": check_out_time,
        "Waiting_Time": waiting_time

    }

# Function to generate doctor data
def generate_doctor_data():
    return {
        "Doctor_ID": str(uuid.uuid4()),
        "Doctor_Specialization": random.choice(['Cardiology', 'Neurology', 'Orthopedics', 'General Medicine', 'Pediatrics']),
        "Doctor_Availability": random.choice([True,False]),
        "Emergency_Cases_Handled": random.randint(0, 10)
    }

# Function to generate hospital data
def generate_hospital_data():
    return {
        "OPD_Capacity": random.randint(50, 200),
        "Current_OPD_Load": random.randint(10, 150)
    }

# Function to generate external factors data
def generate_external_factors():
    return {
        "Weather_Condition": random.choice(['Sunny', 'Rainy', 'Humid', 'Cloudy']),
        "Traffic_Condition": random.choice(['Low', 'Moderate', 'High']),
        "Public_Holiday": random.choice([True,False]),
        "Local_Event": random.choice([True,False])
    }

# Function to generate travel data
def generate_travel_data():
    return {
        "Distance_to_Hospital": random.randint(1, 20),
        "Travel_Time": random.randint(5, 60)
    }

# Function to generate historical insights data
def generate_historical_insights():
    return {
        "Avg_Doctor_Consultation_Time": random.randint(10, 30),
        "Avg_Patient_Waiting_Time": random.randint(5, 45)
    }

# Function to generate the optimal leave time
def generate_optimal_leave_time():
    return {
        "Optimal_Leave_Time": f"{random.randint(6, 8)}:{random.randint(0, 59):02d}"
    }

# Create database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Change this to 'mysql' if using Docker
        user="akshu",
        password="karan",
        database="ml_model",
        port=3308
    )

# Function to seed patient data
def seed_patient_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):  # Generate 100 records
        patient_data = generate_patient_data()
        cursor.execute("""
            INSERT INTO patients (Patient_ID, Patient_Age, Patient_Gender, Patient_Location)
            VALUES (%s, %s, %s, %s)
        """, (patient_data['Patient_ID'], patient_data['Patient_Age'], patient_data['Patient_Gender'], patient_data['Patient_Location']))
    conn.commit()
    cursor.close()
    conn.close()
    print("Patient data seeded successfully!")

# Function to seed appointment data
def seed_appointment_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        appointment_data = generate_appointment_data()
        cursor.execute("""
            INSERT INTO appointments (Appointment_ID, Appointment_Date, Appointment_Time, Consultation_Type, Check_in_Time, Check_out_Time, Waiting_Time)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (appointment_data['Appointment_ID'], appointment_data['Appointment_Date'], appointment_data['Appointment_Time'], appointment_data['Consultation_Type'], appointment_data['Check-in_Time'], appointment_data['Check-out_Time'], appointment_data['Waiting_Time']))
    conn.commit()
    cursor.close()
    conn.close()
    print("Appointment data seeded successfully!")

# Function to seed doctor data
def seed_doctor_data(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        doctor_data = data
        cursor.execute("""
            INSERT INTO doctor_data (Doctor_ID, Doctor_Specialization, Doctor_Availability, Emergency_Cases_Handled)
            VALUES (%s, %s, %s, %s)
        """, (doctor_data['Doctor_ID'], doctor_data['Doctor_Specialization'], doctor_data['Doctor_Availability'], doctor_data['Emergency_Cases_Handled']))
    conn.commit()
    cursor.close()
    conn.close()
    print("Doctor data seeded successfully!")

# Function to seed hospital data
def seed_hospital_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        hospital_data = generate_hospital_data()
        cursor.execute("""
            INSERT INTO hospitals (OPD_Capacity, Current_OPD_Load)
            VALUES (%s, %s)
        """, (hospital_data['OPD_Capacity'], hospital_data['Current_OPD_Load']))
    conn.commit()
    cursor.close()
    conn.close()
    print("Hospital data seeded successfully!")

# Function to seed external factors data
def seed_external_factors_data(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        external_factors = data()
        cursor.execute("""
            INSERT INTO external_factors (Weather_Condition, Traffic_Condition, Public_Holiday, Local_Event)
            VALUES (%s, %s, %s, %s)
        """, (external_factors['Weather_Condition'], external_factors['Traffic_Condition'], external_factors['Public_Holiday'], external_factors['Local_Event']))
    conn.commit()
    cursor.close()
    conn.close()
    print("External factors data seeded successfully!")

# Function to seed travel data
def seed_travel_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        travel_data = generate_travel_data()
        cursor.execute("""
            INSERT INTO travel (Distance_to_Hospital, Travel_Time)
            VALUES (%s, %s)
        """, (travel_data['Distance_to_Hospital'], travel_data['Travel_Time']))
    conn.commit()
    cursor.close()
    conn.close()
    print("Travel data seeded successfully!")

# Function to seed historical insights data
def seed_historical_insights():
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        historical_insights = generate_historical_insights()
        cursor.execute("""
            INSERT INTO historical_insights (Avg_Doctor_Consultation_Time, Avg_Patient_Waiting_Time)
            VALUES (%s, %s)
        """, (historical_insights['Avg_Doctor_Consultation_Time'], historical_insights['Avg_Patient_Waiting_Time']))
    conn.commit()
    cursor.close()
    conn.close()
    print("Historical insights data seeded successfully!")

# Function to seed optimal leave time
def seed_optimal_leave_time():
    conn = get_db_connection()
    cursor = conn.cursor()
    for _ in range(100):
        optimal_leave_time = generate_optimal_leave_time()
        cursor.execute("""
            INSERT INTO optimal_leave_time (Optimal_Leave_Time)
            VALUES (%s)
        """, (optimal_leave_time['Optimal_Leave_Time'],))
    conn.commit()
    cursor.close()
    conn.close()
    print("Optimal leave time data seeded successfully!")

# Run all the seed functions
if __name__ == "__main__":
    seed_patient_data()
    seed_appointment_data()
    seed_doctor_data()
    seed_hospital_data()
    seed_external_factors_data()
    seed_travel_data()
    seed_historical_insights()
    seed_optimal_leave_time()
    