from src.api_builder import  api_v1_get_users
from resource import utility

@given(u'user have an access to the API')
def step_impl(context):
    print("User have an acess to the API")

@when(u'user send request with payload')
def step_impl(context):
    payload      = utility.string2dict(context.text)
    base_url    = context.base_url
    path        = "api/v1/users/1"
    context.response = api_v1_get_users.api_get_users(
        base_url= base_url,
        path    = path,
        payload = payload
    )

@then(u'user will get response status code "{status}"')
def step_impl(context,status):
    #check the status code
    assert (context.response.status_code == int(status)),f"result status code {status}, different"

@then(u'user get list of the users')
def step_impl(context):
    response_dict = utility.string2dict(context.response.text)
    #check name exist
    assert "name" in response_dict.keys(),"name is not in the response"
    #check name createdAt
    assert "createdAt" in response_dict.keys(),"createdAt is not in the response"
    #check avatar exist
    assert "avatar" in response_dict.keys(),"avatar is not in the response"