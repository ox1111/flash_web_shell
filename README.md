# flash_web_shell
[ flash_web_shell;; ios에서 사용할 웹셀 맹글어보기 ]
- 아들 교육용
- 악용 시 본인 책임

 ## mac에서 설치

[+] brew 설치

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
[+] iproxy 설치
```
brew install usbmuxd
```

## iso에서 설치

[+] flask 설치

```
pip3 install flask
```

[+] wget 설치

```
apt install wget
```
[+] python 설치

```
apt install python3
```
[+] pip 설치

```
wget https://raw.githubusercontent.com/ox1111/flash_web_shell/master/get-pip.py --no-check-certificate
python3 get-pip.py
```

[+] web shell 설치

```
git clone https://github.com/ox1111/flash_web_shell.git
cd flash_web_shell
```


## 사용법 
[+] jailbreak된 폰에 ssh 연결하기
```
iproxy 2222(mac port ) -> 22(ios port )

iproxy 2222 22
root/alpine
```

[+] mac에서 usb로 웹쉘 연결 포트  설정 
```
iproxy 5000(mac port ) -> 5000(ios port )

iproxy 5000 5000 
```


[+] mac에서 usb로 웹쉘 연결 포트  설정 
```
python3 app.py
```


