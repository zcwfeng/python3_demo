import requests

# r = requests.get('https://www.douban.com/') # 豆瓣首页
# print(r.status_code)
# print(r.text)


# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
#
# print(r.url)
# print(r.encoding)
# print(r.content)

#
# r = requests.post('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())


# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)


# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'zcwfeng@126.com', 'form_password': 'qwly@douban@tyf'})
# print(r.status_code)
# print(r.text)



# 获取ip的方法
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(response.json()['origin']))
