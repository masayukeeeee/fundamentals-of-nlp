import MeCab

mecab = MeCab.Tagger()
text = '今日の朝刊一面は、北朝鮮のミサイル発射に関する記事であった。'
result = mecab.parse(text)
print(result)
