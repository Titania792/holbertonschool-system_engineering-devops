#!/usr/bin/python3
""" extend your Python script to export info in the JSON format """


if __name__ == "__main__":
    import json
    import requests

    api_url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(api_url).json()
    dict = {}
    for user in response:
        name = user.get('username')
        u_id = str(user.get('id'))
        api_url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"\
            .format(u_id)
        resp = requests.get(api_url2).json()
        tasks = [task for task in resp]
        dict[u_id] = []
        for info in tasks:
            t_dic = {"task": info.get('title'), "completed": info.get('completed'),
                     "username": name}
            dict.get(u_id).append(t_dic)
    with open("todo_all_employees.json", 'w', encoding='utf-8') as f:
        json.dump(dict, f)
