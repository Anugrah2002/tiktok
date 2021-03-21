from firebase import Firebase
from datetime import datetime


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

  a=storage.child(filepath[:-5]+current_time+'.mp4').get_url(1)
  print(a)