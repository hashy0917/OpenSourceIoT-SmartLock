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
未実装

### `/locking`
鍵をかけ、ステータスを表示する

### `/unlock`
鍵をあけ
指定されてある秒数後、鍵をかける
その後、ステータスを表示する

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
![Untitled Diagram](https://user-images.githubusercontent.com/19991619/98459896-90c3ab00-21e2-11eb-93b9-511c50ef54f9.png)
