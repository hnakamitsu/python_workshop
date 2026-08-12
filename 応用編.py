import sys
import random
import requests

# 入力された文字を受け取る
score_text = input("目標のTOEIC点数: ")

# 数字でなければ、ここで終了する
if not score_text.isdigit():
    print("数字で入力してください")
    sys.exit(1)

# 文字を数字に変換する
score = int(score_text)

# 10未満、または990を超える点数は使えない
if score < 10 or score > 990:
    print("TOEICは10点から990点です")
    sys.exit(1)

# TOEICは5点刻み
if score % 5 != 0:
    print("TOEICは5点刻みです")
    sys.exit(1)

# 英単語リストをインターネットから取得する
word_response = requests.get(
    "https://www.newgeneralservicelist.com/s/NGSL_12_stats.csv",
    verify=False,
)

# 取得したデータを文字として保存する
csv_text = word_response.text

# 取得したデータを1行ずつに分ける
csv_lines = csv_text.splitlines()

# 英単語を保存する空のリストを作る
words = []

# 1行目は見出しなので、2行目から繰り返す
for line_data in csv_lines[1:]:
    line_items = line_data.split(",")
    word = line_items[0]
    words.append(word)

# 目標点数に応じて、単語を選ぶ範囲を決める
if score < 500:
    start = 0
    end = 800
elif score < 700:
    start = 800
    end = 1600
elif score < 850:
    start = 1600
    end = 2300
else:
    start = 2300
    end = len(words)

# 指定した範囲からランダムに1単語選ぶ
word_number = random.randint(start, end - 1)
today_word = words[word_number]

# 英和辞書APIから日本語訳を取得する
meaning_response = requests.get(
    "https://api.excelapi.org/dictionary/enja",
    params={
        "word": today_word,
    },
    verify=False,
)
meaning = meaning_response.text.strip()

# 結果を表示する
print()
print("🎯 今日覚える英単語")
print("--------------------")
print("英単語:", today_word)
print("日本語:", meaning)
