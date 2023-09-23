# -can-t.com-cookies
snu hackathon repository: Problem ID 1364; Identifying Fake Social Media Profiles

Subject: summary of a possible, feasible resolution to assist fake social media profile detection and
reporting
1. Selecting a suitable API wrapper (in this case: instagrapi) to help us deal with Instagram's API smoothly in order to collect data.
2. Creation of multiple guidelines to follow, classify and tabulate accounts into different types of
accounts (real/fake/scam) and of different severity stages.
 Ex: this can be done by providing weightage to each violation (refer to pt.5) and setting an
overall grading, where grades beyond a point corresspond to accounts that are found to be spam/fake.
3. Multiple aspects to be judged i.e., the following criteriae:
   - the following or follower counts being 0
   - the follower/following ratio
   - post frequency
   - coherence of profile bio and post captions
   - the ratio of numbers/special characters in the username string
   - the existence of a default profile photo
   - the use of emoji in bio/captions.
5. Setting up of a program to identify such red flags using instagrapi, and
accordingly “flag” them. 
6. Plugging of data into a well-approximated formula to quantify its susceptibility to being spam.
7. Providing an overall summary using information taken from all accounts, to provide relevant
information.
8. Criteriae that we recognize would be useful but could not incorporate due to API restrictions and rate limits:
   - comment history, quality, and coherence
   - comments under target profile's posts
   - story/highlight data
   - account age
9. The program's basis lies in converting inputted user id from a string format to a numeric id format, accessing its data (via API) on Instagram, managing and retrieving the data in functions defined in the program code, and quantifying all values accordingly.
10. Modules imported:
    - instagrapi
    - json
    - re
    - collections
    - datetime
    - language_tool_python
Team Members:
 1. Anuran
 2. Kishika
 3. Anish
 4. Piyush
 5. Jia
 6. Arnab 
