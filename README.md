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

## 접속환경 
[+] jailbreak된 폰에 ssh 연결하기
```
ssh -p 2222 root@localhost  [ 2222 서버 포트 연결 ] -> iproxy 2222(mac port ) [ 2222 포트 리스닝 server 역활 ] -> 22(ios port : client역활 ) -> ssl server demon연결(22 포트 리스닝)

iproxy 2222 22
```

[+] jailbreak된 폰에 ssh 연결하기
```
ssh -p 2222 root@localhost
root/alpine
```

## iso에서 설치

[+] wget 설치

```
apt install wget
```


[+] gcc 설치

```
apt install gcc
```


[+] clang 설치

```
apt install clang
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

[+] flask 설치

```
pip3 install flask
```
[+] git 설치

```
apt install git
```

[+] web shell 설치

```
git clone https://github.com/ox1111/flash_web_shell.git
cd flash_web_shell
```

## 사용법 

[+] mac에서 usb로 웹쉘 연결 포트  설정 
```
iproxy 5000(mac port ) -> 5000(ios port )

iproxy 5000 5000 
```

[+] mac에서 usb로 웹쉘 연결 포트  설정 
```
python3 app.py
```

[+] iphone에서 5000 포트 사용하고 있다고 하면 


```
apt install lsof
```

```
lsof -i :5000
```

```
jang-gyeongchib-ui-iPhone:~/flash_web_shell root# lsof -i :5000
COMMAND    PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
python3.7 3646 root    3u  IPv4 0xd9be63abb3d08a69      0t0  TCP *:commplex-main (LISTEN)
python3.7 3658 root    3u  IPv4 0xd9be63abb3d08a69      0t0  TCP *:commplex-main (LISTEN)
python3.7 3658 root    4u  IPv4 0xd9be63abb3d08a69      0t0  TCP *:commplex-main (LISTEN)
jang-gyeongchib-ui-iPhone:~/flash_web_shell root# kill -9 3646
jang-gyeongchib-ui-iPhone:~/flash_web_shell root# kill -9 3658
jang-gyeongchib-ui-iPhone:~/flash_web_shell root# lsof -i :5000
jang-gyeongchib-ui-iPhone:~/flash_web_shell root# 
```

```
python3 -m venv myenv

source myenv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
pip3 install requests
```

