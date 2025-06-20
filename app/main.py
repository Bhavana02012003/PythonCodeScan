import os

def insecure_function():
    password = input("Enter password: ")  # 🚨 Bandit: B322
    os.system(f"echo {password}")  # 🚨 Bandit: B602

def unused_function():  # 🚨 Pylint: function defined but not used
    print("This does nothing")

insecure_function()
