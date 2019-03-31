import plotly.offline as py
import plotly.graph_objs as go

from data import binance_price

table_trace = go.Table(
    domain=dict(x=[0, 0.5],
                y=[0, 1.0]),
    columnwidth=[30] + [33, 35, 33],
    columnorder=[0, 1,2,3,4],
    header= dict(height=50,
                 values =[['<b>Date</b>'], ['<b>Open Price</b>'], ['<b>High Price</b>'], ['<b>Low Price</b>'], ['<b>Close Price</b>'], ['<b>volume</b>'],  ['<b>Number of Trades</b>']],
                 line= dict(color='rgb(50, 50, 50)'),
                 align =['left'] * 5,
                 font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                 fill = dict(color='rgb(135, 193, 238)')
                 ),
    cells= dict(values=[binance_price().index[:], binance_price()['open'],binance_price()['high'], binance_price()['low'], binance_price()['close'], binance_price()['volume'], binance_price()['trade_number']],
                line= dict(color='#106784'),
                align=['left'] * 5,
                font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                format = [None] + [', .2f'] * 2 + [', .4f'],
                prefix = [None] * 2 + ['$', u'\u20BF'],
                suffix = [None] *4,
                height = 27,
                fill=dict(color=['rgb(135, 193, 238)', 'rgba(128, 222, 249, 0.65)']))
)
trace = go.Ohlc(x=binance_price().index[:],
                open=binance_price()['open'],
                close=binance_price()['close'],
                high=binance_price()['high'],
                low=binance_price()['low'])

trace2 = go.Scatter(
    x=binance_price().index[:],
    y=binance_price()['volume'],
    xaxis='x2',
    yaxis='y2',
    line=dict(width=2, color='purple'),
    name='volume'
)

trace3 = go.Scatter(
    x=binance_price().index[:],
    y=binance_price()['trade_number'],
    xaxis='x3',
    yaxis='y3',
    line=dict(width=2, color='green'),
    name='# of trades'
)

axis = dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='#ffffff',
    tickfont=(dict(size=10))
)


layout = dict(
    width=950,
    height=800,
    autosize=False,
    title='Trade Data',
    margin=dict(t=100),
    showlegend=False,
    xaxis1=dict(axis, **dict(domain=[0.55, 1], anchor='y1', showticklabels=False)),
    xaxis2=dict(axis, **dict(domain=[0.55, 1], anchor='y2', showticklabels=False)),
    xaxis3=dict(axis, **dict(domain=[0.55, 1], anchor='y1', showticklabels=False)),
    yaxis1=dict(axis, **dict(domain=[0.66, 1], anchor='x1', hoverformat='.2f')),
    yaxis2=dict(axis, **dict(domain=[0.3 + 0.03, 0.63], anchor='x2', tickprefix='$', hoverformat='.2f')),
    yaxis3=dict(axis, **dict(domain=[0.0, 0.3], anchor='x3', tickprefix='\u20BF', hoverformat='.2f')),

)


fig = dict(data=[table_trace, trace, trace2, trace3], layout=layout)
py.plot(fig, filename='table.html')