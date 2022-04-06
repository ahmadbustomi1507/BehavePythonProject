from behave import *
import requests
import json

API_URL = "https://gorest.co.in/public/v1/posts"

class response_builder(object):
    post_id         = 0
    user_id         = 0
    title           = 'title'
    body            = 'body'
    Bearer_token    = 'Bearer <insert your token here>'

post = response_builder()
post.title = "Automation test 15/01/2022"
post.body = "This is just a random post for an automation with BDD approach"


@given('Successfully registered new user_id "{user_id}"')
def step_impl(context,user_id):
    post.user_id = user_id

@when('User create a new post')
def step_impl(context):

    input = {
        "user_id":post.user_id,
        "title": post.title ,
        "body": post.body
    }

    context.r = requests.post(API_URL,json=input,headers={'Authorization':post.Bearer_token})

@then('POST success with reponse code "{response}"')
def step_impl(context,response):
    if context.r.status_code == response:
        assert True , "Response code {}, success create a post".format(response)

    data = context.r.json()['data']

    #get the post id
    post.post_id    = data['id']

    #assertion for title and body
    if data['title'] in post.title:
        assert True, "Title match"
    if data['body'] in post.body:
        assert True, "Body/content match"


@when('User get the created post')
def step_impl(context):
    context.r = requests.get(API_URL+'/?id'.format(post.post_id),headers={'Authorization':post.Bearer_token})


@then('GET success with response code "{response}"')
def step_impl(context,response):
    if context.r.status_code == response:
        assert True, "Response code {}, success get the post".format()

    # this will return array of nested json
    list_data = context.r.json()['data']
    for data in list_data:
        if data['id']  == post.post_id:
            #assertion for title and body
            if data['title'] in post.title:
                assert True, "Title match"
            if data['body'] in post.body:
                assert True, "Body/content match"
            break
        else:
            continue

@when('User update the created post')
def step_impl(context):

    post.body  = "[modified] This is just a random post for an automation with BDD approach"

    input = {
        "user_id":post.user_id,
        "title": post.title ,
        "body": post.body
    }

    context.r = requests.put(API_URL +'/{}'.format(post.post_id),json=input,headers={'Authorization':post.Bearer_token})


@then('PUT success with response "{response}"')
def step_impl(context, response):


    if context.r.status_code == response:
        assert True, "Response code {}, success get the post".format(response)

    # this will return array of nested json
    data = context.r.json()['data']
    if data['title'] in post.title:
        assert True, "Title match"
    if ("[modified] This is" in data['body']) and (post.body in data['body'] ):
        assert True, "Body/content match"


@when('User delete the created post')
def step_impl(context):
    context.r = requests.delete(API_URL +'/{}'.format(post.post_id),headers={'Authorization':post.Bearer_token})


@then('DELETE success with response "{response}"')
def step_impl(context,response):
    if context.r.status_code == response:
        assert True, "Response code {}, success get the post".format(response)
