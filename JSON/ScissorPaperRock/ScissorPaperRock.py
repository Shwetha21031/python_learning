import json
import random

try:
    with open('Scores.json','r') as file:
        score = json.load(file)
except FileNotFoundError:
    print('file not found')
    temp = {
        "score" : {
            'u':0,
            'c':0
        }
    }
    with open('Scores.json','w') as file:
        json.dump(temp,file)
        with open('Scores.json','r') as file:
            score = json.load(file)
            print(score)
vals = list(score.values())
s = vals[0]


user = int(input("""enter 
     1 for scissor
     2 for paper
     3 for rock \n :  """))

comp = random.randrange(1,4)



if user == comp:
    result = '- Tie -'
elif (user == 1 and comp == 3) or (user == 2 and comp == 1) or (user == 3 and comp == 2):
    result = '- Computer won -'
    s["c"] += 1
else:
    result = '- User won -'
    s['u'] += 1

print("\n",result," \n === scores ===\n User: ",s["u"]," Compter: ",s["c"])

 
with open('Scores.json','w') as file:
    json.dump(score,file,indent=4)
