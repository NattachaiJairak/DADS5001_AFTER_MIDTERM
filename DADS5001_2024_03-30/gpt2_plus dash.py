import requests
from dash import Dash, html, dcc, Input, Output

# กำหนด URL และ headers สำหรับ API
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # พิมพ์ status code และข้อความที่ได้จาก response เพื่อการดีบัก
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON response")
        return None

# สร้างแอป Dash
app = Dash(__name__)

# ออกแบบเลย์เอาท์ของแอป
app.layout = html.Div([
    dcc.Input(id='input-text', type='text', value='', style={'width': '50%'}),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output-text')
])

# กำหนด callback สำหรับการประมวลผลอินพุตและแสดงผลลัพธ์
@app.callback(
    Output('output-text', 'children'),
    Input('submit-button', 'n_clicks'),
    Input('input-text', 'value')
)
def update_output(n_clicks, input_value):
    if n_clicks > 0 and input_value:
        data = query({"inputs": input_value})
        if data:
            # ดึงเฉพาะข้อความที่สร้างขึ้นมาแสดง
            generated_text = data[0]['generated_text']
            return generated_text
        else:
            return "No data received"
    return ""

# รันเซิร์ฟเวอร์
if __name__ == '__main__':
    app.run_server(debug=True)
