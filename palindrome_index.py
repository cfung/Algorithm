# mistake 1: (method 2) end of loop should -1
# mistake 2: (method 2) end of loop forgot idx
# mistake 3:  cannot enumerate len(input_str)/2, use range
# mistake 4:  if (s[:idx]+s[idx+1:] == (s[:idx]+s[idx+1:])[::-1]):
#             figure out how to remove the idx in substring

n = int(raw_input().strip())

def palindrome(s):
    
    if s == s[::-1]:
        return -1
    else:
        # save time by only going thru 1/2 of the len (only if compare first and last char)
        for idx in range(int(len(s)/2)):
            
            # method 1: compare entire strings (this did not pass last tc due to runtime error)
            #newstr = input_str[:idx] + input_str[idx+1:]

            #if newstr == newstr[::-1]:
            #    return idx

            # method 2: compare char only, start and end char
            if s[idx] != s[len(s)-1-idx]:
                # remove that char, then compare the strings
 
                if (s[:idx]+s[idx+1:] == (s[:idx]+s[idx+1:])[::-1]):
                #if input_str[idx+1:] == input_str[idx+1:][::-1]:#input_str[len(input_str)-1-idx][::-1]:
                    return idx
                else:
                    return len(s)-1-idx
     
                #return (idx if ((s[:idx]+s[idx+1:]) == (s[:idx]+s[idx+1:])[::-1]) else len(s)-1-idx)
                

for i in range(0, n):
    line = raw_input().strip()
    print palindrome(line)

# sample input: 'aaab'
# sample output: 3

# sample input: 'baa'
# sample output: 0

# sample input: 'aaa'
# sample output: -1



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