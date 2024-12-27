# app/dashboard.py

from dash import Dash
from data_cleaning import load_and_clean_data
from layout import create_layout
from data_cleaning import load_and_clean_data
from callbacks import register_callbacks


# Load dataset
DATA_PATH = 'traffic_accident_dataset.csv'
df = load_and_clean_data(DATA_PATH)

# Initialize the app
app = Dash(__name__)

# Set layout
app.layout = create_layout(df)

# Register callbacks
register_callbacks(app, df)

# Check data size
print(df.shape)  # Should print (841, number_of_columns)

# Check the first few rows
print(df.head())

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
