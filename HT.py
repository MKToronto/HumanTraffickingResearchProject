import plotly.plotly as py
import pandas as pd
import plotly.tools as tls
tls.set_credentials_file(username='marckendal', api_key='c4ZivXd3Vnxntq8QfElS')

df = pd.read_csv('Final_Decisions_2015_Next_Line.csv')
#print(df.head())


data = [ dict(
        type = 'choropleth',
        locations = df['Nationality'],
        locationmode = "country names",
        z = df['Referals in 2015'],
        text = df['Nationality'],
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '$',
            title = 'Referals in 2015'),
      ) ]
      


layout = dict(
    title = 'Referals in 2015',
    geo = dict(
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='d3-world-map' )