import psycopg2
import os

conn = psycopg2.connect(database="project",
                        host="localhost",
                        user="postgres",
                        password="1234",
                        port="5432")

attributes = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
              'marital_status', 'occupation', 'relationship', 'race',
              'sex', 'native_country', 'income']

measures = ['capital_gain', 'capital_loss', 'hours_per_week']

aggregations = ['sum', 'count', 'max', 'avg']


cursor = conn.cursor()
for attr in attributes:
    for m in measures:
        for agg in aggregations:
            sql = f'select {attr}, {agg}({m}) from adult group by {attr}'
            saveSQL = f"Copy ({sql}) to '{os.path.join(os.getcwd(),'views',f'{attr}-{m}-{agg}.csv')}' With CSV DELIMITER ',' HEADER"
            cursor.execute(saveSQL)

cursor.close()

conn.close() 