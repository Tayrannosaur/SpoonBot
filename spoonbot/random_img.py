import random

import httpx

def gen_params(query, offset):
    return {'q': query,
            'count': '1',
            'offset': offset,
            't': 'images',
            'safesearch': '1',
            'locale': 'en_US',
            'uiv': '4'}

user_agent = """
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
"""

headers = {'User-Agent': user_agent}

url = 'https://api.qwant.com/api/search/images'

async def random_img(query):
    """Will fetch a random image from qwant.com based on your query"""
    offset = random.randint(1, 250)
    params = gen_params(query, offset)

    result = await httpx.get(url, params=params, headers=headers)
    data = result.json()
    if (data['status'] == 'success'):
        return data['data']['result']['items'][0]['media']
    else:
        return random_img(query)
