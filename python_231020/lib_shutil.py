import shutil

with open("temp.txt", 'w', encoding="UTF-8") as f:
    f.write("테스트를 위한 임시파일")

shutil.copy("temp.txt", "temp2.txt")
shutil.move("temp2.txt", "../temp3.txt")