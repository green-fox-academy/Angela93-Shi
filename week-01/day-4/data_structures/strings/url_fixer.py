
# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crutial component, find out what it is and insert it too!
url = "https//www.reddit.com/r/nevertellmethebots"
url.replace('bots','odds')
target_list=list(url)
target_list.insert(5,':')
target_str=''.join(target_list)
print(target_str)
