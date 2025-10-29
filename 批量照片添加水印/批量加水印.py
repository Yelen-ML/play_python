from watermarker.marker import add_mark
import os
files=os.listdir('D:\\Python - 副本\\爬取王者荣耀英雄壁纸\\heros')
print(files)
for file in files:
    add_mark(f'D:\\Python - 副本\\爬取王者荣耀英雄壁纸\\heros\\{file}', mark='测试水印',opacity=0.5)