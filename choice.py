def choicemaker():
    name=input('hi farmer ,enter your name:')
    print('which feature you want to use?')
    [print('-',end='') for x in range(0,29)]
    print('\n')
    print('1.crop recommentation')
    print('2.farming essentials')
    print('3.seed  price analyser')
    print('4.weather forcast -5 days')
    print('5.profit calculator')
    print('6. for quit')
    answer='0'
    while(answer.lower()!='6'):
        answer=input('enter your choice:')
        match int(answer):
            case 1:
                import croprecommendation
                croprecommendation.cropreco(name)
            case 2:
                import farmingessentials
                farmingessentials.farmessent(name)
            case 3:
                import seedpriceanalyser
                seedpriceanalyser.analyser(name)
            case 4:
                import weather
                weather.weather(name)
            case 5:
                import profitcalculator
                profitcalculator.profit(name)
            case 6:
                print('stopping...')
                break
            case _:
                print('invalid choice')

