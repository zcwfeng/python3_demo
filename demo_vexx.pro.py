# -*-coding=utf-8-*-

import requests
session = requests.Session()
user = ''
password = ''

def getCode():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    url = 'http://vexx.pro/verify/code.html'
    s = session.get(url=url, headers=headers)

    with open('code.png', 'wb') as f:
        f.write(s.content)

    code = raw_input('input the code: ')
    print 'code is ', code

    login_url = 'http://vexx.pro/login/up_login.html'
    post_data = {
        'moble': user,
        'mobles': '+86',
        'password': password,
        'verify': code,
        'login_token': ''}

    login_s = session.post(url=login_url, headers=header, data=post_data)
    print login_s.status_code

    zzc_url = 'http://vexx.pro/ajax/check_zzc/'
    zzc_s = session.get(url=zzc_url, headers=headers)
    print zzc_s.text

def main():
    getCode()

if __name__ == '__main__':
    main()
