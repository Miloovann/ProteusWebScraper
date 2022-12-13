import requests, datetime, json, time

'''Proteus Website URL: https://www.proteus-ranks.com/'''

signa = ["hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMY1x0iqfEX0oyfShF9pcyoyQfUPv7XMU0NSRgl6ja5cOE=", 
         "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYCC9eABenak9OUpK1spSbJrL8/41xDwNMacocIrnebfo=", 
         "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYnO/7shm+wR0nVVRLdUJQhqE9gjI/fKz7MIUmHRjRy3s=", 
         "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYDCz66NuIhI0heOMI+B54zXm5ou5kTJghEZI0IGyd/sQ="]
signb = ["hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMY0+hpEKa5ZehEJWNZsGsXvkIW6r0lFLv3IrTQPwlJuOI="
, "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYe2RVap5GHeFGi7uAywwR/ktgloIkEZe8zQ15MgQTiMs="
, "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYzhvw/aggf4k3TBxdpXsfLOoL1s+T9nwE5JMRnx9BXK4="
, "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYU4MNq+eQINZ80h2Mxp3fAPO4JFtl+ANGME30F5EANbs="]
signc = ["hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYuZHc1fiZgTc/lhRIQ9pMiRCOfBrMNj/xwCt1fSp7c1c="
, "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMY/ZfM9kxHRGVMxsB6x3p5LqvYjQD+E3l+h/CKw3c1qYg="
, "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYxV1wvta02G95PBaypxdDUpA2jpCXPrffW4zXcXIv7MU="
, "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYckQ4hSdRLJxZzrcbFPje7R8DLScHQAdYLJYhWPRmPrY="]
signd = ["hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYmsEJedKWKC0Lnddp/ei4hXm5ou5kTJghEZI0IGyd/sQ=",
            "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYlyE8KD6sN3Ns33SdNul8+zgIyTrvadw87Z7OyIDmGo0=",
            "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYBRXVTXM+5EFzaZEM9TYIElTJ8NAViCcu4YvGgIm4nTI=",
            "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYCJ7K37k6q7TtkgmvWMaZukIW6r0lFLv3IrTQPwlJuOI="]
signe = ["hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYsucjmX2N1q4dLomuadJRneg87bxEQ1/0KUXlzDGyNR0=",
             "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYCugi6+u1oaqNVGeYT26t60wSIKDzc/bbjcRl2IppPjc=",
             "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYH3gOwNICIc5aHJNa2YZQoKE9gjI/fKz7MIUmHRjRy3s=",
             "hI0ZRK5a8B3egZMW/qejlVj+TAyhZVBxwCcmgz8ALU3EZwV2avHVFwH1A5BhSDMYUyE91gJ+Y7hNpVrU7S1fD9RY9J6pv8YLozdfNAamv1Q="]

def main(sign11, sign22, sign33, sign44):
    print("\n\n")
    print(datetime.datetime.now().strftime("%I:%M"), "\n")
    

    '''Part 1: Extract Token, Login Part 1'''
    target_url1 = "https://admin.proteusio.net/api/login/login" 
    headers = {"Referer" : target_url1,"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    payload1 = {"requesTime":1670910315225,"phone":"minimac","password":"e28d4dfb7c8ea29071519f51809fbf39"} ##use own username and password
    login = requests.post(target_url1, payload1, headers = headers)
    textextract = login.content.decode("utf8")
    token = json.loads(textextract)["data"]["userInfo"]["token"]
    print("Login Status Code:", login.status_code)
    


    '''Part 2: send Post Request to getIndex, Login Part 2'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json;charset=utf-8',
        'aeskey': 'bc9mvyytmuftyf1d',
        'apptype': 'macos',
        'device': 'PC',
        'version': '1.0.0',
        'Origin': 'https://www.proteus-ranks.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Referer': 'https://www.proteus-ranks.com/',
    }
    headers['sign'] = sign11

    json_data = {
        'requesTime': 1670915696003,
        'userid': 'F6OSWL', ##use own userid
        'token': token,
    }
    getIndexUrl = 'https://admin.proteusio.net/api/User/getIndex'
    getIndexResp = requests.post(getIndexUrl, headers=headers, json=json_data)
    print("getIndex Status Code:", getIndexResp.status_code)

    
    
    '''Part 3: send Post Request to getGoods, Automate Part 1'''
    headers['sign'] = sign22
    
    getGoodsUrl = "https://admin.proteusio.net/api/User/getGoods"
    getGoodsResp = requests.post(getGoodsUrl, headers=headers, json=json_data)
    print("getGoods Status Code:", getGoodsResp.status_code)
    textextract = getGoodsResp.content.decode("UTF8")
    extract = dict(eval(textextract))
    OrderID = extract["data"]["id"]
        
    

    '''Part 4: send Post Request to submitGoodsOrder, Automate Part 2'''
    headers['sign'] = sign33
    
    json_data["order_id"] = OrderID
    submitGoodsUrl = 'https://admin.proteusio.net/api/User/submitGoodsOrder'
    submitGoodsResp = requests.post(submitGoodsUrl, headers=headers, json=json_data)
    print("submitGoods Status Code:", submitGoodsResp.status_code)
    
    
    
    
    '''Part 5: send Post Request to initStartData, Automate Part 3'''
    headers['sign'] = sign44
    
    del json_data["order_id"]
    initStartUrl = 'https://admin.proteusio.net/api/User/initStartData'
    initStartResp = requests.post(initStartUrl, headers=headers, json=json_data)
    print("initStart Status Code:", initStartResp.status_code)
        

while True:
    lis = signa
    main(lis[0], lis[1], lis[2], lis[3])

    lis = signb
    main(lis[0], lis[1], lis[2], lis[3])

    lis = signc
    main(lis[0], lis[1], lis[2], lis[3])

    lis = signd
    main(lis[0], lis[1], lis[2], lis[3])
    
    lis = signe
    main(lis[0], lis[1], lis[2], lis[3])


    time.sleep(80)