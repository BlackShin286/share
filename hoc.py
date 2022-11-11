import os
import requests
from time import sleep
import sys
import threading
os.system('cls')
cookie = input('Cookie : ')
idpost = input('ID Post : ')
share = int(input('So Luong :'))
delay = int(input('Delay : '))
def MainShare(idpage):
    hd_log = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
    response = requests.get('https://mbasic.facebook.com/',headers=hd_log).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': f'https://www.facebook.com/{idpost}',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'viewport-width': '723',
        'x-fb-friendly-name': 'useCometFeedToFeedReshare_FeedToFeedMutation',
    }

    data = {
        'av': idpage,
        'dpr': '1',
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useCometFeedToFeedReshare_FeedToFeedMutation',
        'variables': '{"input":{"attachments":{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+idpost+']}"}},"audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},"is_tracking_encrypted":true,"navigation_data":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1668168930732,571255,,"},"source":"www","tracking":["AZX6_qk4YKdcAUZKHIhRgf_1HElZVihNHf1LGYob2VA-FpIPFvsxbQdh4QKx1psroDPlli000Isbil_5WaL-MVKG2sW-2diHNUtGuGQTwJ7dyZpco4vK7v0Fx7GIYfc2uLZdX6JkOmcbDy2TG2bk-iaF6OtmqbRf1TFFerVFdOVlZbQHPqiRbyJq-am2t0KdG56T4Mme2TFjpLYv05YP6Zu0hgJQucGt0vcpmKFyAr2EHTP-MAk7Rrwfx2hj5fo95Nq9qkS5t_QApxkoghPdUt0VtxnZwu1Nyc0ZNU58F4eNDCx5rNZxSD5TmxMNBX3KpSYhz5sK9BrelP7am7l5akjixraHRH-kxMADcF6OOfWsfzaqckXKGFS4BKY0CLCrDv0"],"actor_id":"'+idpage+'","client_mutation_id":"1"},"renderLocation":"homepage_stream","scale":1,"privacySelectorRenderLocation":"COMET_STREAM","useDefaultActor":false,"displayCommentsContextEnableComment":null,"feedLocation":"NEWSFEED","displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedbackSource":1,"focusCommentID":null,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery"}',
        'server_timestamps': 'true',
        'doc_id': '4026767267447619',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
    print(f'Success ! Share ID : {idpage}_{idpost}')
    sleep(delay)
token = input('Token ( EAAB... ) : ')
headers = {
    'authority': 'graph.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': cookie,
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

response = requests.get(f'https://graph.facebook.com/me?fields=facebook_pages.limit(1000){{additional_profile_id}}&access_token={token}', headers=headers).json()
for i in range(share):
    for line in response['facebook_pages']['data']:
        idpage = line['additional_profile_id']
        threading.Thread(target=MainShare, args=(idpage,)).start()
















































'''def MainViewPage(idpage):
    hd_log = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi-VN,vi;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get('https://mbasic.facebook.com/',headers=hd_log).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/dthinh.06',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'viewport-width': '702',
        'x-fb-friendly-name': 'CometUserFollowMutation',
    }

    data = {
        'av': idpage,
        'dpr': '1',
        'fb_dtsg': 'NAcOUBDlVixKTzVYFSzXYdoVdMJOORhJEJbO2mqryYuDlbO_RLs8N6g:35:1668005977',
        'jazoest': '25627',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometUserFollowMutation',
        'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1668056606356,767099,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"100082234812595","actor_id":"'+idpage+'","client_mutation_id":"1"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5032256523527306',
    }
    response = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
    print(response)
cookie = input('Cookie : ')
link = input('Link Story : ')
bucket_id = link.split('https://www.facebook.com/stories/')[1].split('/')[0]
print(bucket_id)
story_id = link.split(f'https://www.facebook.com/stories/{bucket_id}/')[1]
print(story_id)
id_page = open('idpage.txt','r').readlines()
for idpage in id_page:
    MainViewPage(idpage)'''