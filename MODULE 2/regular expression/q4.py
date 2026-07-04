import re


def clean_tweet(tweet):
    cleaned = re.sub(r"http\S+|@\w+|#\w+|\bRT\b|\bcc:?\b", "", tweet, flags=re.IGNORECASE)
    cleaned = re.sub(r"[\-–—_:;,.!?]+", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


if __name__ == "__main__":
    tweet = (
        "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today "
        "http://t.co/lbwej0px0d cc: @garybernhardt #rstats"
    )
    print("Original tweet:\n", tweet)
    print("Cleaned tweet:\n", clean_tweet(tweet))
