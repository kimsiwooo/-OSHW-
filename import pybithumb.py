import pybithumb
import time
import telegram
from datetime import datetime

all = pybithumb.get_current_price("ALL") 
sort_all = sorted(all.items(), key = lambda x : float(x[1]['fluctate_rate_24H']), reverse=True)

cycle_time = 1 
loop_time = 30 * 1 
ascent = 1.0 

sec = 0
prev_ticker = ''
prev_rate = 0
prev_dict = { 'ticker' : 0 }

telgm_token = "" 
            
bot = telegram.Bot(token = telgm_token)
bot.send_message(chat_id='', text="종목|현재가격|전체상승률|1초전상승률|상승률차이")

print("   날짜    현재시간           종목   현재가격   전체상승률   1초전상승률   상승률차이")

for ticker, data in sort_all :        
    prev_dict[ticker] = data['fluctate_rate_24H']

while sec < loop_time :
    all = pybithumb.get_current_price("ALL") 
    sort_all = sorted(all.items(), key = lambda x : float(x[1]['fluctate_rate_24H']), reverse=True)
    
    for ticker, data in sort_all :        
        diff = float(data['fluctate_rate_24H']) - float(prev_dict[ticker])    
        if diff >= ascent :
            print(datetime.now(),"  ", ticker, "  ",data['closing_price'], "      ",data['fluctate_rate_24H'],"      ", float(prev_dict[ticker]),"      ", '%.2f' % diff )
            a=ticker,data['closing_price'],data['fluctate_rate_24H'],float(prev_dict[ticker]), '%.2f' % diff
            telgm_token = ""  
            
            bot = telegram.Bot(token = telgm_token)
    
            bot.send_message(chat_id='', text= a )

        prev_dict[ticker] = data['fluctate_rate_24H']

    time.sleep(cycle_time)
    sec+=cycle_time
