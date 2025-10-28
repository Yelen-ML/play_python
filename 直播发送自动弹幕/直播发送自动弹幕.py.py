import requests
import random
import time
while True:
    time.sleep(random.randint(1, 5))
    lis=['666','主播真棒','支持主播']
    word=random.choice(lis)
    url = "https://api.live.bilibili.com/msg/send?web_location=444.8&w_rid=aab7598734a24c9d0fe91c6350cd9912&wts=1761649816"
    data={
        #对应的网络负载表单数据自行替换
        'bubble':'0',
        'msg':word,
        'color':'16777215',
        'mode':'1',
        'room_type':'0',
        'jumpfrom':'71003',
        'reply_mid':'0',
        'reply_attr':'0',
        'statistics':'{"trackid":"live_feed_0.router-live-2231394-2cb94.1761649643521.942"}',
        'reply_type':'0',
        'data_extend':'{"trackid":"-99998"}',
        'fontsize':'25',
        'rnd':'1761652557',
        'roomid':'32076423',
        'csrf':'a5e918c489212be29bb9942a94ad979d',
        'csrf_token':'a5e918c489212be29bb9942a94ad979d',
    }
    headers = {
        #对应的网络请求头自行替换
        'cookie':'enable_web_push=DISABLE; header_theme_version=CLOSE; enable_feed_channel=DISABLE; home_feed_column=5; browser_resolution=1536-837; CURRENT_FNVAL=4048; theme-tip-show=SHOWED; LIVE_BUVID=AUTO9317605996696161; buvid3=BE3F3961-9DD5-4E77-351D-8B64FEC4358B40757infoc; b_nut=1760867240; buvid4=766C395F-B6C6-605D-8ADC-A2F991C063CD41455-025101917-DUR3IsvHB5pgjLekHBmrDYEkaSStmtoTdaWZoqGKLQmx0wXkp1GmCLH8hBfSIX3y; b_lsid=FE3227D9_19A2A803914; bsource=search_bing; _uuid=A12DDD3E-B46A-32101-B354-DF27B184DBB937659infoc; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjE5MDg4NDMsImlhdCI6MTc2MTY0OTU4MywicGx0IjotMX0.GorNcEg9NWBPnlMoNUETHBEvdcKyaUAszdPowY2F79c; bili_ticket_expires=1761908783; fingerprint=4ed154e7f677035ffe874e44e4071930; buvid_fp_plain=undefined; SESSDATA=800bee10%2C1777201761%2Cdfce8%2Aa2CjDtxtbFbIbsPWwlHEyyR4V4sBnXhouAslAIywJkh5Og4AcHM-XWVbjk01NzzrRPWNASVnBKSVJsVjdWSHEtbXY1V0VEUVhVVm9Gc2VGTWlCQTRhdkQ3N0ZGR1ZtMXE5YXFqdi1UYnpXclpiWTU3OW50VXFTc0tBOEJHQkcwOGRGN29vbnZWc05BIIEC; bili_jct=a5e918c489212be29bb9942a94ad979d; DedeUserID=3493270055291502; DedeUserID__ckMd5=5f0fe4589ce21684; sid=8kulugnc; buvid_fp=48144494699cfca66dbf51d264907ed2; PVID=3',
        'origin':'https://live.bilibili.com',
        'priority':'u=1, i',
        'referer':'https://live.bilibili.com/blanc/8016907?liteVersion=true',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-site',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15 Edg/141.0.0.0',
    }
    response = requests.post(url=url, headers=headers, data=data)
    print(response.status_code)