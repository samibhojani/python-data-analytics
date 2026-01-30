import statistics

company_name = "Habib Education Trust"
last_post_count = int(input("Total Posts: "))
in_month = input("Month: ")
likes_on_socialmedia_posts = []

for i in range(1, last_post_count + 1):
    likes = int(input(f"likes on post {i}: "))
    likes_on_socialmedia_posts.append(likes)

avg_likes_on_socialmedia_posts = statistics.mean(likes_on_socialmedia_posts)
print(
    f"In the month of {in_month} average number of likes on {company_name}'s Social Media Posts is: {avg_likes_on_socialmedia_posts:.0f}")
