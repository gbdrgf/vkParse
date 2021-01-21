import requests
import time
import csv


def take_1000_posts():
    token = 'dfc702c3dfc702c3dfc702c39edfb78481ddfc7dfc702c3bfce3bbc8f63f51c5d320afa'
    version = 5.126
    domain = 'molotfitness'
    offset = 0
    count = 100
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts


def file_writer(all_posts):
    with open('molotfitness.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
                a_pen.writerow((post['likes']['count'], post['text'], img_url))
            except:
                pass


all_posts = take_1000_posts()
file_writer(all_posts)
