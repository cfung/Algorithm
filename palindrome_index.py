# mistake 1: (method 2) end of loop should -1
# mistake 2: (method 2) end of loop forgot idx

n = int(raw_input().strip())

def palindrome(input_str):
    
    if input_str == input_str[::-1]:
        return -1

    for idx, char in enumerate(len(input_str)/2:

        # method 1: compare entire strings
        #newstr = input_str[:idx] + input_str[idx+1:]

        #if newstr == newstr[::-1]:
        #    return idx

        # method 2: compare start and end char
        if input_str[idx] != input_str[len(input_str)-1]:
            if input_str[idx+1] == input_str[len(input_str)-1-idx]:
                return idx
            else:
                return len(input_str)-1-idx
      
for i in range(0, n):
    line = raw_input().strip()
    print palindrome(line)


# sample input: 'aaab'
# sample output: 3

# sample input: 'baa'
# sample output: 0

# sample input: 'aaa'
# sample output: -1

'''
n=int(raw_input())
for n0 in range(n):
    s=list(raw_input())
    if list(reversed(s))==s:
        print -1
    else:
        for _ in range(1,(len(s)/2)+1):
            if s[_-1]!= s[-_]:
                break
        s1=s[:]
        del s[_-1]
        del s1[-_]
        if list(reversed(s))==s:
            print _-1
        else:
            print len(s)+1-_
'''

'''  test case #2
10
ifcldioxqllqxidlcfi
iqnvaakgtilctohorlwwpkcyiskspywxqqxwypsksiyckpwwlrohotclitgkaavnqi
ociyjqnlncsctgbtwlxvvriojinjbbftppubjinwnibhredderhbinwnijbupptfbbjnijoirvvxlwtbgtcscnlnqjyio
nvwcfhsokvvellcpukdtanwihbnxsfpognmlsvejhafnnnnfahjevslmngopsxnbhiwnatdkupcllevvkoshfcwvn
dkldyinimehfvvokkaddakkovvfheminiydlkd
qiuexowegcorhpcxyocgwxelirlobtercyxaowguyvoovyugwoaxycretbolrilexwgcoyxcphrocgewoxeuiq
hmilufjaqutlejuxnmcomeemocmnxujetuqajfulimh
ljqukwwuqjl
pnfvahowbsgxsvkukxyskmuvvmtvuxgnqnlqxcnbuvaptmmmmtpavubncxqlnqngxuvtmvvumksyxkukvsxgsbwohavfp
wbuvyhpuespdrgtfyrhouekuveiiluuliievukeuohryftgrdpeuphyvubw


6
-1
1
29
-1
-1
11
4
1
9
'''