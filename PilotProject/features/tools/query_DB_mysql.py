
import MySQLdb


def query_mysql(config= None, service_name = None):

    try:
        connection = MySQLdb.connection.begin(host=qa_project_report_db['host'],
                                             database=qa_project_report_db['database'],
                                             user=qa_project_report_db['user'],
                                             password=qa_project_report_db['password'] )

        sql_select_Query = "SELECT scenario_name,service,action,taskid,param_name,param_value" + \
                           "FROM testcase_jest " +\
                           "WHERE service LIKE %{}%".format(service_name)
        print (sql_select_Query)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
    except mysql.connector.Error as e:
        raise Exception("Error reading data from MySQL table",e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


qa_project_report_db = {
    "host" : "10.23.41.160",
    "user" : "root",
    "password" : "password*1",
    "database" : "qafprojectreport",
    "port"     : "3306"
}
query_mysql(config=qa_project_report_db,service_name="GX-1846" )
