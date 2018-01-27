
def max_substring(s,n):
    '''
    :param s:
    :param n:
    :return
    '''
    #inpur string s,max no repeat string
    lists = list(s)
    dict_substring = {}
    for i in range(len(lists)):
        sets=set()
        for ls in lists[i:]:
            sets.add(ls)
            if len(sets)<=n:
                continue
            else:
                ls_index = lists.index(ls)
                dict_substring[s[i:ls_index]]=len(s[i:ls_index])
                break

    return dict_substring

if __name__ =="__main__":
    s = 'uabbcadbaefc'
    dict_sub={}
    dict_sub=max_substring(s,4)
    #for item in dict_sub.items():
    #   print(item)
    print(max(dict_sub,key=lambda x:dict_sub[x]))



