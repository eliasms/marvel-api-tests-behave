import os
from datetime import datetime
import hashlib

def get_var_from_environment(var_env):
    envirionment_variable = os.environ[var_env]
    return envirionment_variable

def get_timestamp():
    timestamp = ts = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    return timestamp

def make_a_hash(*args, sep = ""):
    pre_hash = sep.join(args)
    hash = hashlib.md5(pre_hash.encode('utf-8')).hexdigest()
    return hash
