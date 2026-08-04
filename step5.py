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
