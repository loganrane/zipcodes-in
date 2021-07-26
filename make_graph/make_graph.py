import plotly.express as px
import pandas as pd
import os


def createCountData(df):
    """Function to create the count of each entry state/ut wise.
    @params:
        df: dataframe object of the original data
    @return:
        df: dataframe object with state name and the count of postoffices"""

    # Take the count of each state's entries
    df = df.groupby('state_ut').count()
    # Clean the data as per requirements
    df = df.drop(['zipcode', 'region', 'country',
                  'latitude', 'longitude'], axis=1)
    df = df.rename({'post_office': 'count_post_office'}, axis=1)

    return df


def createChoroplethMap(df):
    """Function to create the choropleth math for count of postoffice in each state
    @params:
        df: dataframe object of count of postoffices in India
    @return:
        fig: plotly figure object with choropleth map"""

    # Update India Map from - https://github.com/datameet/maps
    # Geojson file from - https://stackoverflow.com/questions/60910962/is-there-any-way-to-draw-india-map-in-plotly/
    geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

    fig = px.choropleth(df,
                        geojson=geojson,
                        color="count_post_office",
                        featureidkey='properties.ST_NM',
                        locations="state_ut",
                        color_continuous_scale='Viridis',
                        )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


def main():
    pathToOriginalData = '.\data\zipcode_db.csv'
    pathToCountData = '.\data\\'
    pathToMap = '.\static\\'

    # Read original data and convert to count data
    df = pd.read_csv(pathToOriginalData)
    dfCount = createCountData(df)

    fileName = 'zipcode_count.csv'
    pathToCountData = os.path.join(pathToCountData, fileName)
    dfCount.to_csv(pathToCountData)

    # Create and write the map to a new html file
    df = pd.read_csv(pathToCountData)
    fig = createChoroplethMap(df)

    fileName = 'map.html'
    pathToMap = os.path.join(pathToMap, fileName)
    fig.write_html(pathToMap)


if __name__ == '__main__':
    main()
