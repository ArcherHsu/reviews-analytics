

data = []
data2 =[]
new = []

count = 0
with open('reviews.txt','r') as f :
    for line in f:
        data.append(line)
        count+=1
        # if count % 1000 ==0:
        #     print(len(data))

print('檔案讀取完畢, 共有',len(data),'筆留言')        


sum_line = 0
for d in data:
    sum_line+=len(d)
    if len(d) < 100:
        new.append(d)
sum_line = sum_line/len(data)
print('每筆平均長度為:',sum_line,'個字') 
print('長度小於100的留言有',len(new),'筆')



  
