from flask_httpauth import HTTPBasicAuth
from flask import g




auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email, password):
    if email == "":
        g.current_user_ = ""
        return True
    user = "gmero"
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)
