import MeCab

mecab = MeCab.Tagger()
mecab.parse('')  # 文字列がGCされるのを防ぐ
text = '今日の朝刊一面は、北朝鮮のミサイル発射に関する記事であった。'
text.encode('utf-8')
result = mecab.parse(text)
print(result)
