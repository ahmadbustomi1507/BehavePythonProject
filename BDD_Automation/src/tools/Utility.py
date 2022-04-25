
# from requests import *
import json
import httpx
import MySQLdb
import copy
import os
import sys

import cx_Oracle
try:
    cx_Oracle.init_oracle_client(lib_dir=r'tools\instantclient_21_3')
except Exception as err:
    print("Whoops!")
    print(err);
    sys.exit(1);

# Request Builder
# def Send_Request(type= "GET", api_endpoint =None, Params =None , Body={} ):
#     if type =='GET':
#         response = httpx.get(url=api_endpoint, params=Params)
#     elif type == 'POST' :
#         response = httpx.post(url=api_endpoint,  data = Body)
#         pass
#
#     return response


# Parsing the JSON from external
def json2dict(input_json={}):
    return json.loads(input_json)


def dict2json(input_dict={}):
    return json.dumps(input_dict)

def query_oracle(config=None,query=''):

    dsn_tns = cx_Oracle.makedsn(config['host'],
                                int(config['port']),
                                service_name=config['service_name'])

    conn = cx_Oracle.connect(user=config['user'],
                             password=config['password'],
                             dsn=dsn_tns,encoding="UTF-8")
    cursor   = conn.cursor()
    cursor.execute(query)
    records  = cursor.fetchall()
    # cursor.close()
    conn.close()

    return records

def query_mysql(config=None, query = ''):
    try:
        db_connection = MySQLdb.connect(host=config['host']   ,
                                        port = int(config['port']),
                                             database=config['database'],
                                             user=config['user'],
                                             password=config['password'] )

        cursor = db_connection.cursor()
        cursor.execute(query)
        # get all records
        records = cursor.fetchall()
        # return records
    except MySQLdb.connections.Error as e :
        raise Exception("Error reading data from MySQL table",e)

    finally:
        cursor.close()
        db_connection.close()
        return records

    # return Ut.dict2json(records)
    # return records
    # print(records)
    # dict_data_test = {}
    # for record in records:
    #     data_test = copy.deepcopy(record)
    #     dummy_dict = {}
    #     if data_test[1] in dict_data_test.keys():
    #         #modify the dict data and convert it to lower case
    #         param = copy.deepcopy(data_test[5]).lower()
    #         value = copy.deepcopy(data_test[6]).lower()
    #         dict_data_test[data_test[1]]['data'][param] = value
    #     else :
    #         #create new key value
    #         dict_data_test[data_test[1]]            = {}
    #         dict_data_test[data_test[1]]['scenario_name'] =  data_test[0]
    #         dict_data_test[data_test[1]]['service']          =  data_test[2]
    #         dict_data_test[data_test[1]]['action']      =  data_test[3]
    #         dict_data_test[data_test[1]]['taskid']      =  data_test[4]
    #         dict_data_test[data_test[1]]['data']        = {}
    # return dict_data_test

# #debug
# data_releng = query_mysql(config= {
#     "host" : "10.23.41.160",
#     "user" : "root",
#     "password" : "password*1",
#     "database" : "qafprojectreport",
#     "port"     : "3306"
# }, task_id="GX-1846")
# print(data_releng)
