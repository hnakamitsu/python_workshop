# 1行目は見出しなので、2行目から繰り返す
for line_data in csv_lines[1:]:

    # 1行分のデータをカンマで分ける
    line_items = line_data.split(",")

    # 最初の項目が英単語
    word = line_items[0]

    # 英単語をリストに追加する
    words.append(word)
