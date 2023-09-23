#imports
 
import json
import re
from instagrapi import Client
from collections import defaultdict
from datetime import datetime
from language_tool_python import LanguageTool
 
#initializing client
 
apicl = Client()
 
#logging in
 
user = "snu.hackathon.burner.finale"
passkey = "snu@12345"
 
#enabling login
 
apicl.login(user, passkey)
 
target = input("enter target username: ")
 
#finding numeric user id from username
 
targetid = apicl.user_id_from_username(target)
 
#retrieving followers
 
followers = apicl.user_followers(targetid)
follower_count = len(followers)
 
#retrieving posts
 
posts = apicl.user_medias(targetid)
post_count = len(posts)
 
#retrieving following data
 
following = apicl.user_following(targetid)
following_count = len(following)
 
#taking into account users with no followers/following
 
if following_count == follower_count == 0:
    blank = 1
 
else:
    blank = 0
 
#finding average likes per post to follower ratio
 
def lf_ratio(user_id):
    #initialize like counter
 
    like_sum = 0
 
    #totalling likes and calculating average likes
 
    for post in posts:
        like_count = post.like_count
        like_sum += like_count
 
    if post_count > 0:
        like_avg = like_sum / post_count
    else:
        like_avg = 0
 
    print("followers:", follower_count)
    print("post count:", post_count)
    print("average likes:", like_avg)
 
    #calculating like to follower ratio
 
    if follower_count > 0:
        lfratio = like_avg / follower_count
    else:
        lfratio = 0
 
    return(lfratio)
 
#calculating ratio of followers to following
 
def ff_ratio(user_id): 
 
    if follower_count > 0 and following_count > 0:
        ffratio = follower_count/following_count
    else:
        ffratio = 0
 
    return(ffratio)
 
 
#checking post frequency
 
def post_freq(user_id): 
    print("posts per day:")
 
    posts = apicl.user_medias(user_id)
 
    days = 0
 
    count_sum = 0
 
    #initializing storage dictionary
 
    daily_post_counts = defaultdict(int) 
 
    for post in posts:
        #extracting date
 
        post_date = post.taken_at.date()
 
        daily_post_counts[post_date] += 1
 
    for date, count in sorted(daily_post_counts.items()):
        print(date,":", count, "posts")
 
        days += 1
 
        count_sum += count
 
    #calculating average posts per days (on which posts have been made)
 
    avg_posts = count_sum/days
 
    return(avg_posts)
 
 
def check_grammar(text):
    tool = LanguageTool('en-US')
    errors = tool.check(text)
    error_count = len(errors)
 
    #determining grammar mistakes and quantifying coherence
 
    coherence_score = 30 - min(30, error_count)  
 
    return coherence_score
 
#checking coherence of user bio
 
def bio_coherence(user_id): 
    user_info = apicl.user_info(user_id)
 
    #extracting bio text
 
    bio_text = user_info.biography.lower()
 
    #printing bio text
 
    print("Bio Text: ", bio_text)
 
    #initializing grammar tool
 
    coherence_score_bio = check_grammar(bio_text)
    return(coherence_score_bio)
 
#checking coherence of post captions
 
def cap_coherence(user_id): 
    user_info = apicl.user_info(user_id)
 
    #retrieving post data
 
    user_posts = apicl.user_medias(user_id)
 
    #creating an empty list to store post captions
 
    captions = []
 
    for post in user_posts:
        caption = post.caption_text.lower()
 
        #storing captions in the list
 
        captions.append(caption)  
 
    #declaring suspicious texts to check for
 
    suspicious_text = "iPhone bitcoin dropshipping cheap link make money fast spin call crypto cash paying DM Viral debt investment trade trust market license entrepreuner services free partnership rich discount bet finance stock trade".split()
 
    #initializing keyword counter and red flag alert
 
    suspicious_words = 0
 
    red_flag_detected = False
 
    coherence_sum = 0
 
    #nesting loops to check for suspicious words in every list element
 
    for cap in captions:
        #summing up coherence scores
 
        coherence_sum += check_grammar(cap)
 
        coherence_avg = coherence_sum/len(captions)
 
        #quantifying suspicious words
 
        cap = cap.split()
        for i in cap:
            if i in suspicious_text:
                suspicious_words += 1
                red_flag_detected = True
 
    suspicious_words_avg = suspicious_words/len(captions)
 
    return(suspicious_words_avg, coherence_avg)
 
