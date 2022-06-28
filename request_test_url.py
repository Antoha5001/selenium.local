import sys
import requests

def main ():
	
	if len(sys.argv) > 1:

		cookies = {
    'DY_SS_LOGIN_NECESSARY': 'true',
    'DY_SS_CART_SYNC_NECESSARY': 'false',
    'disp_react_aa': '2',
    'disp_plp_promo_ab': 'B',
    'ggr-widget-test': '1',
    'flowbox-gallery-pdp': '1',
    'dtCookie': 'v_4_srv_5_sn_D9CB63A4A6F13DDC869B969D52CC02FB_perc_23626_ol_1_app-3Ab82b63450c1d92de_0',
    '_ym_uid': '1621840552121649442',
    '_ym_d': '1655176288',
    '_gcl_au': '1.1.437717566.1655176288',
    'iap.uid': '2ef8378df08a4a788e3dccc3372a3db5',
    '_ym_isad': '2',
    '_reactCheckout': 'true',
    '_gaexp': 'GAX1.2.ouICWlkpTuKpvosrUFwQ2g.19166.1!VwpUMju9StqK4VAIUXCnRg.19201.1!eR73QAwhQEm_bbI90yLBVA.19239.3',
    'x-api-option': 'cce-283',
    '_ga': 'GA1.2.858098261.1655176289',
    '_gid': 'GA1.2.550913553.1655176289',
    'tmr_lvidTS': '1621840553597',
    'tmr_lvid': '831899b639f47b02efeeead313ac4964',
    'aplaut_distinct_id': 'aauh9TKvvuHL',
    'cookie_accepted': 'true',
    'fromRegion': '34',
    '___dmpkit___': 'a0558670-d422-43c2-8a97-902aff1e462e',
    'aplaut_distinct_id': 'aauh9TKvvuHL',
    'DY_SS_CART_SYNC_NECESSARY': 'true',
    'lastConfirmedRegionID': '2397',
    'GACookieStorage': 'GA1.2.858098261.1655176289',
    'user-geolocation': '0%2C0',
    'X-API-Experiments-sub': 'B',
    '_regionID': '2397',
    '_newPickup': 'true',
    'tmr_detect': '0%7C1655176990388',
    'cto_bundle': 'LEDBKl9aVUhRTXZ1bnlXa2glMkZZenRvRWVDTFlXV29lMkVKJTJGQU1uRzduYUJZajRGekk5bCUyRktpRzFYaSUyQmFWRTlVS0hvU0paS09PcTglMkZNcDhOYXZqakJQMnZVWWhMbmdFeTZqMUVPT2dpZ2YyMzNiMm04ZGZDMDVtUWRISFpmVnR2JTJGNXBqdzhnNEdDaGRMSW5mVVdJUUlLemVkOXclM0QlM0Q',
    'tmr_reqNum': '175',
    'qrator_jsr': '1655186286.996.InIXSbzQhhfR5Jdh-0kslhj8rhqmlsca10g8vkqbvtfjnk5a0-00',
    'qrator_jsid': '1655186286.996.InIXSbzQhhfR5Jdh-42lpc40gs7od9tqoqdvtgs88nkkij338',
    'qrator_ssid': '1655186287.797.PecOw6Bb0mUaJLjE-33o9d64v02q17sjseudf7bdl50cg8nhj',
}

		headers = {
    'authority': 'barnaul.leroymerlin.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'DY_SS_LOGIN_NECESSARY=true; DY_SS_CART_SYNC_NECESSARY=false; disp_react_aa=2; disp_plp_promo_ab=B; ggr-widget-test=1; flowbox-gallery-pdp=1; dtCookie=v_4_srv_5_sn_D9CB63A4A6F13DDC869B969D52CC02FB_perc_23626_ol_1_app-3Ab82b63450c1d92de_0; _ym_uid=1621840552121649442; _ym_d=1655176288; _gcl_au=1.1.437717566.1655176288; iap.uid=2ef8378df08a4a788e3dccc3372a3db5; _ym_isad=2; _reactCheckout=true; _gaexp=GAX1.2.ouICWlkpTuKpvosrUFwQ2g.19166.1!VwpUMju9StqK4VAIUXCnRg.19201.1!eR73QAwhQEm_bbI90yLBVA.19239.3; x-api-option=cce-283; _ga=GA1.2.858098261.1655176289; _gid=GA1.2.550913553.1655176289; tmr_lvidTS=1621840553597; tmr_lvid=831899b639f47b02efeeead313ac4964; aplaut_distinct_id=aauh9TKvvuHL; cookie_accepted=true; fromRegion=34; ___dmpkit___=a0558670-d422-43c2-8a97-902aff1e462e; aplaut_distinct_id=aauh9TKvvuHL; DY_SS_CART_SYNC_NECESSARY=true; lastConfirmedRegionID=2397; GACookieStorage=GA1.2.858098261.1655176289; user-geolocation=0%2C0; X-API-Experiments-sub=B; _regionID=2397; _newPickup=true; tmr_detect=0%7C1655176990388; cto_bundle=LEDBKl9aVUhRTXZ1bnlXa2glMkZZenRvRWVDTFlXV29lMkVKJTJGQU1uRzduYUJZajRGekk5bCUyRktpRzFYaSUyQmFWRTlVS0hvU0paS09PcTglMkZNcDhOYXZqakJQMnZVWWhMbmdFeTZqMUVPT2dpZ2YyMzNiMm04ZGZDMDVtUWRISFpmVnR2JTJGNXBqdzhnNEdDaGRMSW5mVVdJUUlLemVkOXclM0QlM0Q; tmr_reqNum=175; qrator_jsr=1655186286.996.InIXSbzQhhfR5Jdh-0kslhj8rhqmlsca10g8vkqbvtfjnk5a0-00; qrator_jsid=1655186286.996.InIXSbzQhhfR5Jdh-42lpc40gs7od9tqoqdvtgs88nkkij338; qrator_ssid=1655186287.797.PecOw6Bb0mUaJLjE-33o9d64v02q17sjseudf7bdl50cg8nhj',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Mobile Safari/537.36',
}
		
		response = requests.get(sys.argv[1], headers=headers, cookies=cookies)
		print(response.text)


if __name__ == "__main__":
	main()