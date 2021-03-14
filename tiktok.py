from TikTokApi import TikTokApi
api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
api = TikTokApi.get_instance(use_selenium=True)

results = 10

# Since TikTok changed their API you need to use the custom_verifyFp option. 
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
trending = api.trending(count=results, custom_verifyFp="verify_km82f9aj_jizxev2u_XCqM_4W3N_9hVV_NrqG98hejlXY")

for tiktok in trending:
    # Prints the id of the tiktok
    print(tiktok['id'])
    print(tiktok['video']['downloadAddr'])


print(len(trending))



#S_V_WEB_ID:- verify_km82f9aj_jizxev2u_XCqM_4W3N_9hVV_NrqG98hejlXY