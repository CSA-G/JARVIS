from google import genai
gapi="AIzaSyCrYWQPt7KfC-kuBiGev_4LXcdmHJN9698"
client = genai.Client(api_key="AIzaSyCrYWQPt7KfC-kuBiGev_4LXcdmHJN9698")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="You are a Virtual assistant name Jarvis and you will perform all the general tasks which I will command just like Alexa and Google "
)
print(response.text)