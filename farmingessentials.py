from groq import Groq as myai
import os
from dotenv import load_dotenv
load_dotenv()
grok_key=os.getenv('grok_key3')
client=myai(api_key=grok_key)
# groq api integration 
import intro
# import module intro for using introduce
def farmessent(name):
    intro.introduce(name)
    crop=input('enter the crop for which you want to get details:')
    try:
        response=client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            max_completion_tokens=200,
            messages=[{"role":"user","content":f"generate farming essentials for {crop} which include: fertilizer name recommendations,care-tips , irrigation for crops. Give necessary data ,one line each with no extra text."}]
            #passing prompt and model with limit to words
            )
        [print('-',end='')for x in range(0,30)]
        print('\n')
        print(response.choices[0].message.content)

    except Exception as e:
        print('something went wrong .sorry!')
        #project crash handling
        
if __name__=='__main__':
    name=input('enter name:')
    farmessent(name)
    # for if the file is handled as the main file