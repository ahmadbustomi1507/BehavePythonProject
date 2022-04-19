import behave
import copy
from tools import Utility as Ut
from tools import Definition as Definition
import os

def post_test(context, feature):
    print ('------------END THE PROJECT ---------------------')
    return True

def initialized(context, feature):
    feature_name = os.path.basename(context.feature.filename)
    task_id      = '-'.join(feature_name.split('_')[0:2])
    query        = '''
                    SELECT scenario_name,scenario_id,service,action,taskid,param_name,param_value
                    FROM testcase_jest
                    WHERE taskid = '{}'
                    '''.format(task_id)
    records = Ut.query_mysql(config=Definition.qa_project_report_db, query=query)
    ''' extract the data from releng centre, then create a new structure as
        {
            <scenario_id> :{
                <scenario_name> : <...> , 
                <service>       : <...> ,
                <action>        : <...> ,
                <taskid>        : <...> ,
                <data>          : { <param1> :<value1>,
                                    <param2> :<value2>}
            }
        }
        
        Then return it as a dict 
        
    '''
    dict_data_test = {}
    for record in records:
        data_test = copy.deepcopy(record)
        if data_test[1] in dict_data_test.keys():
            # modify the dict data and convert it to lower case
            param = copy.deepcopy(data_test[5]).lower()
            value = copy.deepcopy(data_test[6]).lower()
            dict_data_test['scenario_id']['data'][param] = value
        else:
            # create new key value
            dict_data_test['scenario_id'] = {}
            dict_data_test['scenario_id']['scenario_name'] = data_test[0]
            dict_data_test['scenario_id']['service'] = data_test[2]
            dict_data_test['scenario_id']['action'] = data_test[3]
            dict_data_test['scenario_id']['taskid'] = data_test[4]
            dict_data_test['scenario_id']['data'] = {}

    return {
        'feature_name': feature_name,
        'env': '<on progress env>',
        'test' : dict_data_test
    }
