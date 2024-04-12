import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-box', type='text', value=''),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button')
])

@app.callback(
    Output('output-container-button', 'children'),
    [Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks is not None:
        if value:
            data = query(value)
            if isinstance(data, list):
                generated_text = '\n'.join([d.get('generated_text', 'No response') for d in data])
            else:
                generated_text = data.get('generated_text', 'No response')
            return html.Div(generated_text)
        else:
            return 'Please enter some text.'

if __name__ == '__main__':
    app.run_server(debug=True)
