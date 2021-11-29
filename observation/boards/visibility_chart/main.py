from django_plotly_dash import DjangoDash
from dash import html
from dash import dcc
import plotly_express as px
import pandas as pd

app = DjangoDash('visibility_chart')


def _get_graph_data():
    df = pd.DataFrame({'time': [0, 1, 2], 'source_alt': [10, 20, 30], 'moon_alt': [10, 5, 0]})
    return df


def graph():
    chart = dcc.Graph(
        id='visibility_chart',
        figure=px.line(
            _get_graph_data(),
            'time', 'source_alt'
        )
    )
    return chart


def layout():
    div = html.Div(
        [
            graph()
        ]
    )
    return div


app.layout = layout
