
from tools import settings as set
import allure
import allure_commons
import copy
import behave

@allure_commons.fixture
def before_feature(context,feature):

    data = set.initialized(context,feature)

    #save it into environtment behave
    context.feature.data_environtment = copy.deepcopy(data)
    dict_data_test = data['test']

    allure.attach('''
    Getting the environtment test as:
        'feature_name'  : {},
        'environtment'  : {},
    '''.format(data['feature_name'],data['env']),'data.txt', allure.attachment_type.TEXT)

    for s in feature.scenarios:
        if type(s) == behave.model.ScenarioOutline and 'dynamic' in s.tags:
            list_of_data = []
            if dict_data_test == None  :
                raise Exception("No data were parsed,recheck again in releng webpage")
            else:
                context.feature.scenario_list = list(dict_data_test.keys())
                for scenario_id in context.feature.scenario_list :
                    data_dict = copy.deepcopy(dict_data_test[scenario_id]['data'])
                    # Added scenario name
                    data_dict['scenario_name'] = dict_data_test[scenario_id]['scenario_name']
                    # [{json1},{json2},{json3}]
                    list_of_data.append(data_dict)

            # fill in the table in the tables of gherkin
            # for test in features:
            #looping over table each test case
            for test_table in s.examples:
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
    allure.attach('{}'.format(list_of_data),'datatest.txt',allure.attachment_type.TEXT)
    print('data test \n{}'.format(list_of_data))

@allure_commons.fixture
def before_scenario(context,feature):
    pass
    # allure.attach('''
    # Executing scenario : {}
    # '''.format(context.feature.data_environtment[]),
    #               'data.txt', allure.attachment_type.TEXT)
    # context.feature.examples
    # allure.dynamic.link("http://qameta.io")
    # allure.dynamic.issue("http://example.com")

@allure_commons.fixture
def after_feature(context,feature):
    pass

@allure_commons.fixture
def after_scenario(context,feature):
    pass