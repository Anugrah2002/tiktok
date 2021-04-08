from firebase import Firebase
firebaseConfig = {
    'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
    'authDomain': "tiktokvideos-378aa.firebaseapp.com",
    'storageBucket': "tiktokvideos-378aa.appspot.com",
    "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
}


firebase = Firebase(firebaseConfig)
storage = firebase.storage()
storage.delete('AllVideos/finalVide2021-04-03 21:12:53.071381.mp4')