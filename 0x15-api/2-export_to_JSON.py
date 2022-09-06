#!/usr/bin/python3
""" extend your Python script to export info in the JSON format """


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    u_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(u_id)
    response = requests.get(api_url).json()
    EMPLOYEE_NAME = response.get('username')
    response = requests.get(api_url2).json()
    f_name = u_id + '.json'
    u_list = []
    with open(f_name, 'w', encoding='utf-8') as f:
        for info in response:
            dic = {"task": info['title'], "completed": info['completed'],
                   "username": EMPLOYEE_NAME}
            u_list.append(dic)
            user = {u_id: u_list}
            f.write(json.dumps(user))
