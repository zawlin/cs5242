import json

shared_test=json.loads(open('data/squad/shared_single.json').read())


answer_single=json.loads(open('out/basic/00/answer/single-020000.json').read())

import string
import re
def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))

ret='Id,Answer\n'
for k in answer_single.keys():
    if k !='scores':
        ret+=k + ',' +normalize_answer(answer_single[k])+'\r\n'
f=open('test.csv','w')
f.write(ret)
f.close()
