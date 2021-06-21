'''
    This file contains the code for the Bar charts in part2.
'''

import plotly.graph_objects as go

import hover_template

from plotly.subplots import make_subplots

def plot_g2(df_exp,df_imp):
    #On sépare l'écran en deux subplot nommées importations et exportations
    fig = make_subplots(rows=1, cols=2, shared_xaxes=True, vertical_spacing=0.07, subplot_titles=("Exportations","Importations"))
    #On inverse l'ordre d'affichage des pays
    fig.update_layout(yaxis=dict(autorange='reversed'),yaxis2=dict(autorange='reversed'))
    #Figure d'exportations
    fig.add_trace(go.Bar(
        y=df_exp.Pays,
        x=df_exp.Pourcentage,
        orientation='h',
        showlegend=False,
        hoverinfo='x+y',
        width=0.5,
        marker=dict(
        color='rgba(38, 24, 74, 0.6)',
        line=dict(color='rgba(38, 24, 74, 0.8)',width=1))),
        row=1,col=1)
    #figure d'importations
    fig.add_trace(go.Bar(
        y=df_imp.Pays,
        x=df_imp.Pourcentage,
        orientation='h',
        showlegend=False,
        hoverinfo='x+y',
        width = 0.5,
        marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(color='rgba(50, 171, 96, 1.0)',width=1))),
        row=1,col=2)
    fig.update_layout(template="plotly_white")
    #On change le noms des axes
    fig.update_yaxes(title_text="Pays", row=1, col=1)
    fig.update_xaxes(title_text="%", row=1, col=1)
    fig.update_xaxes(title_text="%", row=1, col=2)
    return fig