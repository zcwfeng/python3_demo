import urllib3, time

time_start = time.time()
data = []
for i in range(30):
    print('request movie:', i)
    id = 1764798 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib3.connection_from_url(url)
    data.append(d)
    print(i, time.time() - time_start)

print('data:', len(data))
