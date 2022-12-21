import pyexiv2
import glob
import csv
import sys

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
'''
# 辞書で返って来る
print(metadata)

# 特定のメタデータを指定して取り出す
print("------------------------------")
print("Filename:", filename)
print("DateTimeOriginal:", metadata['Exif.Photo.DateTimeOriginal'])
print("---------------")
print("Make:", metadata['Exif.Image.Make'])
print("Model:", metadata['Exif.Image.Model'])
print("---------------")

# print("FocalLength:", metadata['Exif.Photo.FocalLength'])
# 700/10 と表示されてしまうので、文字列を数値化して計算
x = metadata['Exif.Photo.FocalLength'].split('/')
# なぜか floot(浮動小数点数値) になってしまったので、割り算をしてから再度 int に変換
y = int(x[0]) / int(x[1])
print("FocalLength:", int(y), "mm")

print("FocalLength(35mm):", metadata['Exif.Photo.FocalLengthIn35mmFilm'], "mm")
print("ExposureTime:", metadata['Exif.Photo.ExposureTime'])

# print("FNumber: F", metadata['Exif.Photo.FNumber'])
# 63/10 と表示されてしまうので、文字列を数値化して計算
x = metadata['Exif.Photo.FNumber'].split('/')
print("FNumber: F", int(x[0]) / int(x[1]))

print("ISO Speed:", metadata['Exif.Photo.ISOSpeedRatings'])

# print("ExposureBiasValue(APEX:EV):", metadata['Exif.Photo.ExposureBiasValue'])
# -3/10 と表示されてしまうので、文字列を数値化して計算
x = metadata['Exif.Photo.ExposureBiasValue'].split('/')
print("ExposureBiasValue:", int(x[0]) / int(x[1]), "EV")
print("------------------------------")
'''

header=[]
header.append('filename')

# 一覧表示
# 読み出したいメタデータの名称を調べる
# 何のタグか分かり易いように、値も出力
#headerfile = glob.glob('./header/*')
print(path+foldername+'/')
files = glob.glob(path + foldername + '/*')
with open(path + foldername + "_exif.csv","w") as f:
	writer = csv.writer(f)
	#取得するexifデータと同じ画像を下記の名前で登録。ヘッダファイルを取得するため、
	headimg = pyexiv2.Image("sample.jpg")
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
