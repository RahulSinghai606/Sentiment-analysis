import csv
import random
from datetime import datetime, timedelta

# Helper Functions
def generate_username():
    first_names = [
        "rahul", "priya", "ajay", "anita", "vijay", "neha", "arjun", "sneha", "rohit", "deepika",
        "amit", "shreya", "vikas", "pooja", "ankit", "nisha", "manoj", "kavya", "sandeep", "shruti"
    ]
    last_names = [
        "sharma", "verma", "singh", "patel", "kumar", "gupta", "reddy", "joshi", "mehta", "choudhary"
    ]
    random_number = random.randint(100, 999)
    username_style = random.choice([
        f"{random.choice(first_names)}_{random.choice(last_names)}",
        f"{random.choice(first_names)}{random_number}",
        f"{random.choice(first_names)}.{random.choice(last_names)}"
    ])
    return username_style.lower()

def generate_tweet(sentiment):
    positive_tweets = [
        "I started using @ApolloPharmacy online 2 years ago. Delivery was next day earlier, now it's just 7 mins! Amazing service! #ApolloPharmacy #FastDelivery",
        "Love how @ApolloPharmacy has made healthcare accessible. So proud of their work! #Trust #ApolloPharmacy",
        "Quick delivery and excellent customer support from @ApolloPharmacy. Highly recommend! #CustomerService",
        "@ApolloPharmacy saved my day with their fast response. Thank you! #ApolloPharmacy #Healthcare",
        "Great experience at @ApolloPharmacy! The staff was very friendly and helpful. #PositiveExperience"
    ]
    negative_tweets = [
        "Placed an order with @ApolloPharmacy but didn't receive one of my medicines. Immediate resolution needed! #ApolloPharmacy #Issue",
        "Fake deliveries by @ApolloPharmacy's courier partner. No communication at all! #DeliveryFailed #ApolloPharmacy",
        "Doctor prescribed 3 days of medicine, but @ApolloPharmacy gave me 10 tablets. Not happy with the service! #ApolloPharmacy #PrescriptionError",
        "The delivery guy didn't even call or enter my society. Terrible experience with @ApolloPharmacy. #BadService",
        "Change staff at @ApolloPharmacy MMDA, Chennai. They don't respect patients' prescriptions. #ApolloPharmacy #Complaint"
    ]
    neutral_tweets = [
        "Visited @ApolloPharmacy today. It was okay, nothing special. #NeutralExperience",
        "Ordered some medicines from @ApolloPharmacy. Standard service as usual. #ApolloPharmacy",
        "Picked up my prescription from @ApolloPharmacy. Everything was fine. #NoIssues",
        "Just another day at @ApolloPharmacy. No complaints so far. #Neutral",
        "Used @ApolloPharmacy for the first time. Service was decent. #FirstImpression"
    ]
    
    if sentiment == "Positive":
        return random.choice(positive_tweets)
    elif sentiment == "Negative":
        return random.choice(negative_tweets)
    else:
        return random.choice(neutral_tweets)

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_days = random.randrange(time_between_dates.days)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    return start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

# Main Function to Generate Dataset
def generate_synthetic_dataset(num_tweets=500):
    tweets = []
    start_date = datetime(2024, 11, 1)
    end_date = datetime(2025, 1, 31)
    
    for i in range(num_tweets):
        # Randomly assign sentiment
        sentiment = random.choices(["Positive", "Negative", "Neutral"], weights=[0.5, 0.2, 0.3])[0]
        
        # Generate tweet details
        username = generate_username()
        text = generate_tweet(sentiment)
        likes = random.randint(0, 1000)  # More variability in likes
        retweets = random.randint(0, 200)  # More variability in retweets
        replies = random.randint(0, 100)  # More variability in replies
        created_at = generate_random_date(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S")
        
        # Append to dataset
        tweets.append({
            'id': i + 1,
            'username': username,
            'text': text,
            'likes': likes,
            'retweets': retweets,
            'replies': replies,
            'created_at': created_at
        })
    
    return tweets

# Save Dataset to CSV
def save_to_csv(tweets, filename="apollopharmacy_tweets.csv"):
    keys = ['id', 'username', 'text', 'likes', 'retweets', 'replies', 'created_at']
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(tweets)
        print(f"Dataset saved to {filename}.")
    except Exception as e:
        print(f"Error saving dataset to CSV: {e}")

# Main Execution
if __name__ == "__main__":
    print("Generating synthetic dataset...")
    synthetic_tweets = generate_synthetic_dataset(num_tweets=500)
    save_to_csv(synthetic_tweets)
    print("Synthetic dataset generation complete.")