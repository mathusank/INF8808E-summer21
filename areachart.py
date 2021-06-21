'''
    This file contains the code for the area chart.
'''

import plotly.graph_objects as go

import hover_template

from plotly.subplots import make_subplots


def get_plot(df):
    '''
        Args:
            df: The dataframe to display
        Returns:
            The generated figure
    '''
    fig = go.Figure()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.07, subplot_titles=("Exportations","Importations"))
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Exportations, part internationale'],
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#2c4674'),
        stackgroup='one', # define stack group
        name="Exportations, part internationale"),
        row=1, col=1
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Exportations, part interprovinciale'],
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#Adc5f1'),
        stackgroup='one',
        name="Exportations, part interprovinciale"),
        row=1, col=1
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Importations, part internationale'],
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#F1be03'),
        stackgroup='one', # define stack group
        name="Importations, part internationale"),
        row=2, col=1
    )
    fig.add_trace(go.Scatter(
        x=df['Annee'], y=df['Importations, part interprovinciale'],
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#F9eec6'),
        stackgroup='one',
        name="Importations, part interprovinciale"),
        row=2, col=1
    )
    fig.update_layout(yaxis_range=(0, 100), title={
        'text': "<b>Parts internationale et interprovinciale des exportations et importations au Québec, de 1981 à 2019 </b>",
        'y':0.97,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

    fig.update_layout(hovermode="x")
    return fig


def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''

    fig.update_traces(hovertemplate=hover_template.get_areachart_hover_template())
    return fig
    



def update_axes_labels(fig):
    '''

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    fig.update_xaxes(title_text="Année", row=2, col=1)
    fig.update_yaxes(title_text="%", row=1, col=1)
    fig.update_yaxes(title_text="%", row=2, col=1)
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
    fig.update_layout(template='simple_white')
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
    legend_title=""
    )
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.3,
    xanchor="left",
    x=0
))
    return fig

def add_animation(fig,df):
    '''
        Add animation (with button) and shape to highlight some infos corresponding to the text.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    info1 = [dict(text=df['Exportations, part internationale'][0], x=df['Annee'][0], y=df['Exportations, part internationale'][0], textposition="top right"), dict(text=df['Exportations, part internationale'][len(df)-1], x=df['Annee'][len(df)-1], y=df['Exportations, part internationale'][len(df)-1])]
    info2 = [dict(type="line", x0=1992, y0=0, x1=1992, y1=100,line=dict(color="Black", width=6, dash="dot")),dict(type="line", x0=1994, y0=0, x1=1994, y1=100,line=dict(color="Black", width=6, dash="dot"))]
    info22 = [dict(text='ALENA', x=1994, y=50, textposition="top right")]
    info3 = [dict(type="circle",xref="x", yref="y",fillcolor="Black",x0=1999.6, y0=60, x1=2000.4, y1=74,line_color="Black")]
    info33 = [dict(text='67%', x=2000, y=67, textposition="top right")]
    info4 = [dict(type="circle",xref="x", yref="paper",fillcolor="Black",x0=2018.6, y0=0.26, x1=2019.4, y1=0.34,line_color="Black")]
    info44 = [dict(text=df['Importations, part internationale'][len(df)-1], yref="paper", x=df['Annee'][len(df)-1], y=0.3)]

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                y=0.25,
                yanchor="bottom",
                x=1.05,
                xanchor="left",
                buttons=[
                    dict(label="None",
                        method="relayout",
                        args=[dict(shapes=[], annotations=[])]), 
                    dict(label="5.1",
                        method="relayout",
                        args=[dict(shapes=[], annotations=info1)]),
                    dict(label="5.2",
                        method="relayout",
                        args=[dict(shapes=info2, annotations=info22)]),
                    dict(label="5.3",
                        method="relayout",
                        args=[dict(shapes=info3, annotations=info33)]),
                    dict(label="5.4",
                        method="relayout",
                        args=[dict(shapes=info4, annotations=info44)]),
                    dict(label="All",
                        method="relayout",
                        args=[dict(shapes=info2+info3+info4, annotations=info1+info22+info33+info44)]),
                ],
            )
        ]
    )
    return fig
