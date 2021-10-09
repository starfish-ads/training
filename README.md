## フェッチ同期/プルの違い

- fetch
リモートブランチの変更を取得する

- pull
リモートブランチの変更を取得して、上書きする
fetchの上位互換

- 同期
同期はVScode独自の機能なので､基本的に使わない

## 機能説明

- リベート
使用頻度低い
過去のコミットをなかったコトにする｡
なかったことにしたというコミットが残るので実質影響は少ない

- リベース
使用頻度低い
過去のコミット自体を変更する
リモートのブランチの形が変わってしまうので､チームで管理している場合は使用は控えたほうがいい

- リセット
指定範囲内のコミットを遡ってまとめることができる｡

- スタッシュ
一時退避 の意味
ローカルで差分のみを一時的に保存しておくことができる


## 修正コミットの考え方
基本的にリベースやリベート､リセットなどは使わずに､
修正コミットでコミットの修正を行う


## Git Graph

コミットの日付が最も新しい場所に【head】がつくが意識しなくていい
origin/main → リモートブランチ
main → ローカルブランチ
GitGraph上で並んでいる場合､同じ断面を持っているという意味

アンコミットチェンジ
hoge3のブランチで作業



## タグに関して
タグはコミットとは別軸で動いている
ローカルでタグを作成しても､【push to remote】をしない限りリモートに存在しないタグなので
ローカルでは自由に作業できる｡ リモートに上げるタグとしては､【Release】など

新しくブランチを作成