2023 DGIST 컴퓨터 알고리즘 HW3 test case generator입니다.
현재 1번부터 5번까지 지원됩니다.

Linux기준 입니다.

권한 부여와 실행
```bash
sudo chmod +x ./test.sh
./test.sh
```

```bash
start=1
end=4
```

test.sh내에서 여기에 있는 값 조절
```bash
python3 main$i.py < tmp.txt
```
test.sh내에서 여기에 있는 파일 이름을 수정해서 돌릴것
