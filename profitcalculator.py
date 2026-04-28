import intro

def profit(name):
    intro.introduce(name)
    crop = input("Enter crop name: ")
    area = input("Enter area (acres): ")
    seed_cost = input("Enter total seed cost (₹): ")
    fertilizer_cost = input("Enter fertilizer cost (₹): ")
    irrigation_cost = input("Enter irrigation cost (₹): ")
    labour_cost = input("Enter labour cost (₹): ")
    yield_per_acre = input("Enter expected yield per acre (kg): ")
    market_rate = input("Enter current market rate per kg (₹): ")
    result=(float(yield_per_acre)*float(market_rate)*float(area))-(float(irrigation_cost)+float(labour_cost)+float(seed_cost))
    if result>0:
        print(f'your profit for {crop} is {result}')
    else:
        print(f'your loss for {crop} is {result}')

if __name__=='__main__':
    name=input('enter your name:')
    profit(name)