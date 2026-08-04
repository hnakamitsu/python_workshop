import random
import requests

# 目標点数を文字として受け取る
score_text = input("目標のTOEIC点数: ")

# 文字を数字に変換する
score = int(score_text)

# 英単語リストをインターネットから取得する
word_response = requests.get(
    "https://www.newgeneralservicelist.com/s/NGSL_12_stats.csv",
    verify=False,
)

# 取得したデータを文字として保存する
csv_text = word_response.text

# 取得したデータを1行ずつに分ける
csv_lines = csv_text.splitlines()

# 英単語を保存する空のリストを作る
words = []

# 1行目は見出しなので、2行目から繰り返す
for line_data in csv_lines[1:]:

    # 1行分のデータをカンマで分ける
    line_items = line_data.split(",")

    # 最初の項目が英単語
    word = line_items[0]

    # 英単語をリストに追加する
    words.append(word)

# 目標点数に応じて、単語を選ぶ範囲を決める
if score < 500:
    start = 0
    end = 800
elif score < 700:
    start = 800
    end = 1600
elif score < 850:
    start = 1600
    end = 2300
else:
    start = 2300
    end = len(words)

# 指定した範囲からランダムに1単語選ぶ
word_number = random.randint(start, end - 1)
today_word = words[word_number]

# 結果を表示する
print()
print("🎯 今日覚える英単語")
print("--------------------")
print("英単語:", today_word)
