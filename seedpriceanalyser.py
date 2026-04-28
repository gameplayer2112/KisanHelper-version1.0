from groq import Groq as myai
import os
from dotenv import load_dotenv
load_dotenv()
grok_key=os.getenv('grok_key2')
client=myai(api_key=grok_key)
#groq api integration for getting prices of crop get compared
#using groq means the data is actually estimated
#future goal is to govt website like mandi
import intro
def analyser(name):
    intro.introduce(name)
    crop=input('Which cropseeds are you buying?')
    unit=input('enter unit for the cropseeds:')
    location=input(f'from which location are you buying  {crop}?')
    price=input(f'at what rate are you buying {crop}?')
    budget=input('what is your budget?')
    area=input('how much area do you have(in acres)?')

    try:
        response=client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            max_completion_tokens=200,
            messages=[{'role':'user','content':f'{name} is buying seeds of{crop} at rate {price} in {unit} from location:{location}, his/her budget is {budget}  with area {area} in acres , tell is the seed buying feasible or not by comparing with market average?be strict and realistic, also tell the diff between the actual market rate and he getting with profit amount and loss  amount , no extra lines just give word outputs '}]
            
        )
        #passing prompt and model with limit to words
        [print('-',end='')for x in range(0,30)]
        print('\n')
        print('using estimated data of ai:')
        print(response.choices[0].message.content)
    except Exception as e:
        print('something went wrong,Sorry!')
        #project crash handling

if __name__=='__main__':
    name=input('enter name:')
    analyser(name)