import behave
import copy

def before_feature(context, feature):
    # # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # # on behave command-line or in "behave.ini".
    # print ('ini before all')
    features = (s for s in feature.scenarios
                if type(s) == behave.model.ScenarioOutline
                and 'dynamic' in s.tags )

    for s in features:
        for e in s.examples:
            default = copy.deepcopy(e.table.rows[0])
            e.table.rows = []

            # insert a row
            n = copy.deepcopy(default)
            n.cells = ['628176677807','6281808030805','0004550000010050','4678009180739283']
            e.table.rows.append(n)

            # n = copy.deepcopy(default)
            # n.cells = ['msisdnro_1','msisdn_target_2','Voucher_1','HRN_1']
            # e.table.rows.append(n)

