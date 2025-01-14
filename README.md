# mypkg
ロボットシステム学の課題2で作成したものです。

## countupコマンド
[![test](https://github.com/kawamoto21/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/kawamoto21/mypkg/actions/workflows/test.yml)

数字をカウント＋現在時刻を表示  
5カウント後に警告（タイマーのようなもの）が出ます  

##使い方  
2端末使用します。  
1. 片方の端末で 
~~~
$ ros2 run mypkg talker
~~~
2. もう一方で 
~~~
$ ros2 run mypkg listener
~~~

-終了するときは `Ctrl + C`  


-実行例

１． ros2 run mypkg talker
[INFO] [1736529261.859830844] [talker]: Publishing: Count: 0, Time: 2025-01-11 02:14:21

２． ros2 run mypkg listener
[INFO] [1736529261.860827113] [listener]: Received: Count: 0, Time: 2025-01-11 02:14:21

## 必要なソフトウェア
- Python
  - テスト済みバージョン：3.10

## テスト環境
- Ubuntu 22.04 LTS  

このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．  
© 2025 Sou Kawamoto
