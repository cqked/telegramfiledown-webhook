import json

import jsonpath

text = '{"update_id":738111156,"message":{"message_id":686,"from":{"id":5091164508,"is_bot":false,"first_name":"\u4e09\u5c94\u53e3","language_code":"zh-hans"},"chat":{"id":5091164508,"first_name":"\u4e09\u5c94\u53e3","type":"private"},"date":1664994521,"forward_from_chat":{"id":-1001191878539,"title":"\u5403\u74dc\u4e2d\u5fc3","username":"chigua91","type":"channel"},"forward_from_message_id":90292,"forward_date":1664930417,"photo":[{"file_id":"AgACAgEAAxkBAAICrmM9zNkef0gFgjJm7PrK6sa-BhSvAAKUqjEbAAGN6EWUk1c6knHfRQEAAwIAA3MAAykE","file_unique_id":"AQADlKoxGwABjehFeA","file_size":1728,"width":67,"height":90},{"file_id":"AgACAgEAAxkBAAICrmM9zNkef0gFgjJm7PrK6sa-BhSvAAKUqjEbAAGN6EWUk1c6knHfRQEAAwIAA20AAykE","file_unique_id":"AQADlKoxGwABjehFcg","file_size":31259,"width":240,"height":320},{"file_id":"AgACAgEAAxkBAAICrmM9zNkef0gFgjJm7PrK6sa-BhSvAAKUqjEbAAGN6EWUk1c6knHfRQEAAwIAA3gAAykE","file_unique_id":"AQADlKoxGwABjehFfQ","file_size":143111,"width":600,"height":800},{"file_id":"AgACAgEAAxkBAAICrmM9zNkef0gFgjJm7PrK6sa-BhSvAAKUqjEbAAGN6EWUk1c6knHfRQEAAwIAA3kAAykE","file_unique_id":"AQADlKoxGwABjehFfg","file_size":310865,"width":960,"height":1280},{"file_id":"AgACAgEAAxkBAAICrmM9zNkef0gFgjJm7PrK6sa-BhSvAAKUqjEbAAGN6EWUk1c6knHfRQEAAwIAA3cAAykE","file_unique_id":"AQADlKoxGwABjehFfA","file_size":360913,"width":1080,"height":1440}]}}'
text1 = json.dumps(text)
print(str(text1))
print(jsonpath.jsonpath(f'{text1}', '$..message'))
