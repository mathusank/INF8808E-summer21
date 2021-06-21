'''
    This file contains the code for the line chart 1.
'''

import plotly.graph_objects as go

from plotly.subplots import make_subplots


def get_plot(df):
    '''
        Args:
            df: The dataframe to display
        Returns:
            The generated figure
    '''
    fig = go.Figure()
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Exportations internationales'],
        hoverinfo='x+y',
        mode='lines',
        line=dict(color='#2D99FF'),
        name="Exportations internationales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Importations internationales'],
        hoverinfo='x+y',
        mode='lines',
        line=dict( color='#FF40EC'),
        name="Importations internationales"),
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Solde commerciale international'],
        hoverinfo='x+y',
        mode='lines',
        name="Solde commerciale international",
          line= dict(dash="dashdot", 
            color= "rgb(254, 204, 25)")),
      
    )
    
    fig.update_layout(yaxis_range=(-10.914171223568989, 45.36925324781082), title={
        'text': "<b>Commerce International, Québec 1981-2019 (en pourcentage PIB) </b>",
        'xanchor': 'left',
        'yanchor': 'middle'})

    fig.update_layout(hovermode="x unified")
    return fig


    

def update_axes_labels(fig):
    '''

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    fig.update_xaxes(title_text="Année")
    fig.update_yaxes(title_text="Pourcentage du PIB")

    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    fig.update_layout(template='plotly_white')
    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    fig.update_layout(    
        legend_title="")
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="left",
        x=0
        )
    )
    return fig
