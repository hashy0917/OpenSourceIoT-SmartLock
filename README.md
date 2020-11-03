# OpenSourceIoT-SmartLock
**現在試作零号機**

## 使用する物
- RaspberryPi 2 Model B V1.1
- SG92R

## 動作
- フロントエンド
nginxが動作。
/api を バックエンドの `:1323` にリダイレクトする
- バックエンド
golangのechoを使い実装。
`/status` `/locking` `/unlock` の3つを用意
### `/status`
現在のステータスを表示する

### `/locking`
鍵をかけ、ステータスを表示する

### `/unlock`
鍵をあけ、ステータスを表示する
指定されてある秒数後、鍵をかける

## image

