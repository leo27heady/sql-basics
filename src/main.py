import mysql.connector
from datetime import datetime
from Classes import Patient  # , Blood_test, Covid_analysis


def create_database(cursor, base_name):
    cursor.execute("CREATE DATABASE {0}".format(base_name))


def create_tables(cursor):
    cursor.execute(
        "CREATE TABLE Patient ("
        + "id BIGINT AUTO_INCREMENT PRIMARY KEY"
        + ", passport_id VARCHAR(40) PRIMARY KEY"
        + ", full_name VARCHAR(40) NOT NULL"
        + ", birthday DATE"
        + ", sex char(1)"
        + ", CONSTRAINT check_sex CHECK (sex IN ('M', 'F'))"
        + ", CONSTRAINT cn_unique UNIQUE (passport_id)"
        + ")"
    )

    cursor.execute(
        "CREATE TABLE Blood_test ("
        + "id BIGINT AUTO_INCREMENT PRIMARY KEY"
        + ", patient_id VARCHAR(40) PRIMARY KEY"
        + ", passport_id VARCHAR(40)"
        + " FOREIGN KEY REFERENCES Patient(passport_id)"
        + ", blood_test_time DATETIME"
        + ", hemoglobin_level INT NOT NULL"
        + ", glucose_level FLOAT NOT NULL"
        + ", CONSTRAINT cn_unique UNIQUE (patient_id, passport_id)"
        + ")"
    )

    cursor.execute(
        "CREATE TABLE Covid_analysis ("
        + "id BIGINT AUTO_INCREMENT PRIMARY KEY"
        + ", covid_result BOOL PRIMARY KEY"
        + ", patient_id VARCHAR(40)"
        + " FOREIGN KEY REFERENCES Blood_test(patient_id)"
        + ", covid_test_time DATETIME"
        + ", CONSTRAINT cn_unique UNIQUE (passport_id)"
        + ")"
    )


def insert_into_patient(database, patient_obj):
    cursor.execute(
        "INSERT INTO Patient (passport_id, full_name, birthday, sex)"
        + " VALUES (%s, %s, %s, %s)",
        (
            patient_obj.passport_id,
            patient_obj.full_name,
            patient_obj.birthday,
            patient_obj.sex,
        ),
    )
    database.commit()


def insert_into_blood_test(database, blood_test_obj):
    cursor.execute(
        "INSERT INTO Blood_test ("
        + "patient_id"
        + ", passport_id"
        + ", blood_test_time"
        + ", hemoglobin_level"
        + ", glucose_level"
        + ")  VALUES (%s, %s, %s, %s, %s)",
        (
            blood_test_obj.patient_id,
            blood_test_obj.passport_id,
            blood_test_obj.blood_test_time,
            blood_test_obj.hemoglobin_level,
            blood_test_obj.glucose_level,
        ),
    )
    database.commit()


def insert_into_covid_analysis(database, covid_analysis_obj):
    cursor.execute(
        "INSERT INTO Covid_analysis ("
        + "covid_result"
        + ", patient_id"
        + ", covid_test_time"
        + ") VALUES (%s, %s, %s)",
        (
            covid_analysis_obj.covid_result,
            covid_analysis_obj.patient_id,
            covid_analysis_obj.covid_test_time,
        ),
    )
    database.commit()


db = mysql.connector.connect(
    host="localhost", user="root", passwd="051227", database="CovidDatabase"
)

cursor = db.cursor()

# create_database(cursor=cursor, base_name="CovidDatabase")

# create_tables(cursor=cursor)

patient_obj = Patient(
    passport_id="UA12345678AB",
    full_name="Kulyk Leonid Ruslanovych",
    birthday=datetime.strptime("27-07-2000", "%d-%m-%Y"),
    sex="M",
)
insert_into_patient(database=db, patient_obj=patient_obj)

# cursor.execute("SELECT * FROM Movie")

# cursor.execute("DROP TABLE Movie")

# for i in cursor:
# 	print(i)
