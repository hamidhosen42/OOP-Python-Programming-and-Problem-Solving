import requests

api_url = "https://restcountries.com/v3.1/all"

def get_response(url):
    return requests.get(url)

if __name__ == "__main__":
    res = get_response(api_url)
    # print(__name__)
    print(res)

# print("Hey Baby")