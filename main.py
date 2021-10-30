from os import system, name
import string
from pycoingecko import CoinGeckoAPI

#---------------------------------------------------------------GLOBAL--------------------------------------------------------------------------#

filename = 'db.txt'

cg = CoinGeckoAPI()

total_coins_tracked = 0
list_index = []
date = []
coingecko_id = []
coin_name = []
coin_smart_contract = []
coin_network = []
coin_exchange = []
coin_price_bought = []
total_coins = []
total_spent = []

#---------------------------------------------------------------FUNCTIONS-------------------------------------------------------------------------#

#Read from file
def read_file(file):
    global total_coins_tracked
    
    with open(file) as f:
        for lines in f:
            if (lines[0] != '#'):
                reading_list = lines.split(",")
                list_index.append(reading_list[0])
                date.append(reading_list[1])
                coingecko_id.append(reading_list[2])
                coin_name.append(reading_list[3])
                coin_smart_contract.append(reading_list[4])
                coin_network.append(reading_list[5])
                coin_exchange.append(reading_list[6])
                total_coins.append("{:,}".format(float(reading_list[7])))
                total_spent.append(reading_list[8])
                coin_price_bought.append(format((float(reading_list[8])/float(reading_list[7])),'.20f'))
                total_coins_tracked +=1 

#Print all the coins that I have in my list
def printAllCoins():
    print(f"# \ Date \ CG ID \ Coin \ Smart Contract \ Network\ Exchange \ Price Bought \ Total Coins \ Total Spent TOTAL COINS: {total_coins_tracked}\n")
    for index in range(0,len(list_index)):
        print(f'{list_index[index]}  {date[index]}  {coingecko_id[index]}  {coin_name[index]}  {coin_smart_contract[index]}  {coin_network[index]}  {coin_exchange[index]}  ${coin_price_bought[index]}  {total_coins[index]}  ${total_spent[index]}')  

#Get the coin price by coingecko id using API
def getCoinPrice(crypto_id):
    try:
        dict_output = (cg.get_price(ids=crypto_id, vs_currencies='usd'))
        price = dict_output[crypto_id]['usd']
        return format(price, '.20f')
    except:
        print("ERROR: either coin does not exist or coin id entered is incorrect\n")
    
    
#Get the difference in price from bought to current for coins
def getCoinPriceDifference(current_price, price_bought):
    return format((float(current_price) - float(price_bought)),'.20f')

#Get the total value of the assets with current price
def getCurrentTotalValue(total_coins, current_price):
    float_total_coins = total_coins.replace(',','')
    return format((float(float_total_coins) * float(current_price)),'.3f')

#Will return the diffence in investment 
def getTotalValueDifference(total_spent, current_price, total_coins):
    float_total_coins = total_coins.replace(',','')
    current_total_value = format((float(float_total_coins) * float(current_price)),'.3f')
    return format((float(current_total_value) - float(total_spent)),'.3f')

#Will return to show if investment is up or down
def getValueUpOrDown(total_spent, current_price, total_coins):
    float_total_coins = total_coins.replace(',','')
    current_total_value = format((float(float_total_coins) * float(current_price)),'.3f')
    return 'UP' if float(current_total_value) > float(total_spent) else 'DOWN!'

#Will return price difference info of all coins in details
def getAllCoinValues():
    print(f"# \ Coin \ Total Coins \ Coin Price Bought \ Current Coin Price \ Coin Price Difference \ Total Spent \ Current Total Value \ Value Difference \ Up-Down \n")
    for index in range(0,len(list_index)):
        current_price_api = getCoinPrice(coingecko_id[index])
        print(f'{list_index[index]}  {coin_name[index]}  {total_coins[index]}  ${coin_price_bought[index]} ${current_price_api}  ${getCoinPriceDifference(current_price_api,coin_price_bought[index])}  ${total_spent[index]}  ${getCurrentTotalValue(total_coins[index],current_price_api)}  ${getTotalValueDifference(total_spent[index],current_price_api,total_coins[index])}  {getValueUpOrDown(total_spent[index],current_price_api,total_coins[index])}')  

#Will return price difference info of all coins (basic version)
def getBasicCoinValue():
    print(f"# \ Coin \ Total Spent \ Current Total Value \ Value Difference \ Up-Down \n")
    for index in range(0,len(list_index)):
        current_price_api = getCoinPrice(coingecko_id[index])
        print(f'{list_index[index]}  {coin_name[index]}  ${total_spent[index]}  ${getCurrentTotalValue(total_coins[index],current_price_api)}  ${getTotalValueDifference(total_spent[index],current_price_api,total_coins[index])}  {getValueUpOrDown(total_spent[index],current_price_api,total_coins[index])}')  

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')
  

def menu():
    print("1 - Get Total Coins Tacking\n")
    print("2 - Get All Coin Info\n")
    print("3 - Get Price Details Of Investment\n")
    print("4 - Get Basic Price Details Of Investment\n")
    print("5 - Check Coin Price on CoinGecko\n")
    print("0 - Exit\n")

#---------------------------------------------------------------MAIN----------------------------------------------------------------------------#


read_file(filename)
user_input = -1
coin_id_input = -1
run = False

#Menu loop
while (user_input != '0'):
    if (run == False):
        print("\n\n-----------------------SHIEET COIN SCRIPT-----------------------Created By BitByBit\n\n")
        run = True
    else:
        print("\n\n-----------------------SHIEET COIN SCRIPT-----------------------\n\n")
    menu()
    user_input = input("Please select your option: ")
    clear()
    print('\n\n')
    
    #Start of input checks
    if user_input == '1':
        print(f'Total Coins Tracking: {total_coins_tracked}')
    
    elif user_input == '2':
        printAllCoins()
    
    elif user_input == '3':
        getAllCoinValues()
    
    elif user_input == '4':
        getBasicCoinValue()
    
    elif user_input == '5':
        while (coin_id_input != '0'):
            clear()
            coin_id_input = input("\nEnter Coin Id from CoinGecko (Press 0 to exit): ")
            if (coin_id_input != '0'):
                coin_return = getCoinPrice(coin_id_input)
                if (coin_return != None):
                    print(coin_return)
                input("\nPress Any Key To Continue")
        
    elif user_input == '0':
        continue
    
    else:
        print("Invalid Option Idiot")

    if (coin_id_input != '0'):
        input("\nPress Any Key To Continue")
    coin_id_input = -1
    clear()

print("\n\n\t\tThank you for choosing SHIEET COIN SCRIPT to keep track of how much you are losing! (L) -- BitByBit\n\n")













