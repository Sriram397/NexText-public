
import mysql.connector as connector
import random
mycon = connector.connect(
    host='localhost',
    user='root',
    passwd='password', 
    auth_plugin='mysql_native_password'
)



    
# FUNCTIONS

def setup():       #this creates the table containing the data us all the users
    cur.execute('create database if not exists NexText;')
    cur.execute('use NexText;')
    cur.execute('create table if not exists users ( name varchar(50) primary key,password varchar(50) not null,userid int not null unique);')
    #cur.execute("insert into users(name,password,userid) values('ghfrue','shdfy',32423);")
    #cur.execute("insert into users(name,password,userid) values('ghfue','hdfy',34423);")
    #cur.execute("insert into users(name,password,userid) values('gh','sdfy',38798);")
    #mycon.commit()
    #print("Users table has been created")

def authn():
    start=input("Enter you want to login(1) or sign up(2):")
    if start=='1':        
        return login()
    elif start=='2':
        return signup()
    else:
        print("Please enter only numbers from the give code.")
        print()
        authn()
    
    
    
def signup():      #note : if  name repeats error occus (to be fixed)
    
    #nested functions
    def usid():  #generation if user id such that it is unique but randomly generated
        a=random.randint(10000,99999)        

        #print(a)
        cur.execute('select count(*) from users where userid=%s;',(a,))
        n=cur.fetchone()        
        if n[0]==0:
            return a       #a random unique id has been generated.
        else:
            print('EXCEPTINON----random generated userid is repeating')
            secondtry= usid()  #complex loop where this function itself runs again to give non repeating value.(if in this secondtry also id is same it gos into the elsloop of the second try.this continues until unique valueis achieved.
            return secondtry     
           
    fin_userid=usid()
    name=input("Enter your name:")
    pasd=input("Enter your password:")    
    cur.execute('insert into users(name,password,userid) values(%s,%s,%s);',(name,pasd,fin_userid))
    mycon.commit()
    print('Congratulations!! You have successfully created your account',name,'.')
    return fin_userid

def login():          
    b=input("Enter your name:")
    c=input("Enter your password:")
    cur.execute("select password from users where name=%s;",(b,))
    d=cur.fetchone()
    #print(d)
    if(d==None):
        print()
        print('Seems like you have not created an account yet.')
        print('If you want to try again please press-1')
        print('If you want to create an account(signup) please press-2')
        print()
        inp=input('Enter the number:')
        if(inp=='1'):
            login()
        elif(inp=='2'):
            signup()
        else:
            print('You have incorrectly entered a value.Pleas enter only 1 or 2')
            print('Please login again')
            login()
    elif(d[0]==c):
        print('-'*50,'You have logged in successfully','-'*50)
        print('Welcome back',b,'.')
        cur.execute("select userid from users where name=%s;",(b,))
        id1=cur.fetchone()#insdie tuple
        id2=id1[0]        
        return id2
        
    else:
        print('Please recheck your username and password')#else act only when name is correct but password is wrong
        login()  #runs the function again
        

def delf():          #use with CAUTION
    mf=open('chatf.txt','w')
    mf.close()
    
def chatwrite(cid):

    n1=str(cid)
    mf=open('chatf.txt','a')
    print('Enter text below')
    print('To finish typing type (;;;) and press enter')
    #mf.write()

    mf.write('\n')
    mf.write('---')
    mf.write(n1)
    mf.write('---')
    mf.write('\n')

    y1='y'
    while y1=='y':
        k1=input()    
        if ';;;' in k1:
            k1=k1[0:-3]
            mf.write(k1)
            mf.write('\n')
            break
        mf.write(k1)
        mf.write('\n')
        #y1=input('Do you want to continue(y/n):')


    mf.write('---')
    mf.write(n1)
    mf.write('---')
    mf.write('\n')

    mf.close()







# PROGRAM
cur=mycon.cursor()

setup()
cid=authn()
chatwrite(cid)

mycon.commit()
#print(cid)
    
    
        
#signup()
#name=input("Enter your name:")
#pasd=input("Enter your password:")    
#login(name,pasd)



#c.execute("select * from student")
#x=c.fetchall()
#print(x)
    
