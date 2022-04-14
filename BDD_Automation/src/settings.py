import behave
import copy
from tools import Utility as Ut
from tools import Definition as Definition
import os

def post_test(context, feature):
    print ('------------END THE PROJECT ---------------------')
    return True

def initialized(context, feature):
    print ('------------START THE PROJECT ---------------------')
    # features = (s for s in feature.scenarios
    #             if type(s) == behave.model.ScenarioOutline
    #             and 'dynamic' in s.tags )

    # on going parsing the feature name and extract the jira number to query from releng
    feature_name                 = os.path.basename(context.feature.filename)
    # context.feature.feature_name = feature_name
    task_id                      = '-'.join(feature_name.split('_')[0:2])

    for s in feature.scenarios:
        if type(s) == behave.model.ScenarioOutline and 'dynamic' in s.tags:

            # Query the Data from data releng query
            data_test = Ut.query_mysql(config=Definition.qa_project_report_db, task_id=task_id)

            test = {}
            for x in data_test.keys():
                test_id       = copy.deepcopy(x)
                test[x] = data_test[test_id]['scenario_name']

            context.feature.data_environtment = {
                'feature_name': feature_name,
                'env': 'http://roaming-vas-sit.api.devgcp.excelcom.co.id/',
                'test' : test
            }

            list_of_data = []
            if data_test == None  :
                raise Exception("No data were parsed,recheck again in releng webpage")
            else:
                # save the list of scenario
                context.feature.scenario_list = list(data_test.keys())
                # print('data releng {}'.format(context.feature.scenario_list ))
                for scenario_id in context.feature.scenario_list :

                    data_dict = copy.deepcopy(data_test[scenario_id]['data'])

                    # Added scenario name
                    data_dict['scenario_name'] = data_test[scenario_id]['scenario_name']

                    # [{json1},{json2},{json3}]
                    list_of_data.append(data_dict)

            # looping over test case
            for test in features:
                #looping over table each test case
                for test_table in test.examples:
                    default = copy.deepcopy(test_table.table.rows[0])
                    test_table.table.rows = []

                    #looping over data list , type(data) = dict
                    for data in list_of_data:
                        #{"a": "1", "b": "2", "c": "3", "d": "4"}
                        data_dict_test = copy.deepcopy(data)
                        n = copy.deepcopy(default)

                        row = [data_dict_test[x] for x in test_table.table.headings]

                        # insert a row
                        n.cells = copy.deepcopy(row)

                        test_table.table.rows.append(n)

                    # print('Headings\t: {}'.format(test_table.table.headings))
                    # [print('Rows\t\t:{}'.format(list(x)) ) for x in test_table.table.rows]
        else:
            pass
