
import settings
from behave.log_capture import capture

def before_feature(context, feature):
    logging.info('Before feature nya jalan')
    return settings.initialized(context, feature)

def after_feature(context, feature):
    print(context.log_capture)
    return settings.post_test(context,feature)

# import behave
# import copy
# from tools import Utility as Ut
# from tools import Definition as Definition
#
# def before_feature(context, feature):
#     # # -- SET LOG LEVEL: behave --logging-level=ERROR ...
#     # # on behave command-line or in "behave.ini".
#     # print ('ini before all')
#     src = (s for s in feature.scenarios
#                 if type(s) == behave.model.ScenarioOutline
#                 and 'dynamic' in s.tags )
#
#     #Access the Data from data releng query
#     # data_releng  = q.query_mysql(context.feature.filename)
#     # print('filename {}'.format(context.feature.filename))
#     service_name = context.feature.filename
#     task_id      = '-'.join(service_name.split('-')[0:1])
#     # print('task id {}'.format(task_id))
#     data_releng = Ut.query_mysql(config=Definition.qa_project_report_db, task_id="GX-1846")
#     # context.feature.data_releng = data_releng
#     print(data_releng)
#     '''
#     {
#         'scenario_id' : {
#             'scenario_name' : <something>,
#             'service': <something>,
#             'action': <something>,
#             'taskid': <something>,
#             'data': {
#                 param1:value1,
#                 param2:value2
#             }
#          },
#         'scenario_name' : ,
#         'scenario_name' : ,
#     }
#     '''
#     list_of_data = []
#     if data_releng == None  :
#         raise Exception("No data were parsed,recheck again in releng webpage")
#     else:
#         # save the list of scenario
#         context.feature.scenario_list = list(data_releng.keys())
#         # print('data releng {}'.format(context.feature.scenario_list ))
#         for scenario_id in context.feature.scenario_list :
#
#             data_dict = copy.deepcopy(data_releng[scenario_id]['data'])
#
#             # will be modified
#             # data_dict =  Ut.json2dict(Ut.dict2json(data_json))
#
#             # Added scenario name
#             data_dict['scenario_name'] = data_releng[scenario_id]['scenario_name']
#
#             # [{json1},{json2},{json3}]
#             list_of_data.append(data_dict)
#
#     # print('list_of_data = {}'.format(list_of_data))
#     # looping over test case
#     for test in src:
#         #looping over table each test case
#         for test_table in test.examples:
#             default = copy.deepcopy(test_table.table.rows[0])
#             test_table.table.rows = []
#
#             #looping over data list , type(data) = dict
#             for data in list_of_data:
#                 #{"a": "1", "b": "2", "c": "3", "d": "4"}
#                 data_dict_test = copy.deepcopy(data)
#                 n = copy.deepcopy(default)
#
#                 row = [data_dict_test[x] for x in test_table.table.headings]
#
#                 # insert a row
#                 n.cells = copy.deepcopy(row)
#
#                 test_table.table.rows.append(n)
#
#             print('Headings\t: {}'.format(test_table.table.headings))
#             [print('Rows\t\t:{}'.format(list(x)) ) for x in test_table.table.rows]
