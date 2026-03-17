with open('../data/logs.txt', 'r', encoding='utf-8') as file:
    data = file.read().strip()

    for line in data.split('\n'):

        data, hora, ip, request, status_code, user_agent = line.split('T').split(' - ')


    print(data)
