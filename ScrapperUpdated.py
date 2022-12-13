import requests
import shutil
import os
import tweepy
# to store the downloaded profile pics in a different folder
try:
    os.mkdir(os.path.join(os.getcwd(), 'profilepic1'))
    os.chdir(os.path.join(os.getcwd(), 'profilepic1'))
except:
    pass
#os.chdir(os.path.join(os.getcwd(), 'profilepic'))
#def downloadPP(username,num):
def downloadPP(username, i, j):
    url ='https://unavatar.io/twitter/'+str(username)        #input('Please enter an image URL (string):') #prompt user for img url
    #file_name ='profilepic'+str(num)+str(username)+'.jpg'            #input('Save image as (string):') #prompt user for file_name
    file_name= j+str(i)+'.jpg'
    
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

#'https://unavatar.io/twitter/anu_shka_28' 
#def scrape(words, date_since, numtweet):

user_name=[]

def scrape(words, date_since, numtweet,i, j):
    # We are using .Cursor() to search
        # through twitter for the required tweets.
        # The number of tweets can be
        # restricted using .items(number of tweets)
        '''tweets = tweepy.Cursor(api.search_tweets,
                               words, lang="en",
                               since_id=date_since,
                               tweet_mode='extended').items(numtweet)'''
        tweets = tweepy.Cursor(api.search_tweets,
                               words, lang="en",
                               since_id=date_since,
                               tweet_mode='extended').items(numtweet)
 
 
        # .Cursor() returns an iterable object. Each item in
        # the iterator has various attributes
        # that you can access to
        # get information about each tweet
        list_tweets = [tweet for tweet in tweets]
        
        # we will iterate over each tweet in the
        # list for extracting information about each tweet
        num = 0
        for tweet in list_tweets:
                username = tweet.user.screen_name
                #downloadPP(username,num)
                #num = num +1
                if (username not in user_name):
                  downloadPP(username,i, j)
                  user_name.append(username)
                  return i
                else:
                  return (i-1)

# Enter your own credentials obtained
# from your developer account
consumer_key = "nEtZNN4eL6d7bnA3zqz33QlRt"
consumer_secret = "mmYVtq9V74KYI3hwCHixJX3v3eWClRuh7OJPFpaU3Ai2DNECQE"
access_key = "1486218021987565568-m592gA9bOh1jJRiCozcFNUrme2vBJ6"
access_secret = "53mqfnis0JKfSLwumhoafWk5zqS1zv7iTaBct3HUdxDfG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#Enter hashtag and initial date

print("Enter Twitter HashTag to search for")
#words = input()
words=['India','Microsoft','nature','RanbirKapoor','Modi','USA','cats','grantgustin','trending','dogs']
print("Enter Date since The Tweets are required in yyyy-mm--dd")
date_since = input()

# number of tweets you want to extract in one run
#numtweet = 10
#scrape(words, date_since, numtweet)

for j in words:
  for i in range(1,11):
    i=scrape(words,date_since,1,i,j)
print('Scraping has completed!')