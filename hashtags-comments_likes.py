#!pip install instagrapi


##############################################################################

USER = ''
PASSWORD = ''

hashtags = [
    ''
]

comments = [
    ''
]

posts = 1
like_post = False



##############################################################################

from instagrapi import Client

client = Client()
client.login(USER, PASSWORD)


for hashtag in hashtags:
    print ('Hashtag:', hashtag)
    for comment in comments:
        print ('Comment:', comment)
        medias = client.hashtag_medias_recent(hashtag, posts)
        for i, media in enumerate(medias):
            print("Post:" , str(media.id))
            
            client.media_comment(media.id, comment)
            print("Commented !")
            
            if like_post == True:
                client.media_like(media.id)
                print("Liked !")
            
            print ('-----------------------------')
        print('====================================')
                
print ('Done !')  