#checking ratio of numbers to letters in the username
 
def userint_ratio(user_id): 
    #initializing 
 
    char = 0
    num = 0
    spec = 0
 
    for i in target:
        #checking if the token is a letter, number, or special character
 
        if i.isalpha():
            char += 1
 
        elif i == "." or i == "_":
            spec += 1
 
        else:
            num += 1
 
    uiratio = (num + spec) / (char + spec + num)
 
    return(uiratio)
 
#checking whether the user has a profile picture or not
 
def pfp(user_id):
    user_info = apicl.user_info(user_id)
 
    has_pfp = bool(user_info.profile_pic_url)
 
    if has_pfp:
 
        has_pfp = 1
 
    else:
 
        has_pfp = 0
 
    return(has_pfp)
 
def emoji(user_id):
    user_info = apicl.user_info(user_id)  
 
    #collecting bio data
 
    bio_text = user_info.biography
    emoji_count_bio = len(re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001F004\U0001F0CF\U0001F170-\U0001F251]+', bio_text))
 
    #collecting captions data
    user_posts = apicl.user_medias(user_id)
 
    #initializing list to store all captions
    caption_texts = []
 
    for post in user_posts:
        caption_text = post.caption_text
        caption_texts.append(caption_text)
 
    #initializing emoji count
 
    emocount = 0
 
    for i, caption_text in enumerate(caption_texts):
        for text in caption_text:
            emoji_count_caption = len(re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001F004\U0001F0CF\U0001F170-\U0001F251]+', caption_text))
            emocount += emoji_count_caption   
 
    avg_emo = emocount / len(user_posts)
 
    return(emoji_count_bio, avg_emo)
 
def url(user_id):
    user_info = apicl.user_info(user_id)  
 
    user_info_json = json.loads(user_info.json(indent=4))
 
    url_detect = 0
 
    try:
        external_url = user_info_json["external_url"]
        if len(external_url) > 0:
            url_detect = 1
 
    except Exception as e:
        print(e)
 
    return(url_detect)
 
#function calling
 
if targetid:
    a = blank #1 or 0, 1 indicates if followers = following = 0
 
    b = lf_ratio(targetid) #average likes / followers ratio
 
    c = ff_ratio(targetid) #followers/following ratio
 
    d = post_freq(targetid) #average posts a day (for days where a post has been made)
 
    e = bio_coherence(targetid) #1-30, least to most coherent bio
 
    f, g = cap_coherence(targetid) #f is the average of the number of suspicious words per post, g is 1-30 average of caption coherence
 
    h = userint_ratio(targetid) #ratio of numbers + special characters (underscores, periods) / all characters in the username
 
    i = pfp(targetid) #1 or 0, 1 if user has a pfp
 
    j, k = emoji(targetid) #j is the number of emoji in the bio, k is the average number of emoji per post
 
    l = url(targetid) #1 or 0, 1 indicating the existence of a url in bio
 
    # Printing values with labels
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")
    print(f"e = {e}")
    print(f"f = {f}")
    print(f"g = {g}")
    print(f"h = {h}")
    print(f"i = {i}")
    print(f"j = {j}")
    print(f"k = {k}")

    final=0
    if a==1:
        final+=8
    else:
        final+=0

    final+=(b/9)*100
    
    final+=(c/10)*100

    final+=(d/10)*100

    final+=(e/11)*100

    final+=(f/11)*100

    final+=(g/11)*100

    final+=(h/6)*100

    final+=(i/6)*100

    final+=(j/3)*100

    final+=(k/5)*100

    final+=(l/8)*100

    print ("The final score is: ")
    print(final)  

else:
    print("invalid username.")
 
#logging out
 
apicl.logout()