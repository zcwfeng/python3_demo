# from furl import  furl
# f = furl('http://www.google.com/?one=1&two=2')
# f.args['three'] = '3'
# del f.args['one']
# print(f.url)


import pyshorteners

s = pyshorteners.Shortener(api_key='YOUR_KEY', user_id='USER_ID',
                               domain='test.us', group_id=12, type='int')



s.short('http://www.google.com')
