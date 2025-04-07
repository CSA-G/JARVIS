from google import genai
gapi= # "USE YOUR GOOGLE GEMINI API 
client = genai.Client(api_key= # "USE YOUR GOOGLE GEMINI API )

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="You are a Virtual assistant name Jarvis and you will perform all the general tasks which I will command just like Alexa and Google "
)
print(response.text)
