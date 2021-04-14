with open('me.jpg','rb') as srt:
    with open('copy2.jpg','wb') as tag:
        tag.write(srt.read()) 