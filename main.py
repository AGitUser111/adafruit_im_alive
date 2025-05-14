import time
from config import config

from Adafruit_IO import Client, Feed, RequestError
import os

def create_feed_if_not_exists(client: Client, feed_name: str) -> Feed:
    """Create a feed if it does not exist."""
    try:
        feed = client.feeds(feed_name)
    except RequestError:  # Doesn't exist, create a new feed
        feed = Feed(name=feed_name)
        feed = client.create_feed(feed)
    return feed


def main():
    
    adafruit_client = Client(
        config.ADAFRUIT_IO_USERNAME,
        config.ADAFRUIT_IO_KEY.get_secret_value(),
    )
    
    create_feed_if_not_exists(adafruit_client, config.FEED_NAME)

    while True:
        try:
            t = os.popen("uptime -p").read()
            print(t)
            adafruit_client.send_data(config.FEED_NAME, t)
            time.sleep(config.SEND_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
    



if __name__ == "__main__":
    main()
