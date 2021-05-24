from quizmod import quiz
from studentmod import student


class interface:      # interface class determines how program will interact with user


    def __init__(self):
        self.all_quizes1 = {}    #list of quiz objects(quizes) for easy level
        self.all_quizes2= {}    #list of quiz objects(quizes) for intermediate level
        self.all_quizes3= {}    #list of quiz objects(quizes) for advanced level
        while True:
            print('Are you \n1)admin\n2)student\n3)exit')
            usr=int(input())
            if usr==1:
                self.admin()    #if u r admin admin function of interface will be called
            elif usr==2:
                self.student()
            else:
                break


    def admin(self):
        print('1)create quiz\n2)modify a quiz')
        c=int(input())
        print('enter name of quiz')
        qname = input()
        print('select level\n1)beginner\n2)intermediate\n3)advanced')
        k = int(input())

        if c==2:    #if admin wants to modify an existing quiz
            if k==1:
                if qname in self.all_quizes1:
                    print('quiz found ')
                    print('1)add question\n2)modify existing question')
                    s=int(input())
                    if s==2:
                        print('enter question number you want to modify')
                        qno=int(input())
                        self.all_quizes1[qname].createquestions(qno)
                    elif s==1:
                        l=len(self.all_quizes1[qname].question_list)
                        self.all_quizes1[qname].createquestions(l+1)
                else:
                    print('no such quiz exists')

            elif k==2:
                if qname in self.all_quizes2:
                    print('quiz found ')
                    print('1)add question\n2)modify existing question')
                    s=int(input())
                    if s==2:
                        print('enter question number you want to modify')
                        qno=int(input())
                        self.all_quizes2[qname].createquestions(qno)
                    elif s==1:
                        l=len(self.all_quizes2[qname].question_list)
                        self.all_quizes2[qname].createquestions(l+1)
                else:
                    print('no such quiz exists')

            elif k==3:
                if qname in self.all_quizes3:
                    print('quiz found ')
                    print('1)add question\n2)modify existing question')
                    s=int(input())
                    if s==2:
                        print('enter question number you want to modify')
                        qno=int(input())
                        self.all_quizes3[qname].createquestions(qno)
                    elif s==1:
                        l=len(self.all_quizes3[qname].question_list)
                        self.all_quizes3[qname].createquestions(l+1)
                else:
                    print('no such quiz exists')
            else:
                print('invalid choice of level')


        elif c==1:    # if admin wants to create a new quiz
            print('how many questions you want to add into the quiz')
            n = int(input())
            if k==1:
                self.all_quizes1[qname]=quiz()
                for i in range(n):
                    self.all_quizes1[qname].createquestions(i+1)
            elif k==2:
                self.all_quizes2[qname]=quiz()
                for i in range(n):
                    self.all_quizes2[qname].createquestions(i+1)
            elif k==3:
                self.all_quizes3[qname]=quiz()
                for i in range(n):
                    self.all_quizes3[qname].createquestions(i+1)
            else:
                print('invalid choice')
        else:
            print('invalid choice')



    def student(self):
        print('enter your name')
        n=input()
        print('enter your email id')
        e=input()
        s=student(n,e)
        while True:
            print('select level\n1)beginner\n2)intermediate\n3)advanced')
            k = int(input())
            if k==1:
                if len(self.all_quizes1)==0:
                    print('no quiz available please try again later')
                else:
                    print('list of quizs available')
                    for val in self.all_quizes1:
                        print(val)
                    print('name the quiz you want to attempt')
                    choice=input()
                    self.all_quizes1[choice].attempt()
                    m=self.all_quizes1[choice].calculatescore()
                    s.getdetails()
                    print(m)

            elif k==2:
                if len(self.all_quizes2)==0:
                    print('no quiz available please try again later')
                else:
                    print('list of quizs available')
                    for val in self.all_quizes2:
                        print(val)
                    print('name the quiz you want to attempt')
                    choice=input()
                    self.all_quizes2[choice].attempt()
                    m=self.all_quizes2[choice].calculatescore()
                    s.getdetails()
                    print(m)

            elif k==3:
                if len(self.all_quizes3)==0:
                    print('no quiz available please try again later')
                else:
                    print('list of quizs available')
                    for val in self.all_quizes3:
                        print(val)
                    print('name the quiz you want to attempt')
                    choice=input()
                    self.all_quizes3[choice].attempt()
                    m=self.all_quizes3[choice].calculatescore()
                    s.getdetails()
                    print(m)
            else:
                print('invalid choice of level')

            print('Want to attempt another quiz\n1)yes\n2)no')
            sel = int(input())
            if sel == 2:
                break
            elif sel==1:
                continue
            else:
                print('invalid choice')


I =interface()
