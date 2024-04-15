reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords():
    for review in reviews:
        review_list = review.split()
        for word in review_list:
            clean_word = word.lower().replace(".", "")
            if clean_word in keywords:
                upper_word = word.upper()
                review.replace(word, word.upper())
                print(review.replace(word, word.upper()))
highlight_keywords()

#sentiment tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

if len(positive_words) == 7:
    num_of_pos = len(positive_words)

    print("There are " + str(num_of_pos) + " positive words!")



    reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords():
    highlighted_reviews = []
    for review in reviews:
        review_list = review.split()
        highlighted_review = ""
        for word in review_list:
            clean_word = word.lower().replace(".", "")
            if clean_word in keywords:
                highlighted_review += word.upper() + " "
            else:
                highlighted_review += word + " "
        highlighted_reviews.append(highlighted_review)
    return highlighted_reviews

if len(negative_words) == 7:
    num_of_neg = len(negative_words)

    print("There are " + str(num_of_neg) + " negative words!")



    reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
key_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


