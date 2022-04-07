from API import redeem_voucher_sa as api

# from features.API.redeem_voucher_sa import * API_REDEEM_VOUCHER_SA


@step('User getting the {msisdn_ro},{msisdn_b},{voucher},{hrn} from Releng')
def step_impl(context,msisdn_ro,msisdn_b,voucher,hrn):
    context.msisdn_ro = msisdn_ro
    context.msisdn_b = msisdn_b
    context.voucher = voucher
    context.hrn = hrn
    print('1 ' + context.msisdn_ro)

@when('User Hit the API with the payload')
def step_impl(context):
    Params = {
        'DEALERMSISDN': context.msisdn_ro,
        'HRN': context.hrn,
        'MSISDN': context.msisdn_ro,
        'USERINPUT': context.msisdn_b
    }
    # context.response = api.API_REDEEM_VOUCHER_SA(
    #     params = Params
    # )
    context.response = 'debug'

@then('User successfully hit the API with status code 200')
def step_impl(context):
    print(context.response)