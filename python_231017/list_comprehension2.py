seoul_gu = [
    "서대문구", "강동구", "성북구",
    "송파구", "강북구", "중구",
    "강서구", "강남구", "성동구"
    ]

gangs = [i for i in seoul_gu if i[0] == "강"]
print(gangs)

not_3_words = [i for i in seoul_gu if len(i) != 3]
print(not_3_words)