import psycopg2
import os

def createUserTable():
    conn = psycopg2.connect(database="project",
                            host="localhost",
                            user="postgres",
                            password="1234",
                            port="5432")

    cursor = conn.cursor()

    cursor.execute('drop table IF EXISTS AdultUser cascade')
    cursor.execute('create table AdultUser (age integer, workclass varchar(20), fnlwgt integer, education varchar(20), education_num integer, marital_status varchar(50), occupation varchar(20), relationship varchar(20), race varchar(20), sex varchar(20), capital_gain integer, capital_loss integer, hours_per_week integer, native_country varchar(50), income varchar(10))')
    # cursor.execute("INSERT INTO AdultUser select * from Adult WHERE marital_status like '%Married-civ-spouse' or marital_status like '%Married-AF-spouse' or marital_status like '%Married-spouse-absent'")

    conn.commit()
    cursor.close()
    conn.close() 

def getWhereCondition():
    return "marital_status like '%Married-civ-spouse' or marital_status like '%Married-AF-spouse' or marital_status like '%Married-spouse-absent'"

# createUserTable()
print(getWhereCondition())