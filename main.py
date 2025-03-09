import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("appointments.db")
cursor = conn.cursor()

# Create tables for doctors, patients, and appointments
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_id INTEGER,
    patient_id INTEGER,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id),
    FOREIGN KEY (patient_id) REFERENCES patients(id)
)
""")

conn.commit()

def add_doctor():
    name = input("Enter doctor's name: ")
    specialization = input("Enter specialization: ")
    cursor.execute("INSERT INTO doctors (name, specialization) VALUES (?, ?)", (name, specialization))
    conn.commit()
    print("Doctor added successfully!")

def view_doctors():
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    print("\nDoctors List:")
    for doc in doctors:
        print(f"ID: {doc[0]}, Name: {doc[1]}, Specialization: {doc[2]}")

def delete_doctor():
    view_doctors()
    doc_id = input("Enter doctor ID to delete: ")
    cursor.execute("DELETE FROM doctors WHERE id = ?", (doc_id,))
    conn.commit()
    print("Doctor deleted successfully!")

def add_patient():
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    cursor.execute("INSERT INTO patients (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Patient added successfully!")

def view_patients():
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    print("\nPatients List:")
    for pat in patients:
        print(f"ID: {pat[0]}, Name: {pat[1]}, Age: {pat[2]}")

def delete_patient():
    view_patients()
    pat_id = input("Enter patient ID to delete: ")
    cursor.execute("DELETE FROM patients WHERE id = ?", (pat_id,))
    conn.commit()
    print("Patient deleted successfully!")

def book_appointment():
    view_doctors()
    doctor_id = input("Enter doctor ID: ")
    view_patients()
    patient_id = input("Enter patient ID: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM): ")
    cursor.execute("INSERT INTO appointments (doctor_id, patient_id, date, time) VALUES (?, ?, ?, ?)", (doctor_id, patient_id, date, time))
    conn.commit()
    print("Appointment booked successfully!")

def view_appointments():
    cursor.execute("SELECT a.id, d.name AS doctor, p.name AS patient, a.date, a.time FROM appointments a JOIN doctors d ON a.doctor_id = d.id JOIN patients p ON a.patient_id = p.id")
    appointments = cursor.fetchall()
    print("\nAppointments:")
    for app in appointments:
        print(f"ID: {app[0]}, Doctor: {app[1]}, Patient: {app[2]}, Date: {app[3]}, Time: {app[4]}")

def delete_appointment():
    view_appointments()
    app_id = input("Enter appointment ID to delete: ")
    cursor.execute("DELETE FROM appointments WHERE id = ?", (app_id,))
    conn.commit()
    print("Appointment deleted successfully!")

def admin_view():
    while True:
        print("\nAdmin Panel")
        print("1. Manage Doctors")
        print("2. Manage Patients")
        print("3. Manage Appointments")
        print("4. Exit Admin View")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n1. Add Doctor\n2. View Doctors\n3. Delete Doctor")
            option = input("Choose an option: ")
            if option == '1':
                add_doctor()
            elif option == '2':
                view_doctors()
            elif option == '3':
                delete_doctor()
        elif choice == '2':
            print("\n1. Add Patient\n2. View Patients\n3. Delete Patient")
            option = input("Choose an option: ")
            if option == '1':
                add_patient()
            elif option == '2':
                view_patients()
            elif option == '3':
                delete_patient()
        elif choice == '3':
            print("\n1. Book Appointment\n2. View Appointments\n3. Delete Appointment")
            option = input("Choose an option: ")
            if option == '1':
                book_appointment()
            elif option == '2':
                view_appointments()
            elif option == '3':
                delete_appointment()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Try again.")

def main():
    while True:
        print("\nDoctor Appointment Management System")
        print("1. Admin View")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            admin_view()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
    conn.close()
