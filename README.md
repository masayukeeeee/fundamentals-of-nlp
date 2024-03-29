# 準備

本編とは関係ない部分（環境構築など）をまとめます。

## Mecab

* MeCabとMeCab辞書のインストール

```shell
brew install mecab mecab-ipadic
```

* mecab-ipadic-neologdのインストール

```shell
cd 
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -a
```

* `mecabrc`の辞書変更

`dicdir = /opt/homebrew/lib/mecab/dic/ipadic`の部分を以下のように変更して、利用する辞書を変更する。

```
; dicdir = /opt/homebrew/lib/mecab/dic/ipadic
dicdir = /opt/homebrew/lib/mecab/dic/mecab-ipadic-neologd
```

## Python環境

* `pyenv + poetry`前提

```shell
pyenv install 3.11.4
pyenv local 3.11.4
poetry init
poetry env use 3.11.4
poetry add jupyterlab flake8 pytest mypy mecab-python3
```

* もし`mecabrc`が`/usr/local/...`にないと言われたら、homebrew経由では`/opt/homebrew/etc/mecabrc`にあるので、`.zshrc`に以下を追記する

```shell
export MECABRC="/opt/homebrew/etc/mecabrc"
```


`<project-root>/setup/run-test-mecab.py`を実行して以下のような結果が返ってくればOK。

```shell
poetry run python run-test-mecab.py
> 今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー
> の	助詞,連体化,*,*,*,*,の,ノ,ノ
> 朝刊	名詞,一般,*,*,*,*,朝刊,チョウカン,チョーカン
> 一	名詞,数,*,*,*,*,一,イチ,イチ
> 面	名詞,接尾,助数詞,*,*,*,面,メン,メン
> は	助詞,係助詞,*,*,*,*,は,ハ,ワ
> 、	記号,読点,*,*,*,*,、,、,、
> 北朝鮮	名詞,固有名詞,地域,国,*,*,北朝鮮,キタチョウセン,キタチョーセン
> の	助詞,連体化,*,*,*,*,の,ノ,ノ
> ミサイル	名詞,一般,*,*,*,*,ミサイル,ミサイル,ミサイル
> 発射	名詞,サ変接続,*,*,*,*,発射,ハッシャ,ハッシャ
> に関する	助詞,格助詞,連語,*,*,*,に関する,ニカンスル,ニカンスル
> 記事	名詞,一般,*,*,*,*,記事,キジ,キジ
> で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
> あっ	助動詞,*,*,*,五段・ラ行アル,連用タ接続,ある,アッ,アッ
> た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
> 。	記号,句点,*,*,*,*,。,。,。
> EOS
```
