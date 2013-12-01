"""
Listening_Post is a Python implementation of the installation by Artists 
Ben Rubin and Mark Hansen.

It takes random text from the internet and displays it.

See http://news.bbc.co.uk/1/hi/technology/7251390.stm for more details.

This implementation by Jack Wearden (@jackweirdy, NotBobTheBuilder)
https://github.com/NotBobTheBuilder/listening_post
Released under MIT License

"""
import praw

def unquote(text):
  """
  Remove opening & closing double quotes, if they're present
  """
  if text[:1] == text[-1:] == "\"":
    return text[1:-1]
  else:
    return text

def r_nocontext():
  """
  Grab some non-modposts from /r/nocontext and display it
  """
  reddit    = praw.Reddit(user_agent="listening_post")
  subreddit = reddit.get_subreddit("nocontext").get_hot(limit=10)
  text      = [unquote(post.title) for post in subreddit if not post.stickied]
  return text

def main():
  print "\n".join(r_nocontext())

if __name__ == "__main__":
  main()
