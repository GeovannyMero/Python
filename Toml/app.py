print('hello')

import tomllib

data = None

with open('config.toml', 'rb') as f:
    data = tomllib.load(f)

print(data['user']['name'])
