# 英単語リストをインターネットから取得する
word_response = requests.get(
    "https://www.newgeneralservicelist.com/s/NGSL_12_stats.csv",
    verify=False,
)

# 取得したデータを文字として保存する
csv_text = word_response.text
