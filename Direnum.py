
import requests 
import sys 

dir_list = open(sys.argv[2]).read() 
directories = dir_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    request = requests.get(dir_enum)
    if request.status_code == 404: 
        pass
    else:
        print("Valid directory: " ,dir_enum)

