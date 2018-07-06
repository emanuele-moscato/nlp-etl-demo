from flask import Flask, send_from_directory

import plotly.graph_objs as go
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

server = Flask('tweets-sentiment', static_url_path='')

@server.route('/static/style.css')
def serve_stylesheet():
    return server.send_static_file('style.css')
    
@server.route('/favicon.ico')
def favicon():
    return server.send_static_file('400x400SML-01.png')
    
app = dash.Dash('Tweets sentiment analysis', server=server, url_base_pathname='/', csrf_protect=False)
app.config['suppress_callback_exceptions']=True

app.css.append_css({
    'external_url': '/static/style.css'
})

app.title = 'Tweets sentiment analysis'

tweets_df = pd.read_csv("../output/tweets_with_sentiment.csv")

'''
column_names = {
        'twitter_id': {'title': 'twitter_id'},
        'created_at': {'title': 'created_at'},
        'twitter_user_id': {'title': 'twitter_user_id'},
        'text': {'title': 'text'},
        'is_retweet': {'title': 'is_retweet'},
        'retweet_count': {'title': 'retweet_count'},
        'favorite_count': {'title': 'favorite_count'},
        'sentiment': {'title': 'sentiment'}
}'''
column_names = {
        'created_at': {'title': 'created_at'},
        'text': {'title': 'text'},
        'retweet_count': {'title': 'retweet_count'},
        'favorite_count': {'title': 'favorite_count'},
        'sentiment': {'title': 'sentiment'}
}
headers = html.Tr([html.Th(col, **kwargs) for col, kwargs in column_names.items()])
rows = []

for i in range(len(tweets_df)):
    '''
    row = html.Tr([
        html.Td(tweets_df.iloc[i]['twitter_id']),
        html.Td(tweets_df.iloc[i]['created_at']),
        html.Td(tweets_df.iloc[i]['twitter_user_id']),
        html.Td(tweets_df.iloc[i]['text']),
        html.Td(tweets_df.iloc[i]['is_retweet']),
        html.Td(tweets_df.iloc[i]['retweet_count']),
        html.Td(tweets_df.iloc[i]['favorite_count']),
        html.Td(tweets_df.iloc[i]['sentiment'])
    ])
    '''
    row = html.Tr([
        html.Td(tweets_df.iloc[i]['created_at']),
        html.Td(tweets_df.iloc[i]['text']),
        html.Td(tweets_df.iloc[i]['retweet_count']),
        html.Td(tweets_df.iloc[i]['favorite_count']),
        html.Td(tweets_df.iloc[i]['sentiment'])
    ])
    rows.append(row)

table = html.Table([headers] + rows)

app.layout = html.Div(
    id='app-container',
    children=[
        html.H1("Latest tweets from @bbc"),
        html.Button('Update', id='update-button'),
        html.Div(
            id='table-container'
        )
    ]
)

@app.callback(
    Output(component_id='table-container', component_property='children'),
    [Input('update-button', 'n_clicks')]
)
def write_params(n_clicks):
    if n_clicks and n_clicks>0:
        tweets_df = pd.read_csv("../output/tweets_with_sentiment.csv")
        column_names = {
                'created_at': {'title': 'created_at'},
                'text': {'title': 'text'},
                'retweet_count': {'title': 'retweet_count'},
                'favorite_count': {'title': 'favorite_count'},
                'sentiment': {'title': 'sentiment'}
        }
        headers = html.Tr([html.Th(col, **kwargs) for col, kwargs in column_names.items()])
        rows = []
        if len(tweets_df)<100:
            n_rows = len(tweets_df)
        else:
            n_rows = 100
            
        for i in range(n_rows):
            row = html.Tr([
                html.Td(tweets_df.iloc[i]['created_at']),
                html.Td(tweets_df.iloc[i]['text']),
                html.Td(tweets_df.iloc[i]['retweet_count']),
                html.Td(tweets_df.iloc[i]['favorite_count']),
                html.Td(tweets_df.iloc[i]['sentiment'])
            ])
            rows.append(row)

        return html.Table([headers] + rows)
        

if __name__ == '__main__':
    server.run(port=8888, debug=True)