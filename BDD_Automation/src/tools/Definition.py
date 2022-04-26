
# SOAR
SOAR_ENV_SIT1 = 'http://10.24.139.15:9991/'
SOAR_ENV_SIT2 = 'http://10.24.139.15:9990/'
SOAR_ENV_SIT3 = 'http://10.24.139.15:9997/'

# Microservice
MICRO_ENV_ENV1 =   'http://amdocs-cm-sit.anthos-dev.intra.excelcom.co.id'
MICRO_ENV_ENV2 =   'http://amdocs-cm-sit.anthos-dev.intra.excelcom.co.id'
MICRO_ENV_ENV3 =   'http://amdocs-cm-sit.anthos-dev.intra.excelcom.co.id'

# Sample
SAMPLE         = 'http://10.24.139.18:15000/executerq'

#Definition Microservis
qa_project_report_db = {
    "host" : "10.23.41.160",
    "user" : "root",
    "password" : "password*1",
    "database" : "qafprojectreport",
    "port"     : "3306"
}

SOAR_TRCKTRACE_DB_ORACLE = {
    'host_name': 'cbtcnboradb02',
    "host": "10.23.41.88",
    'service_name': 'DEVDB',
    'user': 'SOAR_TRCKTRACE',
    'password': 'T3rlaluMudahPasswordnya',
    'port': '1521'
}

# API Endpoint
# http://roaming-vas-sit.api.devgcp.excelcom.co.id/
API_GET_SUBSCRIBER_DETAILS_ENDPOINT = 'http://roaming-vas-sit.api.devgcp.excelcom.co.id/roamingvas/v1/ubscriberdetails'
# API Endpoint
# http://redeem-voucher-sa-sit.api.devgcp.excelcom.co.id/
API_REDEEM_VOUCHER_SA_ENDPOINT = 'umb/menu/business/transferSa'

API_CUSTOM_ACTION               = 'custom-action'

API_SUBSCRIBER_PROFILE_INFO   = 'http://amdocs-cm-sit.anthos-dev.intra.excelcom.co.id/subscriber/v1/profile?'

API_JIRA_STATUS_ENDPOINT = 'https://collabs.xl.co.id/rest/api/2/issue/'