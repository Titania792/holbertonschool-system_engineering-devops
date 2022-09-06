#!/usr/bin/python3
""" script that returns information about an employee TODO
list progress using an API """


if __name__ == '__main__':
    import requests
    from sys import argv

    u_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(u_id)
    response = requests.get(api_url).json()
    EMPLOYEE_NAME = response.get('name')
    response = requests.get(api_url2).json()
    TOTAL_NUMBER_OF_TASKS = len(response)
    NUMBER_OF_DONE_TASKS = 0
    tasks = []
    for task in response:
        if task.get("completed") is True:
            tasks.append(task.get("title"))
            NUMBER_OF_DONE_TASKS += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in tasks:
        print('\t {}'.format(task))
