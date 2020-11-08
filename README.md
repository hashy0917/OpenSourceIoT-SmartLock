# OpenSourceIoT-SmartLock
**現在試作零号機**

Version 0.2

## 使用する物
- python3
    + pigpio
    + flask
- RaspberryPi 2 Model B V1.1
- SG92R

## 動作
`/status` `/locking` `/unlock` の3つを用意

### `/status`
現在のステータスを表示する

### `/locking`
鍵をかけ、ステータスを表示する

### `/unlock`
鍵をあけ、ステータスを表示する
指定されてある秒数後、鍵をかける

## 接続
RaspberryPiのGPIO 4をSG92RのControlピンに接続。
残りはGNDと5Vに接続。

## API
### POST
#### unlock
`/api/post/unlock`

#### locking
`/api/post/locking`

## image
![Untitled Diagram](https://user-images.githubusercontent.com/19991619/97961693-203e1800-1df7-11eb-9c40-95071fd7e8a4.jpg)
