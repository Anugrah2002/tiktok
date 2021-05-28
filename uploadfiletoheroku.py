# This file is of no use in  this whole project
 

# from django.http import HttpResponse, JsonResponse
import requests
import cloudinary
import cloudinary.uploader


cloudinary.config(
  cloud_name = 'drpb4oxcc',
  api_key = '354327896332831',
  api_secret = 'CvetvSAc2xW33TRe_CaitVsi9S8'
)



def uploadvideotoheroku(filepath):
    try:
        print(filepath)
        filepath = str(filepath)
        # filepath = filepath.replace(' ','\ ')
        print(filepath)
        myurl = 'http://ytserver.eu-gb.cf.appdomain.cloud/videouploadwithcloudinary/'
        upload_data = cloudinary.uploader.upload_large(filepath)
        videoPublicId=str(upload_data['public_id'])
        videoUrl=str(upload_data['secure_url'])
        print(videoPublicId)
        print(videoUrl)
        getdata = requests.post(myurl,data={'title':'Top Compilations of funny videos(TikTok)','videoPublicId':videoPublicId,'videoUrl':videoUrl})
        print(getdata.text)  
        # r=requests.post('http://lit-sierra-15246.herokuapp.com/videoupload/')
    except Exception as e:
        print(e)