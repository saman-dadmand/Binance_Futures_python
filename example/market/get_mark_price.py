from binance_f import RequestClient
from binance_f.base.printobject import *
from binance_f.constant.test import *

proxyDict = dict(http='http://eniac-service.ir:53128',
             https='http://eniac-service.ir:53128')
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key, proxy=proxyDict)

result = request_client.get_mark_price(symbol="BTCUSDT")

print("======= Mark Price =======")
PrintBasic.print_obj(result)
print("==========================")
