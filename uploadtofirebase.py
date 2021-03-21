from firebase import Firebase
from datetime import datetime
import requests


def uploadfiletofirebase(filepath):

  current_time=str(datetime.now())
  print(current_time)


  firebaseConfig = {
      'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
      'authDomain': "tiktokvideos-378aa.firebaseapp.com",
      'storageBucket': "tiktokvideos-378aa.appspot.com",
      "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
    }


    # https://tiktokvideos-378aa-default-rtdb.firebaseio.com/



  firebase = Firebase(firebaseConfig)

  storage = firebase.storage()

  # as admin
  storage.child(filepath[:-5]+current_time+'.mp4').put(filepath)

  url=storage.child(filepath[:-5]+current_time+'.mp4').get_url(1)
  print(url)
  myurl = 'http://ytserver.eu-gb.cf.appdomain.cloud/videouploadwithcloudinary/'
  postdatas = requests.post(myurl,data={'title':'Top tiktok compilations','videoPublicId':'Tiktok firebase','videoUrl':url})