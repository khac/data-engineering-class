import psycopg2
import sys
import pprint
from string import Template 

def main():

	DB_PORT = "5432"
	DB_PASSWORD = ''
	DB_USER = 'postgres'
	DB_NAME = 'postgres'
	DB_HOST = 'localhost'
	#conn_string = "host=DB dbname='my_database' user='postgres' password=''"
	conn_string = Template('host=$DB_HOST dbname=$DB_NAME user=$DB_USER port=$DB_PORT password=$DB_PASSWORD')
	
	conn_string = conn_string.substitute({'DB_PORT': DB_PORT,'DB_PASSWORD': DB_PASSWORD,'DB_USER': DB_USER,'DB_HOST': DB_HOST,'DB_NAME': DB_NAME})
	# print the connection string we will use to connect
	print( "Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()

	# execute our Query
	cursor.execute("CREATE TABLE PURCHASES (\
  			PID VARCHAR(36),\
  			ORDER_DATE VARCHAR(10),\
  			CUSTOMER_ID VARCHAR(36)\
	);")
	cursor.execute("INSERT INTO PURCHASES (PID, ORDER_DATE, CUSTOMER_ID) \
		VALUES ('1', '05-10-2024', '1');\
	")
	cursor.execute("INSERT INTO PURCHASES (PID, ORDER_DATE, CUSTOMER_ID) \
		VALUES ('2', '05-10-2024', '2');\
	")
	cursor.execute("INSERT INTO PURCHASES (PID, ORDER_DATE, CUSTOMER_ID) \
		VALUES ('3', '05-10-2024', '3');\
	")
	cursor.execute("INSERT INTO PURCHASES (PID, ORDER_DATE, CUSTOMER_ID) \
		VALUES ('4', '05-10-2024', '4');\
	")

	cursor.execute("CREATE TABLE WEBSITE_VISITOR (\
  			TID VARCHAR(36),\
  			CUSTOMER_ID VARCHAR(36)\
	);")
	cursor.execute("INSERT INTO WEBSITE_VISITOR (TID, CUSTOMER_ID) \
		VALUES ('1', '1');\
	")
	cursor.execute("INSERT INTO WEBSITE_VISITOR (TID, CUSTOMER_ID) \
		VALUES ('2', '2');\
	")
	cursor.execute("INSERT INTO WEBSITE_VISITOR (TID, CUSTOMER_ID) \
		VALUES ('3', '3');\
	")
	cursor.execute("INSERT INTO WEBSITE_VISITOR (TID, CUSTOMER_ID) \
		VALUES ('4', '4');\
	")
	cursor.execute("INSERT INTO WEBSITE_VISITOR (TID, CUSTOMER_ID) \
		VALUES ('5', '5');\
	")

	# retrieve the records from the database
	cursor.execute("SELECT DISTINCT COUNT(*) FROM PURCHASES;");
	NUMERATOR = cursor.fetchall()

	cursor.execute("SELECT DISTINCT COUNT(*) FROM WEBSITE_VISITOR;");
	DENOMINATOR = cursor.fetchall()

	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
	pprint.pprint(NUMERATOR[0][0]/DENOMINATOR[0][0])

if __name__ == "__main__":
	main()
