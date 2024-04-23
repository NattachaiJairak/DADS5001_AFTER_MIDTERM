from dash import Dash, dcc, html
import plotly.express as px
import dask.dataframe as dd
import time

app = Dash(__name__)

start_time = time.time()
df = dd.read_csv('C:/Nida/DADS5001/DADS5001_AfterMidterm_Class5_2024-04-20/train_credit_bureau_a_2_5.csv')
end_time = time.time()

time_taken = end_time - start_time
row_count = df.shape[0].compute()
unique_case_id_count = df["case_id"].nunique().compute()

print("Time taken to read CSV file:", time_taken, "seconds")
print("Total number of rows in the CSV file:", row_count)
print("Number of unique case_id:", unique_case_id_count)

app.layout = html.Div([
    html.H1("Time taken to read CSV file: " + str(time_taken) + " seconds"),
    html.H1("Total number of rows in the CSV file: " + str(row_count)),
    html.H1("Number of unique case_id: " + str(unique_case_id_count))
])

if __name__ == '__main__':
    app.run_server(debug=True)
