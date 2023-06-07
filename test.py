import pymongo
import matplotlib.pyplot as plt
from pymongo import MongoClient

# MongoDB에 연결
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["students"]

# 데이터 조회

data = collection.find({
    "$or": [
        {"name": "ydh", "height": 176},
        {"name": "kbc", "height": 180},
        {"name": "lgs", "height": 174},
        {"name": "bms", "height": 178},
        {"name": "yyb", "height": 173}
    ]
})

# 데이터 가공
names = []
heights = []
for item in data:
    names.append(item["name"])
    heights.append(item["height"])

# 데이터를 내림차순으로 정렬
sorted_indices = sorted(range(len(heights)), key=lambda k: heights[k], reverse=True)
names = [names[i] for i in sorted_indices]
heights = [heights[i] for i in sorted_indices]

# 색상 리스트
colors = ["salmon", "papayawhip", "lavenderblush", "pink", "lightgray"]

# 그래프 그리기
plt.bar(names, heights, color=colors)

# 축과 제목 설정
plt.xlabel("name", fontsize=12)
plt.ylabel("height", fontsize=10)
plt.ylim(170, 182)
plt.title("students data", fontsize=14)

# 눈금선과 그리드 설정
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.grid(axis="y", linestyle="-", alpha=0.7)

# 막대 위에 값 표시
for i in range(len(names)):
    plt.text(i, heights[i]+1, str(heights[i]), ha="center", va="bottom", fontsize=8)

# 그래프 출력
plt.show()
