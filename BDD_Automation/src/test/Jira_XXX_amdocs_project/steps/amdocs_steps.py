# from API import api_amdocs_cm as api
#
# params= {
#     'msisdn' :'6287875736063',
#     'allowCancel' : 'N'
# }
import allure
import logging
@given('something')
def step_impl(context,MSISDN):
    print('do something')

@given('User getting the MSISDN : {MSISDN}')
def step_impl(context,MSISDN):
    logging.info('User getting the MSISDN')
    # print('msisdn {}'.format(MSISDN))


@when('User Hit the API with the payload')
def step_impl(context):


    @allure.step('Send payload as {}'.format('12345'))
    def Hit_API():
        assert True
        allure.attach("some random text",
                      'nama_file.txt', allure.attachment_type.TEXT)

    @allure.step('Validate as {}'.format('12345'))
    def Validate_API():
        assert False, 'this is only an example of assertion'

    @allure.step('some random step')
    def attach():
        allure.attach("{'key1':'value1'}",'nama_file2.json', allure.attachment_type.JSON)

    Hit_API()
    Validate_API()
    attach()

@then('User successfully hit the API with status code 200')
def step_impl(context):
    print('then success')
