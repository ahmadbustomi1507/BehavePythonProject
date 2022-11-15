import tomli
import os

def get_credential(user:str ):
    curr_path = os.path.dirname(os.path.realpath(__file__))
    cre_path  = os.path.join(curr_path,"credential.toml")
    with open(cre_path, mode="rb") as cre:
        config = tomli.load(cre)
        cre.close()
    return config['user'][user]

# print(get_credential('user_test'))
