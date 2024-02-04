from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    user_text = input("Enter the text for the word cloud: ")
    
    if user_text:
        generate_word_cloud(user_text)
        generate_word_cloud(user_text)
    else:
        print("No input provided. Exiting.")