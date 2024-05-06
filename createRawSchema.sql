--"/Applications/Postgres.app/Contents/Versions/16/bin/psql" -f createRawSchema.sql project

drop table IF EXISTS Adult cascade;
create table Adult (age integer, workclass varchar(20),
fnlwgt integer, education varchar(20), education_num integer,
marital_status varchar(50), occupation varchar(20), relationship varchar(20),
race varchar(20), sex varchar(20), capital_gain integer, capital_loss integer,
hours_per_week integer, native_country varchar(50), income varchar(10));

\COPY Adult FROM './adult.csv' WITH (FORMAT CSV, DELIMITER ',', HEADER MATCH, FORCE_NULL(age, fnlwgt, education_num, capital_loss, capital_gain, hours_per_week));