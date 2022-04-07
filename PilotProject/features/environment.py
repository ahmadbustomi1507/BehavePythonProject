import behave
import copy
from tools import Utility as Ut


#example
def get_data_releng():

    return [ \
           ['nama testnya',{"MSISDN_Target": "1", "MSISDN_RO":"2", "Voucher" : "3","HRN": "4"}],
            ['nama testnya', {"MSISDN_Target": "3", "MSISDN_RO": "4", "Voucher": "3", "HRN": "4"}],
            ['nama testnya', {"MSISDN_Target": "2", "MSISDN_RO": "2", "Voucher": "1", "HRN": "4"}],
    ]


def before_feature(context, feature):
    # # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # # on behave command-line or in "behave.ini".
    # print ('ini before all')
    features = (s for s in feature.scenarios
                if type(s) == behave.model.ScenarioOutline
                and 'dynamic' in s.tags )

    #Access the Data from data releng
    data_releng  = get_data_releng()

    list_of_data = []
    if data_releng == None  :
        raise Exception("No data were parsed,recheck again in releng webpage")
    else:
        #data_releng will be a dictionary
        for data in data_releng :

            data_json = copy.deepcopy(data[1])

            # will be modified
            data_dict =  Ut.json2dict(Ut.dict2json(data_json))

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

            print('Headings\t: {}'.format(test_table.table.headings))
            [print('Rows\t\t:{}'.format(list(x)) ) for x in test_table.table.rows]
