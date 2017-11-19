import pandas as pd

def get_ans_dict(aa,path):
    lines = tuple(open(path, 'r'))[1:]
    ret = []
    for l in lines:
        ls = l.split(',')
        if ls[0] in aa:
            aa[ls[0]].append(ls[1].strip())
        else:
            aa[ls[0]]=[]
            aa[ls[0]].append(ls[1].strip())

def fill_gt(aa,path):
    lines = tuple(open(path, 'r'))[1:]
    ret = []
    for l in lines:
        ls = l.split(',')
        aa[ls[0]].append(ls[1].strip())
ans_all = {}

#get_ans_dict(ans_all,'/home/zawlin/answers_dev/1.csv')
#get_ans_dict(ans_all,'/home/zawlin/answers_dev/2.csv')
#get_ans_dict(ans_all,'/home/zawlin/answers_dev/3.csv')
#get_ans_dict(ans_all,'/home/zawlin/answers_dev/4.csv')
#get_ans_dict(ans_all,'/home/zawlin/answers_dev/5.csv')
#get_ans_dict(ans_all,'/home/zawlin/answers_dev/6.csv')

get_ans_dict(ans_all,'/home/zawlin/answers/1.csv')
get_ans_dict(ans_all,'/home/zawlin/answers/2.csv')
get_ans_dict(ans_all,'/home/zawlin/answers/3.csv')
get_ans_dict(ans_all,'/home/zawlin/answers/4.csv')
get_ans_dict(ans_all,'/home/zawlin/answers/5.csv')
get_ans_dict(ans_all,'/home/zawlin/answers/6.csv')
fill_gt(ans_all,'/home/zawlin/answer_gt.csv')
w = [0.5840717586300626, 0.4751291111715141, 0.5982277792878501, 0.5432182658331068, 0.7120413155748844, 0.5833922261484099]

#w[0]=1.1
#w[1]*=.8
#w[2]*=1.1
#w[4]*=1.2
#w[5]*=.9
#w[5]*=.8
#w[1]*=1.1
def find_auto_weight(w,ans_all):

    for i in range(len(w)):

        total = float(len(ans_all.keys()))
        correct = 0.
        for a in ans_all.keys():
            ans = ans_all[a]
            #print(len(ans))
            gt = ans[-1]

            #print(predict)
            if gt == ans[i]:
                correct += 1
                #print(ans)

        w[i]=correct/total
#find_auto_weight(w,ans_all)
#print(w)
import operator
total = float(len(ans_all.keys()))
correct = 0.
dup =0.
ret = 'Id,Answer\r\n'
for a in ans_all.keys():
    ans = ans_all[a]
    voter = {}
    for i in range(len(w)):
        if ans[i] in voter:
            voter[ans[i]] +=  w[i]
        else:
            voter[ans[i]] = w[i]
    sorted_x = sorted(voter.items(), key=operator.itemgetter(1))[::-1]

    predict = sorted_x[0][0]

    ret+=a + ',' +predict+'\r\n'

f=open('/home/zawlin/answer_f2.csv','w')
f.write(ret)
f.close()

