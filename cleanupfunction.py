from firebase import Firebase
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
print(storage)
a=requests.get('gs://tiktokvideos-378aa.appspot.com/AllVideos/')
print(a)
# storage.get
# storage.delete('AllVideos/')
