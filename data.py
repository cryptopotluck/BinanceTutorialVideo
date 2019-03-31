from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df
import keys


def binance_price():
    client = Client(api_key=keys.Pkey, api_secret=keys.Skey)

    candles = client.get_klines(symbol='LTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)

    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame[0]

    final_date = []

    for time in candles_data_frame_date.unique():
        readable = datetime.fromtimestamp(int(time/1000))
        final_date.append(readable)

    candles_data_frame.pop(0)
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)

    dataframe_final_date.columns = ['date']

    final_dataframe = candles_data_frame.join(dataframe_final_date)

    final_dataframe.set_index('date', inplace=True)

    final_dataframe.columns = ['open', 'high', 'low', 'close', 'volume', 'close_time', 'asset_volume', 'trade_number', 'taker_buy_base', 'taker_buy_quote']
    return final_dataframe




