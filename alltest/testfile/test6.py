

src_jpg=open('me.jpg','rb')

tag_jpg=open('copy.jpg','wb')

tag_jpg.write(src_jpg.read())

src_jpg.close()
tag_jpg.close()
