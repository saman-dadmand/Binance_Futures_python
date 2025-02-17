# Binance Futures Python SDK

This is Binance Futures Python SDK, a lightweight python library. You can import to your python project and use this SDK to query all market data, trading and manage your account.

The SDK supports both synchronous RESTful API invoking and subscribing the market data and the user's private data from the websocket connection.
## Update log
>1.1.1
>Add proxy support 
>
>1.1.0
>Add binance_d for delivery futures

## Table of Contents

- [Beginning](#Beginning)
  - [Installation](#Installation)

## Beginning

### Installation

*The SDK is compiled by Python 3.7 and above*

For Beta version, please import the source code directly.

```Python
import binance_f  # For perpetual swap
```

```Python
import binance_d  # For delivery futures
```
### Using Proxy
define proxy dict like

proxyDict = dict(http='http://ip:port',
             https='http://ip:port') 
             
use it like below: 

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key, proxy=proxyDict)

The example code is in python3/example.


To install by source code, run below command

```python
python3 setup.py install
```

## License
MIT
