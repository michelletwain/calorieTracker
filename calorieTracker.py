import requests
import time
import json

def run():
    page = ''
    while page == '':
        try:
            page = requests.get('https://api.api-ninjas.com/v1/nutrition?query={}')
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue



    query = input("Enter the list of food you want to calculate the calories of: ")
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'JUtygfdxhkG8kltgz8/0dA==rsXRXUUcl2bhgkSF'})
    if response.status_code == requests.codes.ok:
        response_dic = json.loads(response.text)

        totalCalories = 0

        for d in response_dic:
            name = d['name']
            calories = d['calories']

            print(str(name) + ": " + str(calories))

            totalCalories = totalCalories + int(calories)

        # print(response_dic)
        print("Total calories: " + str(totalCalories))
    
    else:
        print("Error:", response.status_code, response.text)

run()
