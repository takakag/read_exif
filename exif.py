import pyexiv2
import glob
import csv
import sys
import os

args = sys.argv
#画像データが保存され地えるフォルダの一つ上のフォルダpathを指定
path = './DJI/'
#取得するexifデータと同じ画像を下記の名前で登録。ヘッダファイルを酒盗するため、
#header = u"sample.jpg" headerで渡すとエラーがです。
#画像データが保存されているフォルダ名（引数で渡す
foldername = args[1]
print(foldername)
#filename = 'sample.JPG'
#img = pyexiv2.Image(filename)
#metadata = img.read_exif()

# 辞書で返って来る
# print(metadata)


header=[]
header.append('filename')

# 一覧表示
# 読み出したいメタデータの名称を調べる
# 何のタグか分かり易いように、値も出力
#headerfile = glob.glob('./header/*')
print(path+foldername+'/')
files = glob.glob(path + foldername + '/*')
#print(files[0])
#ファイル名だけ取り出す
#sample = os.path.basename(files[0])
#print(sample)
with open(path + foldername + "_exif.csv","w") as f:
	writer = csv.writer(f)
	#取得するexifデータと同じ画像を下記の名前で登録。ヘッダファイルを取得するため、
	headimg = pyexiv2.Image(files[0])
	headermeta = headimg.read_exif()
#print(headermeta)
	for x in headermeta:
		if x != "Exif.Photo.MakerNote":
	#    		header=[]
	#		header.append('filename')
			header.append(x)
	writer.writerow(header)
	for file in files:
		img = pyexiv2.Image(file)
		metadata = img.read_exif()
		list=[]
		list.append(file)
		for x in metadata:
			if x != "Exif.Photo.MakerNote":
				list.append(metadata[x])
		writer.writerow(list)
#print(x, ":", metadata[x])
