import pprint
message = '用于幻灯片上，就表现为一个虚框，虚框内部往往有“单击此处添加标题”之类的提示语，一旦鼠标点击之后，提示语会自动消失。\
		当我们要创建自己的模板时，占位符就显得非常重要，它能起到规划幻灯片结构的作用。 用于文档排版的方面，\
		就是当你决定要在版面的一个地方放一张图片或其他东西的时候并且你有多种选择一时决定不了，你就可以先放一个图像占位符设置好宽高，待你以后决定好了再来放入需要的图片。\
		外占位符也常用于网页中调节版面中各部分位置，比如你可以将占位符的高设为1个象素，长度根据需要设置就可以空出你需要的距离，而且在页面上还看不到你的占位符。\
		同样你也可以设置宽为1个象素和你需要的高度来空出你需要的部分与部分之间的垂直距离。\
		占位符的说法也用于文档编辑的其他地方，如project等。'
count = {}
for char in message:
	count.setdefault(char,0)
	count[char] += 1
with open('ts.py','w+') as file_obj:
	file_obj.write(str(count))
pprint.pprint(count)