import mysql.connector
from datetime import datetime
from classes import Patient, Blood_test, Covid_analysis


def create_database(cursor, base_name):
    cursor.execute("CREATE DATABASE {0}".format(base_name))


def create_tables(cursor):
    cursor.execute(
        "CREATE TABLE Patient ("
        + "id BIGINT AUTO_INCREMENT PRIMARY KEY"
        + ", passport_id VARCHAR(40) NOT NULL UNIQUE"
        + ", full_name VARCHAR(40) NOT NULL"
        + ", birthday DATE NOT NULL"
        + ", sex char(1) NOT NULL"
        + ", CONSTRAINT check_sex CHECK (sex IN ('M', 'F'))"
        + ")"
    )

    cursor.execute(
        "CREATE TABLE Blood_test ("
        + "id BIGINT AUTO_INCREMENT PRIMARY KEY"
        + ", patient_id VARCHAR(40)  NOT NULL"
        + ", passport_id VARCHAR(40)  NOT NULL"
        + ", blood_test_time DATETIME NOT NULL"
        + ", hemoglobin_level INT NOT NULL"
        + ", glucose_level FLOAT NOT NULL"
        + ", FOREIGN KEY (id)  REFERENCES Patient(id)"
        + ")"
    )

    cursor.execute(
        "CREATE TABLE Covid_analysis ("
        + "id BIGINT AUTO_INCREMENT PRIMARY KEY"
        + ", patient_id VARCHAR(40)  NOT NULL"
        + ", covid_result BOOL  NOT NULL"
        + ", covid_test_time DATETIME  NOT NULL"
        + ", FOREIGN KEY (id)  REFERENCES Patient(id)"
        + ")"
    )


def insert_into_patient(cursor, database, patient_obj):
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


def insert_into_blood_test(cursor, database, blood_test_obj):
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


def insert_into_covid_analysis(cursor, database, covid_analysis_obj):
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


def insert_new_patient_obj(
    cursor, database, patient_obj, blood_test_obj, covid_analysis_obj
):
    blood_test_obj.passport_id = patient_obj.passport_id
    covid_analysis_obj.patient_id = blood_test_obj.patient_id

    insert_into_patient(cursor, database, patient_obj)
    insert_into_blood_test(cursor, database, blood_test_obj)
    insert_into_covid_analysis(cursor, database, covid_analysis_obj)


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

blood_test_obj = Blood_test(
    patient_id="00000001",
    # passport_id="UA12345678AB",
    hemoglobin_level=10,
    glucose_level=0.4,
    blood_test_time=datetime.strptime("18-09-2020 20:16", "%d-%m-%Y %H:%M"),
)

covid_analysis_obj = Covid_analysis(
    covid_result=True,
    # patient_id="00000001",
    covid_test_time=datetime.strptime("18-09-2020 20:39", "%d-%m-%Y %H:%M"),
)


# insert_into_patient(cursor=cursor, database=db, patient_obj=patient_obj)
# insert_into_blood_test(cursor, db, blood_test_obj)

insert_new_patient_obj(
    cursor=cursor,
    database=db,
    patient_obj=patient_obj,
    blood_test_obj=blood_test_obj,
    covid_analysis_obj=covid_analysis_obj,
)

cursor.close()
db.close()

# cursor.execute("SELECT * FROM Movie")
# cursor.execute("DROP TABLE Movie")

# for i in cursor:
# 	print(i)
