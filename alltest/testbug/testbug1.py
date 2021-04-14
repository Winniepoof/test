lst1=[{'movie':'bwbj','actors':['zzz','aaa']}]



name=input('input a name')
for item in lst1:
    act_lst=item['actors']
    print(act_lst)
    for act in act_lst:
        if name in act:
            print(name+'出演了'+item['movie'])


