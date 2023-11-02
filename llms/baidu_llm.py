# import requests
# import json
#
# API_KEY = "Uc9dT2jnsVPch3CzjdGbYtPh"
# SECRET_KEY = "lVN9c9A7KcM2Gp1OwMo1KTxIswPm2bkz"
#
#
# def predict(prompt):
#     url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
#
#     payload = json.dumps({
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
#
#
# def get_access_token():
#     """
#     使用 AK，SK 生成鉴权签名（Access Token）
#     :return: access_token，或是None(如果错误)
#     """
#     url = "https://aip.baidubce.com/oauth/2.0/token"
#     params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
#     return str(requests.post(url, params=params).json().get("access_token"))
#
#
# if __name__ == '__main__':
#     prompt = "You are an excellent English teacher.\nFor 'Oooooh', you need to rate the word in terms of necessity to memorize, from 0 to 10, with 0 indicating not necessary or not worth learning at all, and 10 indicating very worth learning.\nYour reply should only be an integer, without explaining the reason.\n"
#     print(predict(prompt))


import requests
import json, os

API_KEY = os.environ["ba"]
SECRET_KEY = os.environ["bs"]

def predict(content):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/bloomz_7b1?access_token=" + get_access_token()

    payload = json.dumps({
        "user_id": "2",
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "temperature": 0.1
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return json.loads(response.text)["result"].strip()

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    prompt = "You are an excellent English teacher.\nFor 'Oooooh', you need to rate the word in terms of necessity to memorize, from 0 to 10, with 0 indicating not necessary or not worth learning at all, and 10 indicating very worth learning.\nYour reply should only be an integer, without explaining the reason.\n"
    print(predict(prompt))