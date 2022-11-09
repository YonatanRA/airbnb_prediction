import json

import plotly
import plotly.express as px



def treemap(data):
   
    fig = px.treemap(data, path=[px.Constant('Madrid'), 'neighbourhood_group', 'neighbourhood'], 
                     values='avg_price', color='avg_price',color_continuous_scale='pinkyl', width=1250, height=575)

    fig.update(layout_coloraxis_showscale=True)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_traces(root_color='blue', hovertemplate='distrito/barrio=%{label}<br>precio=%{value}<extra></extra>')

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

