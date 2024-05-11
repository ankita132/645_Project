import psycopg2
import os

def createRawSchemaTable():
    conn = psycopg2.connect(database="project",
                            host="localhost",
                            user="postgres",
                            password="1234",
                            port="5432")

    cursor = conn.cursor()

    cursor.execute('drop table IF EXISTS Adult cascade')
    cursor.execute('create table Adult (age integer, workclass varchar(20), fnlwgt integer, education varchar(20), education_num integer, marital_status varchar(50), occupation varchar(20), relationship varchar(20), race varchar(20), sex varchar(20), capital_gain integer, capital_loss integer, hours_per_week integer, native_country varchar(50), income varchar(10))')
    cursor.execute("COPY Adult FROM '/Users/ankita132/Documents/umass/645/project/projectv2/adult.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER MATCH, FORCE_NULL(age, fnlwgt, education_num, capital_loss, capital_gain, hours_per_week))")
    cursor.execute("COPY Adult FROM '/Users/ankita132/Documents/umass/645/project/projectv2/adult_test.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER MATCH, FORCE_NULL(age, fnlwgt, education_num, capital_loss, capital_gain, hours_per_week))")

    conn.commit()
    cursor.close()
    conn.close() 

createRawSchemaTable()