
# 讀取檔案
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])


# 文字計數

wc = {} # words_count
for d in data: # d為字串，data是清單
	words = d.split() # words是一個清單，裝著一堆字
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增key進wc字典
for word in wc: # 變一行一行
	if wc[word] > 1000000: # 查超過一百次的字
		print(word, wc[word])

print(len(wc)) # 查整個字典有幾個字

while True:
	word = input('請問您想查甚麼字?')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本功能')

# ctrl + / 多行式增加或消除註解
# 算留言平均長度are
#sum_len = 0
#for d in data:
#	sum_len = sum_len + len(d)
#	print(sum_len)
#print('檔案讀取完了，留言平均長度為', sum_len / len(data))


# 篩選清單長度小於100字
#new = []
#for d in data:
#	if len(d) < 100:
#		new.append(d)
#print('一共有', len(new), '筆留言長度小於100')

# 把留言內提到good篩選出來
#good = []
#for d in data:
#	if good in d:
#		good.append(d)
#print('一共有', len(good), '筆留言提到good')

# 計算哪個字出現最多次