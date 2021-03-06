import math, time, _thread, sys, os
from User import User



'''from stringbean import stringbean
from pepper import pepper
from eggplant import eggplant
from bokchoy import bokchoy
from container import container
from gardenmixsoil import gardenmixsoil
from water import water'''

'''containers = []'''
'''thewater = water(1000)'''


def WaitForKeyPress(L):
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
        L.append(None)
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
            L.append(None)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


def CreateUsers(test_user):
    ''' Create some random plants'''
    for i in range(1,6):
        test_user.append( User("00{}".format(str(i)),"User{}".format(str(i)),"PW{}".format(str(i)),"User{}@gmail.com".format(str(i))) )
        print ("User{}".format(str(i)))

def Simulate():
    L = []
    timestep = 0
    ''' global thewater
    global containers'''
    _thread.start_new_thread(WaitForKeyPress, (L,))

    while 1:
        time.sleep(1) # delay for 1 second.
        if L: break

        print ("The timestep of the simulation is: {}".format(str(timestep)))
        print("User{} created.".format(str(timestep)))

        timestep+=1

        if timestep%100 ==0: 
            for c in containers:
                c.waterReserve += thewater.Rain()

            '''    for c in containers:
            for v in c.vegtables:
                v.Grow()
                c.nutrientReserve -= 2 * v.Volume()
                c.waterReserve -= 8 * v.Volume()
                if c.nutrientReserve <= 0.0 or c.waterReserve <= 0.0:
                    v.Die()
                    print("YOU KILLED YOUR PLANTS!!!!!")
                    return
            print("Container: Water Reserve {}, Nutrient Level {}".format(str(c.waterReserve),str(c.nutrientReserve)))

            '''

#Remember this method gets executed first since its our 'main'
def main():

    #Make some test users
    test_user = []
    CreateUsers(test_user)

    #Print the test users
    for u in test_user:
        print(u)

    '''   global containers'''
    '''containers.append( container(30, 200, gardenmixsoil("MySoil", 10.0, 20.0, 100.0), veggies) )'''

    print("\nPress Any key to quit simulation...\n")
    ''' Simulate()'''


if __name__ == "__main__":
    main()