from tools import Utility as Ut
from tools import Definition as Define

import uuid
uuid4=str(uuid.uuid4())
import cx_Oracle
# cx_Oracle.init_oracle_client(lib_dir=r'C:\Work\BDD\BehavePythonProject\BDD_Automation\src\tools\instantclient_21_3')
query = '''
SELECT msisdn, sys_creation_date, soccd, serviceid, completionstatus, CD_MAIN_ID, esbuuid, policyname, operationname, expirationdate, benefittype, exceptioncode, exceptiondescription
FROM SOARTT_MISCKPI
WHERE msisdn = '6287868381200' AND esbuuid = '{}'
ORDER BY sys_creation_date DESC'''.format('a3d9caa0-9ba1-452c-bd6a-83a442eda9fe')

config = {
    'host_name': 'cbtcnboradb02',
    'host': '10.23.41.88',
    'service_name': 'DEVDB',
    'user': 'SOAR_TRCKTRACE',
    'password': 'T3rlaluMudahPasswordnya',
    'port': '1521'
}

dsn_tns = cx_Oracle.makedsn('10.23.41.88',
                            int('1521'),
                            service_name='DEVDB')
conn = cx_Oracle.connect(user='SOAR_TRCKTRACE',
                         password='T3rlaluMudahPasswordnya',
                         dsn=dsn_tns, encoding="UTF-8")
cursor = conn.cursor()
records = cursor.execute(query)
for x in records:
    print(type(x))
cursor.close()
conn.close()