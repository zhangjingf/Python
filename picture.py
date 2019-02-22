import requests
from aip import AipOcr

image = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1550825015268&di=203539d4b94cee9172919e787273c31f&imgtype=0&src=http%3A%2F%2Fimg18.3lian.com%2Fd%2Ffile%2F201711%2F13%2F884cf3528b0e5d4142e61bae3c07758a.png').content

APP_ID = '11756541'
API_KEY = '2YhkLuyQGljPUYnmi1CFgxOP'
SECRET_KEY = '4rrHe2BF828bI8bQy6bLlx1MelXqa8Z7'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)

if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])
else:
    print(res)