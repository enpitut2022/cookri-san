# cookりさん

チーム名: 注文の多い料理店(チームB)
プロダクト名: cookりさん

## EVP:

[cookりさん] は
[飽きずに冷蔵庫の食材を使い切りたい]を
解決したい
[自炊するものの買い物に行くのが面倒な大学生]向けの
[レシピ検索サービス] です。
これは [最近作ったレシピや家にない食材をはじくこと] によって、
[レシピ共有サイト、まとめ記事、検索エンジン] とは違って
[今ある食材の中でバリエーションに富んだレシピを提案できる]
を実現できます。

## メンバー

- Nakaya (PO)
- orii(ScM)
- Keisuke
- なおと
- ギルド


## 実行手順
1. mainブランチをpullする
```
git pull origin main
```

2. ライブラリをインストールする
```
python -m pip install -r requirements.txt
```

3. uviconでfastapiを実行する
```
uvicorn main:app --reload
```

4. (deta登録してる人用)detaにデプロイする
```
deta deploy
```

## ドライバー用
- 1-4はドライバのみ
- 4が終わった後、5以降は全員がやる

1. [Pull Request](https://github.com/enpitut2022/cookri-san/pulls)を確認する
2. 自分の環境でデバッグしたいプルリクを確認して、以下コマンドを実行
```
git pull 'ブランチ名'
git switch 'ブランチ名'
```
3. FastAPIを実行してテストする
```
uvicorn main:app --reload
```

4. テストをして問題がなかった場合、該当のプルリクのページを開いてリクエストをマージする

5. 自分の環境でmainブランチに戻る
```
git switch main
```
6. リモートリポジトリから最新のコードをpullする
```
git pull origin main
```