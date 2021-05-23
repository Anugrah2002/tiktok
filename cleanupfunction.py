# from firebase import Firebase
from firebase import Firebase
from datetime import datetime
import requests
import firebase_admin
from firebase_admin import storage as admin_storage, credentials, firestore
# from firebase_admin import bucket


firebaseConfig = {
    'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
    'authDomain': "tiktokvideos-378aa.firebaseapp.com",
    'storageBucket': "tiktokvideos-378aa.appspot.com",
    "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
    "serviceAccount": "./service_account.json",
}


firebase = Firebase(firebaseConfig)
storage = firebase.storage()
a=admin_storage.bucket()
blob=a.blob('Farmers_Increase_Income_By_Adopting_Animal_Husbandry_Etawha_News_Knp615834078_hd.mp4')
blob.delete()

# c=storage.child("AllVideos/").val()
# print(c)
# print('----------------------------------------------------------------------------------')
# # b=storage.bucket(1)
# # print(b)
# print(storage)
# a=requests.get('https://tiktokvideos-378aa.appspot.com/AllVideos/')
# print(a)
# storage.get
# storage.delete('AllVideos/')
