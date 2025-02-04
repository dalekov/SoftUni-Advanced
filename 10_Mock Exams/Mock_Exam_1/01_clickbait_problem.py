from collections import deque

suggested_links = deque([int(x) for x in input().split()]) #queue
featured_articles = [int(x) for x in input().split()] #stack

target_value = int(input())
final_feed = []

while suggested_links and featured_articles:
    link = suggested_links.popleft()
    article = featured_articles.pop()

    if link > article:
        greater_element = link
        lesser_element = article
        sequence = suggested_links
    elif link < article:
        greater_element = article
        lesser_element = link
        sequence = featured_articles
    else:
        final_feed.append(0)
        continue

    remainder = greater_element % lesser_element
    if sequence == featured_articles:
        final_feed.append(abs(remainder))
        if not remainder == 0:
            remainder *= 2
            featured_articles.append(remainder)

    elif sequence == suggested_links:
        final_feed.append(-remainder)
        if not remainder == 0:
            remainder *= 2
            suggested_links.append(remainder)

total_value = sum(final_feed)
print(f"Final Feed: {', '.join(map(str, final_feed))}")
if total_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_value}")
else:
    print(f"Goal not achieved! Short by: {target_value - total_value}")

