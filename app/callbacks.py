# app/callbacks.py

from dash.dependencies import Input, Output
import plotly.express as px

def register_callbacks(app, df):
    """
    Registers callbacks to update charts based on user selections.
    """
    @app.callback(
        [Output('accident-severity-chart', 'figure'),
         Output('traffic-density-chart', 'figure'),
         Output('severity-weather-chart', 'figure'),
         Output('speed-severity-scatter', 'figure')],
        [Input('weather-filter', 'value'),
         Input('time-filter', 'value')]
    )
    def update_charts(selected_weather, selected_time):
        # Filter dataset
        filtered_df = df
        if selected_weather:
            filtered_df = filtered_df[filtered_df['Weather'] == selected_weather]
        if selected_time:
            filtered_df = filtered_df[filtered_df['Time_of_Day'] == selected_time]

        # Accident Severity Chart
        accident_fig = px.bar(
            filtered_df,
            x='Accident_Severity',
            y='Number_of_Vehicles',
            title="Accident Severity vs Number of Vehicles",
            color='Accident_Severity'
        )

        # Traffic Density Chart
        traffic_fig = px.pie(
            filtered_df,
            names='Traffic_Density',
            title="Traffic Density Distribution"
        )

        # Weather Chart
        severity_weather_fig = px.bar(
            filtered_df,
            x='Weather',
            y='Accident_Severity',
            title="Accident Severity by Weather Conditions",
            color='Accident_Severity'
        )

        # Speed and Severity Scatter
        scatter_fig = px.scatter(
            filtered_df,
            x='Speed_Limit',
            y='Accident_Severity',
            title="Speed Limit vs Accident Severity",
            color='Weather'
        )

        return accident_fig, traffic_fig, severity_weather_fig, scatter_fig
