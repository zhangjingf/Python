import requests
from aip import AipOcr

image = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1564424250231&di=b0a3691acea62f65ec8bebd3c0d1d5a4&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201511%2F20%2F20151120222642_hmyY2.jpeg').content

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