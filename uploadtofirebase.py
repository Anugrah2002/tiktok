from firebase import Firebase


def uploadfiletofirebase(filepath):

  firebaseConfig = {
      apiKey: "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
      authDomain: "tiktokvideos-378aa.firebaseapp.com",
      projectId: "tiktokvideos-378aa",
      storageBucket: "tiktokvideos-378aa.appspot.com",
      messagingSenderId: "745659917761",
      appId: "1:745659917761:web:b55d2b3ec189fd4053fb40",
      measurementId: "G-BHVJQBQC0M"
    };



  firebase = Firebase(firebaseConfig)

  storage = firebase.storage()

  # as admin
  storage.child(filepath).put(filepath)