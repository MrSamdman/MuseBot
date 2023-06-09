import requests

ident = "63794e5461e4cfa046edfbdddfccc1ac16daffd2"
ident2 = "38fb9efaae51b0c83b5bb5791a698b48292129e7"
ident3 = "8c022bdef45341074ce876ae57a48f64b86cdcf5"



cookies = {
    'uwguid': 'WEBLS-b9766a32-65ef-464e-9c1f-4dfcc57be378',
    'mu_browser_bi': '6589667686921956405',
    'mu_browser_uni': '0NBsi6fZ',
    '_mu_unified_id': '1.1686227780.1828271',
    'mu_unregister_user_id': '598798501',
    '_gid': 'GA1.2.1244405920.1686227781',
    '_ym_uid': '168622778137611141',
    '_ym_d': '1686227781',
    '_pbjs_userid_consent_data': '3524755945110770',
    '__gads': 'ID=9fb567920c136c6f:T=1686227783:RT=1686227783:S=ALNI_MbyPz2DqHCp5PGZyUwRxhCWe-hzmQ',
    '__gpi': 'UID=00000c2d51f8e9c2:T=1686227783:RT=1686227783:S=ALNI_MauaVkSj1H2gnGz8vBnhVVWK3FKFA',
    '_identity': '%5B40664086%2C%229a0moAfzXGwkT7T-9jMSU0GgDaASI6buczKitGfdfWUA2fUi_t5C566Yh-3Z5fpl%22%2C864000%5D',
    '_welcome_banner_first_seen_at': '1686235733349',
    'learn.tooltip.view.count': '2',
    'mscom_new': 'b56350134a88270b159e6d4c644509cd',
    '_mu_atts_key': 'user_attributes%3A40664086.RU.Petrozavodsk.ru.1686283200.Europe%2FMoscow',
    #'_csrf': 'ufuOMypLB4qZNOUCJd9hEpK9LFWFKZUG',
    'mu_ab_experiment': '2995.1_3010.2_3019.4_3031.1_3040.2_3043.2_3046.2_3049.1_3085.2',
    '_mu_dc_regular': '%7B%22v%22%3A2%2C%22t%22%3A1686323008%7D',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    #'_ms_adScoreView': '6',
    #'mu_has_static_cache': '1686326844',
    '_mu_session_id': '1.1686323005.1686326849',
    '__cf_bm': 'RZgep7Fl.ilns7UBGX1OY2llYvVCjcgauiwEoKJO03I-1686326849-0-AfsUC+g0JMyao96LYnSaJdWi0Em6UO1N6eCYYXU9Fs0gAf+Gnj1hPBVSYzXVvcrqEHvqN3BmEcv/izB4ILRaOtw=',
    '_ga_4YMPJQFQ7N': 'GS1.1.1686323010.5.1.1686326850.0.0.0',
    '_ga': 'GA1.1.1359321515.1686227781',
}

headers = {
    'authority': 'musescore.com',
    'method' : 'GET',
    'path' : '/user/89075/scores/4677401/embed',
    'scheme' : 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding':'gzip, deflate, br',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'uwguid=WEBLS-b9766a32-65ef-464e-9c1f-4dfcc57be378; mu_browser_bi=6589667686921956405; mu_browser_uni=0NBsi6fZ; _mu_unified_id=1.1686227780.1828271; mu_unregister_user_id=598798501; _gid=GA1.2.1244405920.1686227781; _ym_uid=168622778137611141; _ym_d=1686227781; _pbjs_userid_consent_data=3524755945110770; __gads=ID=9fb567920c136c6f:T=1686227783:RT=1686227783:S=ALNI_MbyPz2DqHCp5PGZyUwRxhCWe-hzmQ; __gpi=UID=00000c2d51f8e9c2:T=1686227783:RT=1686227783:S=ALNI_MauaVkSj1H2gnGz8vBnhVVWK3FKFA; _identity=%5B40664086%2C%229a0moAfzXGwkT7T-9jMSU0GgDaASI6buczKitGfdfWUA2fUi_t5C566Yh-3Z5fpl%22%2C864000%5D; _welcome_banner_first_seen_at=1686235733349; learn.tooltip.view.count=2; mscom_new=b56350134a88270b159e6d4c644509cd; _mu_atts_key=user_attributes%3A40664086.RU.Petrozavodsk.ru.1686283200.Europe%2FMoscow; _csrf=ufuOMypLB4qZNOUCJd9hEpK9LFWFKZUG; mu_ab_experiment=2995.1_3010.2_3019.4_3031.1_3040.2_3043.2_3046.2_3049.1_3085.2; _mu_dc_regular=%7B%22v%22%3A2%2C%22t%22%3A1686323008%7D; _ym_isad=1; _ym_visorc=w; _ms_adScoreView=6; mu_has_static_cache=1686326844; _mu_session_id=1.1686323005.1686326849; __cf_bm=RZgep7Fl.ilns7UBGX1OY2llYvVCjcgauiwEoKJO03I-1686326849-0-AfsUC+g0JMyao96LYnSaJdWi0Em6UO1N6eCYYXU9Fs0gAf+Gnj1hPBVSYzXVvcrqEHvqN3BmEcv/izB4ILRaOtw=; _ga_4YMPJQFQ7N=GS1.1.1686323010.5.1.1686326850.0.0.0; _ga=GA1.1.1359321515.1686227781',
    'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.2.595 Yowser/2.5 Safari/537.36',
}

response = requests.get('https://musescore.com/user/89075/scores/4677401/embed', cookies=cookies, headers=headers)
print(response.text)