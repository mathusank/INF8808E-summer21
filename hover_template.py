'''
    Provides the template for the tooltips.
'''


def get_areachart_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    areachart_hover_template=' <b>Année </b> : %{x} <br> <b>Pourcentage</b> : %{y} % </span><extra></extra>'
    return areachart_hover_template
