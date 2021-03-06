from TikTokApi import TikTokApi
from moviepy.editor import *
import os
import uploadtofirebase

NUMOFVIDEOS = 4

def downloadVideos():
    api = TikTokApi.get_instance()
    # If playwright doesn't work for you try to use selenium
    api = TikTokApi.get_instance(use_selenium=True)

    results = NUMOFVIDEOS

    # Since TikTok changed their API you need to use the custom_verifyFp option. 
    # In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
    trending = api.trending(count=results, custom_verifyFp="verify_km82f9aj_jizxev2u_XCqM_4W3N_9hVV_NrqG98hejlXY")

    if not os.path.exists('AllVideos'):
        os.makedirs('AllVideos')

    #Saving Videos
    for tiktok in trending:

        responseInBytes = api.get_Video_By_DownloadURL(tiktok['video']['downloadAddr'], language='en', proxy=None, custom_verifyFp="verify_km82f9aj_jizxev2u_XCqM_4W3N_9hVV_NrqG98hejlXY")
        with open(r'AllVideos/video' + str(results) + '.mp4', 'wb') as f:
            f.write(responseInBytes)
        
        results-=1
        

    print(len(trending))

    concatenateVideoclips()



def concatenateVideoclips():
    
    allClipsArray = [] #it will hold all the clips

    for currentIndex in range(1,NUMOFVIDEOS+1):
        allClipsArray.append(VideoFileClip(r"AllVideos/video" + str(currentIndex) + '.mp4'))
        
    
    final_clip = concatenate_videoclips(allClipsArray)
    print('--------------------------------------')
    size=final_clip.size
    print(size)
    print('***************************************')
    #final_clip = final_clip.resize(0.4)
    print(final_clip.size)

    final_clip.write_videofile(r"AllVideos/finalVideo.mp4")

    uploadtofirebase.uploadfiletofirebase(r'AllVideos/finalVideo.mp4')

downloadVideos()

#S_V_WEB_ID:- verify_km82f9aj_jizxev2u_XCqM_4W3N_9hVV_NrqG98hejlXY
