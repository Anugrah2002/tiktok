from firebase import Firebase
# from firebase_admin import bucket
import requests
firebaseConfig = {
    'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
    'authDomain': "tiktokvideos-378aa.firebaseapp.com",
    'storageBucket': "tiktokvideos-378aa.appspot.com",
    "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
    "serviceAccount": "./service_account.json",
}


firebase = Firebase(firebaseConfig)
storage = firebase.storage()
c=storage.child("AllVideos/").get()
print(c)
print('----------------------------------------------------------------------------------')
# b=storage.bucket(1)
# print(b)
print(storage)
# a=requests.get('https://tiktokvideos-378aa.appspot.com/AllVideos/')
# print(a)
# storage.get
# storage.delete('AllVideos/')
