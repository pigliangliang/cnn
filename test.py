def match_string(test_string,re_string):
    if test_string == re_string:
        return True
    else:
       # list_test_string= list(test_string)
        if test_string.startswith('*'):
            test_string = test_string.lstrip('*')
        if test_string[0] != re_string[0] and test_string[0] != '?':
            return False
        else:
            test_string = test_string.split("*")
            #test_string is convert to list
            #test_string = ['rer','fdfdfd','ererer?',...]
            for ts in test_string:
                #test_string endwith *
                if ts !='':
                    print(ts)
                    sub_re_string = re_string[:len(ts)]
                    re_string = re_string[len(ts):]
                    print(sub_re_string,re_string)
                    if ts == sub_re_string:
                        return True
                    else:
                        for i in range(len(ts)):
                            if ts[i] ==sub_re_string[i] or ts[i] =='?':
                                continue
                            else:
                                return False
                else:
                    return True

if __name__ =="__main__":
    test = "j?od?f*fdf*"
    re = "jaoduffdfahhfryryr"
    flag = match_string(test,re)
    print(flag)



























