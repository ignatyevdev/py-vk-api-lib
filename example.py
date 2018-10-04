from vk_api import api

result = api.call_method('users.get', user_id = '1', access_token="YOUR_ACCESS_TOKEN", v = "API_VERSION")
user = result[0]

print(user.first_name + " " + user.last_name)
