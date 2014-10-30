
import random

print('Welcome to the majic 8-Ball')

while True: 


    print('enter your question:')
    question = input ('>')




    print("You're question is ...",question)

    answers = [
        'Yes.','No.','Maybe','be quit pencil neck',
        'i dont like to be a slave Mr.Garrett',
        'mincraft is awesome ow? sorry i cant answer this question'
    ]

    answer = random.choice(answers)
    print(answer) 
