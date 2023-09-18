from dotenv import load_dotenv
import os
load_dotenv()

cookies = {
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
    '_csrf': 'ufuOMypLB4qZNOUCJd9hEpK9LFWFKZUG',
    'mu_ab_experiment': '2995.1_3010.2_3019.4_3031.1_3040.2_3043.2_3046.2_3049.1_3085.2',
    '_mu_dc_regular': '%7B%22v%22%3A2%2C%22t%22%3A1686323008%7D',
    '_ym_isad': '1',
    '_ym_visorc': 'w',
    '_ms_adScoreView': '6',
    'mu_has_static_cache': '1686326844',
    '__cf_bm': '7OHnvHZGlBA2sj.E8_a707jPa7ERMTL7lGUWULLqMv4-1686327796-0-AUwddl/ccNciKDPkE0AKbaihQnjw2I2OnTczEEiSLSSrgkXyP8Dc58U6dq5sgUBzWyXE2Q7LThTV05LUiEyG3SY=',
    '_ga': 'GA1.1.1359321515.1686227781',
    '_mu_session_id': '1.1686323005.1686328286',
    '_ga_4YMPJQFQ7N': 'GS1.1.1686323010.5.1.1686328286.0.0.0',
}

headers = {
    'authority': 'musescore.com',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'authorization': os.getenv("authorization"),
    'referer': 'https://musescore.com/user/89075/scores/4677401/embed',
    # 'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.2.595 Yowser/2.5 Safari/537.36',
}

params = {
    'id': '4677401',
    'index': '1',
    'type': 'img',
    'v2': '1',
}