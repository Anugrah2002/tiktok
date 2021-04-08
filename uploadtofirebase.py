from firebase import Firebase
from datetime import datetime
import requests
import firebase_admin
from firebase_admin import storage as admin_storage, credentials, firestore


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
  buck=admin_storage.storageBucket()
  da=buck.da('AllVideos/finalVide2021-04-03 21:12:53.071381.mp4')
  da.delete()

  url=storage.child(filepath[:-5]+current_time+'.mp4').get_url(1)
  print(url)

  myurl = 'http://ytserver.eu-gb.cf.appdomain.cloud/videouploadwithcloudinary/'
  
  titletopost = datetime.now()
  titletopost = 'TIK TOK COUPLE GOALS COMPILATION TIKTOK LOVE ROMANTIC  ' + str(titletopost.strftime("%B"))
  
  descriptiontopost = """
   Thanks For Watching........ 🙏🙏 🙏 

Like, Share, Comment, & Don't Forget To Subscribe Channel, and

 press the Bell 🔔 Icon For Never Miss An Update " Tik Tok Latest Videos " 

 If You Like My Videos You Can Subscribe My Channel Now Thank You.

New Tik Tok Funny video Funny & Romantic tik tok video  Tik Tok Video

Tik Tok Mix Tape Videos Compilation  Romantic Couple Goals, Funny, Comedy,  Videos Compilation

Today's Best Latest New Tik Tok Musically Video  Romantic, Funny, Tiktok Video  Tik Tok Videos

New Tiktok Funny & Romantic Videos Of Jannat Zubair, Mr. Faisu, Avneet Kaur, Riyaz Aly, Arishfa Khan

Today's Best Latest New Tik Tok Musically Video | Romantic, Funny, Tiktok Video  Tik Tok Videos

tik tok video beauty Khan tik tok video training new husena khan video rjkevar tik tok video fan

New Latest Romantic Couple Goals Tiktok Videos BF GF GOALS  TIK TOK COUPLE GOALS  COUPLES

ROMANTIC TIKTOK COUPLEGOALS 2020  Best Musically RelationshipGoals  Cute CouplesMusically

Tik Tok Couple VideosTik Tok Romantic Cute Couples GOALS TikTok viral video

New Trending Tik Tok Video!!Tik Tok Romentik  Video !! Couple Goals Letest Funny Video

I Love You TikTok Romantic Cute Couple Goals video  New Tik Tok Bf Gf TikTok viral video

Tiktok Romantic Cute Couple Goal Video 2020  Romantic BF GF Goals Latest tik tok viral video

Tik Tok Love - Best Couple & Relationship Goals Compilation 2020 - Cute Couples Musically
  """
  
  postdatas = requests.post(myurl,data={'title':titletopost,'videoPublicId':descriptiontopost,'videoUrl':url})
