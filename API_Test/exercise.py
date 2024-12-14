# https: // datatables.net / examples / data_sources / server_side
#
# Go to above application
#
# Read Name called "Sakura" from webtable.
#
# Without changing page entires:
#
# Wihtout search:
#
# --------------------------------
# As soon as we found Sakura, exit from there and display the data
# ---------------------------------------------------------------------------------

import requests
import pandas as pd

# Define the URL and API endpoint
# (you can get the API URL by inspecting the network tab in developer tools)
url = "https://datatables.net/examples/data_sources/server_side"
api_url = "https://datatables.net/examples/server_side/scripts/server_processing.php"
#api_url = "https://datatables.net/examples/data_sources/server_side/scripts/server_processing.php"  # Actual data API endpoint


params = {
    'sEcho': 1,           # DataTables echo parameter
    'iDisplayStart': 0,   # Pagination starting index
    'iDisplayLength': 10  # Number of records per page
}
#  Send a GET request to the API
response = requests.get(api_url,params)

# Get the JSON data from the response
data = response.json()

# Extract the 'data' field from the JSON response
rows = data['data']
# Define the column headers
headers = ["FirstName", "LastName", "Position", "Office", "StartDate", "Salary"]

# Convert the rows into a DataFrame
df = pd.DataFrame(rows, columns=headers)

#
# Filter the row where FirstName is "Sakura" (or any other relevant condition)
filtered_row = df[df["FirstName"] == 'Sakura']

# Display the filtered row(without index)
print(filtered_row.to_string(index=False))





