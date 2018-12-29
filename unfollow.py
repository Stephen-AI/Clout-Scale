import twitter
import os

# unfollow users that don't follow back unless they're verified
def main ():
  A = 'TWITTER_CONSUMER_KEY'
  B = 'TWITTER_CONSUMER_SECRET'
  C = 'TWITTER_ACCESS_TOKEN'
  D = 'TWITTER_ACCESS_TOKEN_SECRET'
  consumer_key = os.environ[A]
  consumer_secret = os.environ[B]
  access_token = os.environ[C]
  access_token_secret = os.environ[D]

  

  api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_token, access_token_secret=access_token_secret)
  following = set(api.GetFriends())
  followers = set(api.GetFollowers())
  stans = []
  for stan in following:
    if stan not in followers and not stan.verified:
      # print(stan)
      api.DestroyFriendship(user_id=stan.id)

main ()