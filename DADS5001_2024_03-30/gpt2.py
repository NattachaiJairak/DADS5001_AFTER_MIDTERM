import requests

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

data = query({"inputs": "I love your pen "})

if data:
    # ดึงเฉพาะข้อความที่สร้างขึ้นมาแสดง
    generated_text = data[0]['generated_text']
    print("Generated Text:", generated_text)
else:
    print("No data received")
