import feedparser
import sys


def get_latest_feeds(rss_url, num_feeds):
    feed = feedparser.parse(rss_url)

    if feed.bozo:
        print(f"Error parsing feed: {feed.bozo_exception}")
        return

    entries = feed.entries[:num_feeds]

    for entry in entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Summary: {entry.summary}")
        print("-" * 80)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 rss_reader.py <rss_feed_url> [num_feeds]")
        sys.exit(1)

    rss_url = sys.argv[1]
    if len(sys.argv) > 2:
        num_feeds = int(sys.argv[2])
    else:
        num_feeds = int(input("Enter the number of feeds to display: "))

    get_latest_feeds(rss_url, num_feeds)
