
from tools import settings
import allure
import allure_commons


@allure_commons.fixture
def before_feature(context,feature):
    print('ini versi terbaru before feature')
    allure.attach("before feature",
                  'data.txt', allure.attachment_type.TEXT)

@allure_commons.fixture
def before_scenario(context,feature):
    print('ini versi terbaru before scenario')
    allure.attach("before scenario",
                  'data.txt', allure.attachment_type.TEXT)
    allure.dynamic.link("http://qameta.io")
    allure.dynamic.issue("http://example.com")

@allure_commons.fixture
def after_feature(context,feature):
    print('ini versi terbaru after feature')
    allure.attach("after feature",
                  'data.txt', allure.attachment_type.TEXT)

@allure_commons.fixture
def after_scenario(context,feature):
    print('ini versi terbaru after scenario')
    allure.attach("after scenario",
                  'data.txt', allure.attachment_type.TEXT)

# # @AllureHooks.before_feature(context, feature)
# def before_feature(context, feature):
#     @allure_commons.fixture
#     def before_feature(context):
#         allure.attach("before feature",
#                            'data.txt', allure.attachment_type.TEXT)
#
#     @allure_commons.fixture
#     def before_scenario(context):
#         allure.attach("before scenario",
#                       'data.txt', allure.attachment_type.TEXT)
#     before_feature(context)
#     before_scenario(context)
    # context.feature.rpl_amdocs =  ''
    # @allure.step('before step')
    # def preparing_the_data():
    #     allure.attach("data is being prepared",
    #                   'data.txt', allure.attachment_type.TEXT)
    #
    # preparing_the_data()
    # pass
    # return settings.initialized(context, feature)


# def after_feature(context, feature):
#     @allure_commons.fixture
#     def after_feature(context):
#         allure.attach("after feature",
#                       'data.txt', allure.attachment_type.TEXT)
#
#     @allure_commons.fixture
#     def after_scenario(context):
#         allure.attach("after scenario",
#                       'data.txt', allure.attachment_type.TEXT)
#
#     after_feature(context)
#     after_scenario(context)
#     # print(context.log_capture)
#     # return settings.post_test(context,feature)
