import mysql.connector as sql

conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= '89012345', database='CourierServiceSystem' )
cust1=conn.cursor()

print('WELCOME TO BLUE SKY CARRIERS')

print('Hi')

o=input('Press enter to begin your courier surfing')
print('1.CREATE YOUR SKY ACCOUNT')
print('2.LOGIN')

choose=int(input('ENTER (1) FOR NEW ACCOUNT OR (2) FOR LOGIN:'))

#B_COURIER_MENU
def Bcourier():
    import mysql.connector as sql
    
    conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= '89012345', database='CourierServiceSystem' )
    cust1=conn.cursor()
    for i in range(0,76):
        print('WELCOME TO BLUE SKY CARRIERS:')
        print('1.Courier_order and customer_details')
        print('2.Billing_procedure')
        print('3.Courier_service_boys')
        print('4.Exit')


        choice=int(input('Enter the section you want to access:....(1,2,3or4)	'))
        
        if choice==1:
            print('A:Courier placement')
            print('B:Courier order list')
            sect=input('Enter the section that you want to access:')
            if sect=="A":
                print('COURIER-ORDER')
                a=input('Enter the customer name:')
                b=int(input('Enter the customer mobile number:'))
                c=input('Enter the customer address:')
                d=input('Enter the receiver name:')
                e=int(input('Enter the receiver mobile number:'))
                f=input('Enter the receiver address:')
                cust1.execute("INSERT INTO courier VALUES(' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" ');")
                conn.commit()
                print(cust1.rowcount,'courier (s) placed')
                print('===============================================================================================================')
            elif sect=="B":
                S=input('Do you want to see your courier_order''(yes...\..no):')
                if S=="yes":
                    a=input('Enter the customer mob number:')
                    cust1.execute('select * from courier where Mobilenumber="{}"; '.format(a))
                    order=cust1.fetchall()
                    print('customer name,','customer mob no,','customer address,','receiver name,','receiver mob no,','receiver address:')
                    for j in order:
                        print(j)
                        print('===============================================================================================================')
                else:
                    print('Thank you')
                    
                    print('==============================================================================================================')
        elif choice==2:
            print('BILLING  PROCEDURE:[weight_in_kgs  AND	cost_in_rupees]')
            cust1.execute("select * from bills;")
            bill=cust1.fetchall()
            for x in bill:
                print(x)
                print('===============================================================================================================')
           
                
        elif choice==3:
            city1=input('Enter your city name:')
            z="select * from sboy where City_name='{}';".format(city1)
            cust1.execute(z)
            boys=cust1.fetchall()
            print('City courier_boy mobile no.:')
            for y in boys:
                print(y)
                print('===============================================================================================================')
            if cust1.fetchone() is None :
                print("Servise is Unavailable in your city at the moment. Sorry for incovenience.")
            else :
                print("Thank You for chosing BLUE SKY")
        elif choice==4:
            quit()


if choose==1:
    name=input('Enter your user-name:')
    passwd=input('Set your password (Numeric character only):')
    passwd1=input('Confirm password:')
    cust1.execute("INSERT INTO login VALUES(' "+name+" ',' "+passwd+" ');")
    conn.commit()
    print('ACCOUNT CREATED CONGRATULATIONS')
    move_in=input('Press enter to login')
    Bcourier()

elif choose==2:
    email=input('Enter your UserName')
    passd=input('Enter your PASSWORD:')
    cust1.execute('select * from login where name=" '+email+' " and passwd=" '+passd+' "; ')
    if cust1.fetchone() is None:
        print(' Sorry your password in wrong')
    else:
        Bcourier()


