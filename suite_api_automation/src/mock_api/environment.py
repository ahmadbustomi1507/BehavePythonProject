import datetime


def before_all(context):
    #Get the base url from behave.ini
    context.base_url = context.config.userdata["base_url"].lower()
    context.tester_name     = "Tomi"

def before_feature(context,feature):
    print(f"Currently running feature test of :{context.feature.name}")
    print(f"Desc\t:{context.feature.description}")
    print(f"Tester\t:{context.tester_name}")
    print(f"Date\t:{datetime.datetime.now()}\n\n")

def after_feature(context,feature):
    pass

def before_scenario(context,scenario):
    pass

def after_scenario(context,scenario):
    pass

def before_step(context,step):
    pass

def after_step(context,step):
    pass
