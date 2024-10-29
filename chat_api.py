import time
from g4f.client import Client

client = Client()

words = [""]

def what_beats(it: str) -> str:
    # Hardcoded options (helps saving credits)
    if it == "rock":
        return "paper"

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", 
            "content": "Please find an applicable original creative answer in one word to this question: \"What beats " + it + "?\""
        }],
        kwargs={"temperature": 0.4} # Low temperature -> more creativity
    )
    beater = chat_completion.choices[0].message.content.lower()
    
    beater = beater.replace(".", "")
    beater = beater.replace("\"", "")

    if len(beater.split(" ")) > 2:
        beater = beater.split(" ")[0]

    if len(beater) > 15:
        beater = beater[:15]

    if beater in words:
        print("Word already typed: " + beater)
        time.sleep(1)
        return what_beats(it + ", find an answer that is not the word '" + beater + "'")

    print("Formatted: " + beater)
    return beater