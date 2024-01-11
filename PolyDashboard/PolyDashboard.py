from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
# from jinja2 import escape
dataset = pd.read_csv('master_dataset.csv')
dataset['Indigenous_pct'] = pd.to_numeric(dataset['Indigenous_pct'], errors='coerce')
dataset['LBOTE_pct'] = pd.to_numeric(dataset['LBOTE_pct'], errors='coerce')
dataset['ICSEA_value'] = pd.to_numeric(dataset['ICSEA_value'], errors='coerce')

region_count = dataset['ASGS_remoteness'].value_counts()
region_ind = region_count.index
region_ind_list=list(region_ind)
region_list=region_ind_list[:5]

disadvan_m = ['Indigenous %','LBOTE %','ICSEA Score']
stat = ['Mean','Median','Maximum']

app = Dash(__name__)

app.layout = html.Div([
    # Your code here
    dcc.Dropdown(
        region_list,
        region_list,
        multi = True,
        clearable = False,
        id = 'region'),
    dcc.Dropdown(
        disadvan_m,
        'Indigenous %',
        multi = False,
        clearable = False,
        id = 'column'),
    dcc.RadioItems(
        stat,
        'Mean',
        inline = True,
        id = 'statistic'
    ),
    dcc.Graph(id = 'graph')
])

@app.callback(
    Output('graph','figure'),
    Input('region','value'),
    Input('column','value'),
    Input('statistic','value'),
)

def update_graph(region,column,statistic):
    if not region:
         return {}
    col_mapping = {
            'Indigenous %':'Indigenous_pct',
            "LBOTE %":'LBOTE_pct',
            "ICSEA Score":'ICSEA_value'
            }
    col_name = col_mapping[column]

    if statistic == 'Mean':
        regionset = dataset[dataset['ASGS_remoteness'].isin(region_list)]
        barchart_data = regionset.groupby('ASGS_remoteness')[col_name].mean()
    elif statistic == 'Median':
        regionset = dataset[dataset['ASGS_remoteness'].isin(region_list)]
        barchart_data = regionset.groupby('ASGS_remoteness')[col_name].median()
    else:
        regionset = dataset[dataset['ASGS_remoteness'].isin(region_list)]
        barchart_data = regionset.groupby('ASGS_remoteness')[col_name].max()

    fig = px.bar(
            barchart_data.reset_index(),
            x='ASGS_remoteness',
            y=col_name,
            title= '{} {} by Region of NSW'.format(statistic,column),
            labels= {'ASGS_remoteness' : 'Region', col_name : column}
            )
    return fig
# Your code here

if __name__ == '__main__':
    app.run_server(debug=True)