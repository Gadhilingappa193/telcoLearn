import requests

url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
# print("response",response.json())
datas = {
    "title": "Post the url",
    "body": "abc",
    "query": "hello world",
    "userId": 1
}
response = requests.post(url,data=datas)
print("status code",response.status_code)
print("post response",response.json())


