# 英単語を保存する空のリストを作る
words = []

# 1行目は見出しなので、2行目から繰り返す
for line_data in csv_lines[1:]:

    # 以降は行頭に4個の半角スペースを入れてください

    # 1行分のデータをカンマで分けて最初の項目(英単語)を取得
    word = line_data.split(",")[0]

    # 英単語をリストに追加する
    words.append(word)
