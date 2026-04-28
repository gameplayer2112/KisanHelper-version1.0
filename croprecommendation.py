import os
from dotenv import load_dotenv
load_dotenv()
my_key=os.getenv('grok_key1')
from groq import Groq as mydataai
client=mydataai(api_key=my_key)
#groq api integration 
import intro
# import module intro for using introduce
def cropreco(name):
    intro.introduce(name)
    print("Can you provide us with the necessary data?")

    location=input('enter location:')
    district=input('enter district:')
    soil=input('enter soil type:')
    water=input('enter water availability:')
    season=input('enter current season:')

    try:
        response=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=200,
        messages=[{"role":"user","content":f'best crops for {district},{location} with {soil} and {water} in {season}season are:Give only crop names and one line reason each. No extra text.'}])
        #passing prompt and model with limit to words
        [print('-',end='')for x in range(0,30)]
        print('\n')
        print(response.choices[0].message.content)
    except Exception as e:
        print('something went wrong,Sorry!')


if __name__=='__main__':
    name=input('enter your name:')
    cropreco(name)
    # for if the file is handled as the main file

