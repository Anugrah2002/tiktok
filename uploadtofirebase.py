from firebase import Firebase


def uploadfiletofirebase(filepath):

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
  storage.child(filepath).put(filepath)