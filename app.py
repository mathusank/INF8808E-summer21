
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Alexia Auddino
    Course: INF8808
    Python Version: 3.8

'''
import json
import openpyxl

import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

import barchart_G2
import barchart_g3
import areachart
import linechart_G6
import linechart_G8
from flask_failsafe import failsafe

app = dash.Dash(__name__)
app.title = 'Projet | INF8808'

#manipulation des données pour le graphique 2
data2='assets/data/Data2.xlsx'
df2=pd.read_excel(data2,engine='openpyxl')    
df_exp=df2[df2['Type']=='Export']
df_imp=df2[df2['Type']=='Import']
fig2=barchart_G2.plot_g2(df_exp,df_imp)

#manipulation des données pour le graphique 3
data3='assets/data/Data3.xlsx'
df3=pd.read_excel(data3,engine='openpyxl')    
df3=df3.set_axis(['Ranking','Pays','Country','PIB'],axis=1,inplace=False)
fig3=barchart_g3.plot_g3(df3)

#manipulation des donnees pour le graphique 5
with open('assets/data/G10.json') as data_file:
    data = json.load(data_file)

df = pd.json_normalize(data, 'G10')

fig = areachart.get_plot(df)
fig = areachart.update_animation_hover_template(fig)
fig = areachart.update_axes_labels(fig)
fig = areachart.update_template(fig)
fig = areachart.update_legend(fig)
fig = areachart.add_animation(fig,df)

fig.update_layout(height=600, width=1500)
fig.update_layout(dragmode=False)

#manipulation des donnees pour les graphiques 1 et 4
with open('assets/data/G6.json') as data_file:
    data = json.load(data_file)

df_G6 = pd.json_normalize(data, 'G6')


fig1 = linechart_G6.get_plot(df_G6)
fig1 = linechart_G6.update_axes_labels(fig1)
fig1= linechart_G6.update_template(fig1)
fig1 = linechart_G6.update_legend(fig1)
fig1.update_layout(height=600, width=1100)
fig1.update_layout(dragmode=False)

with open('assets/data/G8.json') as data_file:
    data = json.load(data_file)

df_G8 = pd.json_normalize(data, 'G8')


fig4 = linechart_G8.get_plot(df_G8)
fig4 = linechart_G8.update_axes_labels(fig4)
fig4 = linechart_G8.update_template(fig4)
fig4 = linechart_G8.update_legend(fig4)
fig4.update_layout(height=600, width=1100)
fig4.update_layout(dragmode=False)


app.layout = html.Div(className='content', children=[

html.Header(children=[
        html.H1('Analyse - Le commerce extérieur'),
        html.H2('Intro'),
        html.H4('À plusieurs égards, le Québec peut être considéré comme une économie qui commerce beaucoup avec le reste du monde. En 2019, les exportations internationales québécoises représentaient 28,8 % de son PIB. Le sommet des exportations québécoises en pourcentage du PIB a été atteint en 2000, avec 42,0 % de la production intérieure qui était exportée. Depuis, cette proportion a diminué jusqu’à représenter seulement 25,2 % en 2010, mais reste stable autour de 29 % depuis 2015. '),
        
    ]),
    html.Header(children=[
        html.H2('Précis : Le commerce extérieur'),
        html.H4('Au Québec, le commerce extérieur se divise en deux composantes : les échanges internationaux et les échanges interprovinciaux. Dans une économie ouverte comme celle du Québec, ces deux composantes contribuent pour beaucoup à la vitalité économique. En effet, le solde commercial extérieur (exportations internationales moins importations internationales) entre directement dans l’équation du PIB. Le solde commercial comptabilise les transactions en biens et services entre une juridiction et le reste du monde. ')
    ]),
    html.Header(children=[
        html.H2('Commerce internationale du Québec'),
        html.H4(' Les exportations internationales québécoises en pourcentage du PIB ont explosé à partir de 1990. Cette croissance importante s’est poursuivie jusqu’en 2000. Pendant la décennie des années 1990, marquée par l’entrée en vigueur de l’ALÉNA en 1994, les exportations québécoises connaissent un rythme de croissance annuel composé de 9,1 % ; de 2001 à 2011 toutefois, elles perdent en moyenne 1,8 % par année. Depuis 2012, les exportations sont de nouveau en hausse avec une croissance annuelle moyenne de 3,1 %. ')
        
    ]),
         html.Header(children=[
        html.H4(' Les importations internationales québécoises ont quant à elles connu une croissance constante depuis le début des années 1980. De 1995 à 2000, les importations québécoises ont crû à un rythme annuel composé de 8,7 %.  '),
    ]),
     html.Header(children=[
        html.H4(' Après un ralentissement de la croissance au début de la décennie 2000 (-0,8 % entre 2001 et 2003), elles reprennent une tendance à la croissance rapide jusqu’en 2010 (3,6 %). En 2019, les importations internationales québécoises équivalaient à 34,2 % du PIB, après une croissance annuelle moyenne de 2,3 % depuis 2011. ')
    ]),
     html.Header(children=[
        html.H4('Tel que le montre le graphique 6, le solde commercial international du Québec est négatif depuis 2003. Cela implique que le Québec importe plus de biens et services qu’il n’en exporte. Au cours des trois dernières décennies, l’économie québécoise a alterné entre des périodes où sa balance commerciale était positive (1981-1985, 1994-1996 et 1999- 2002) et des périodes où elle était négative (1986-1993, 1997- 1998 et depuis 2003).')
    ]),

    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig1, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),

    html.Header(children=[
        html.H2("Principaux partenaires du commerce international québécois"),
        html.H4("Les États-Unis sont la principale destination des exportations internationales québécoises en 2019, recevant 71,2 % de celles-ci en termes de valeur. La Chine est le deuxième pays en importance, avec 3,6 % des exportations québécoises, alors que l’Allemagne, troisième, en reçoit 2,2 %. L’ensemble des autres pays reçoit collectivement 23 % des exportations québécoises internationales, mais chaque pays représente moins de 2 % du total."),
        html.H4("Le Québec reçoit également une part importante de ses importations internationales des États-Unis, soit 38,1 %. Si les quatre principaux partenaires sont les mêmes que pour l’exportation (États-Unis, Chine, Allemagne et Mexique), les sources d’importation du Québec sont plus diversifiées que ses destinations d’exportation. "),
        html.H4("12,4 % des importations québécoises proviennent de Chine en 2019, un changement majeur considérant que cette dernière ne figurait pas dans le top 5 il y a dix ans. Par la suite, 4,8 % des importations proviennent de l’Allemagne et 4,7 % du Mexique. Les 40 % restants proviennent des autres partenaires commerciaux, menés par la France (3,6 %), mais comptant tous pour moins de 4 % individuellement."),
    ]),
    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig2, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),
    html.Header(children=[
        html.H2('Encadré 2 : Le Québec, une économie ouverte'),
        html.H4('Lorsqu’on le compare à plusieurs pays, le Québec apparaît comme une économie particulièrement ouverte et commerçante. Le graphique 9 montre que le Québec exporte plus en pourcentage de son PIB (40,5 %) que le Japon (13,3 %) et les États-Unis (7,7 %), si l’on considère la somme des exportations internationales et interprovinciales du Québec. Le constat est similaire au chapitre des importations. L’importance du commerce dans le PIB québécois est comparable à des pays centre-européens, tels la République tchèque (43,5 %) ou la Hongrie (36,7 %).')
    ]),
    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig3, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),

    html.Header(children=[
        html.H2('Commerce international et interprovincial québécois:'),
        html.H4('Le degré d’ouverture de l’économie québécoise est encore plus élevé lorsque l’on tient compte du commerce interprovincial. En termes de valeur, les exportations internationales du Québec totalisent 114,3 G$ en 2019 (en dollars enchaînés de 2012). Les exportations interprovinciales valent quant à elles près de 72,0 G$ ; les exportations québécoises totalisent donc 186,3 G$ (voir graphique 8).')
    ]),
     html.Header(children=[
        html.H4('Les importations internationales et interprovinciales ont connu une évolution légèrement différente des exportations au cours de la période étudiée. En 2019, les importations internationales s’élèvent à 140,8 G$ ; les importations interprovinciales atteignent une valeur de 64,4 milliards de dollars, un chiffre qui a peu fluctué depuis les 15 dernières années.')
    ]),
     html.Header(children=[
        html.H4('Contrairement au solde international, le solde commercial interprovincial du Québec est donc positif et plus ou moins stable depuis 2009. Comme le montre le graphique 8, le solde commercial international négatif du Québec n’est toutefois pas entièrement compensé par son solde commercial interprovincial positif ; en 2019, le solde commercial total du Québec avoisine les -19,0 G$.')
    ]),
     html.Header(children=[
        html.H4('Le solde commercial international du Québec, qui est étroitement lié à l’évolution du taux de change entre les dollars canadien et américain, a commencé à diminuer rapidement à la fin des années 1990.')
    ]),
    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig4, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ]),
        
    html.Header(children=[
        html.H2('5. Part du commerce québécois'),
        html.H4('5.1.    Au fil des années, les exportations internationales ont pris plus d’importance dans le commerce extérieur du Québec. Alors qu’elles représentaient environ 43 % des exportations totales en 1981, elles comptent pour plus de 61 % de celles-ci en 2019.')
    ]),
    html.Header(children=[
        html.H4('5.2.   C’est à partir de 1992 que les exportations internationales commencent à occuper une part majoritaire du commerce extérieur du Québec, une tendance qui sera par la suite accélérée par l’entrée en vigueur de l’ALENA en 1994.')
    ]),
    html.Header(children=[
        html.H4('5.3.    Après l’atteinte d’un sommet à 67 % en 2000, la part internationale des exportations décroît jusqu’en 2011, pour par suite s’installer tout juste au-dessus de 60 % depuis 2015. ')
    ]),
    html.Header(children=[
        html.H4('5.4.    À l’inverse, la part internationale des importations augmente de manière constante depuis 1981 et atteint un sommet à 68,6 % en 2019.')
    ]),
    html.Main(className='viz-container', children=[
        dcc.Graph(className='graph', figure=fig, config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            ))
    ])
])


@failsafe
def create_app():
    '''
        Gets the underlying Flask server from our Dash app.

        Returns:
            The server to be run
    '''
    # the import is intentionally inside to work with the server failsafe
    from app import app  # pylint: disable=import-outside-toplevel
    return app.server


if __name__ == "__main__":
    create_app().run(debug=True)


