from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D



def sym():

    x, y = symbols("x y")
    y = 2*x
    print(y)

    

    print(y.subs(x, 7))


def sym2():
    x, y = symbols("x y")
    y = -4*x**2+4000*x-200000

    print(y.subs(x, 480))


def sym3():
    c,x,t = symbols("c x t")
    c = x**2+2*x+300
    print(c.subs(x, 20*t))


def fact():
    x, y = symbols("x, y")
    print(factor(x*y**3+2*x**2*y**4))

def expand_express():
    x,y = symbols("x y")

    print(expand(x*(x+y)))

def equation():
    x, r, c = symbols("x r c")
    r = 186*x
    c=109*x+11200.0

    p = solve(Eq(r,c),x)

    r_value = r.subs(x, p[0])

    print(p)
    print(r_value)

def root_example():
    c = [-1, -5, 9, 11]
    c_root = np.roots(c)

    print(c_root)

def plt_show():
    x = np.linspace(-5, 5, 100)
    y = x**2

    plt.plot(x, y)
    plt.show()


#graph 1 - linear
def plt_graph():
    x = ['March', 'April', 'May', 'June', 'July']
    y = [35000, 29000, 27000, 32000, 33000 ]


    plt.plot(x, y)
    plt.plot(x, y, 'r o')
    plt.ylim(0, 90000)

    plt.title('Production')
    plt.xlabel('Month')
    plt.ylabel('Pieces')
    plt.show()

#graph 2 - bars
def plt_graph2():
    month = ['March', 'April', 'May', 'June', 'July']

    x = np.arange(5)

    y = [35000, 29000, 27000, 32000, 33000 ]
    z = [30000, 23000, 47000, 52000, 12000 ]

    wid = 0.5
    plt.bar(x, y, wid, color='r')
    plt.bar(x+wid, z, wid, color='c')

    plt.xticks(x, month)


    plt.title('Production')
    plt.xlabel('Month')
    plt.ylabel('Pieces')
    plt.show()

#graph 3 - pizza
def plt_graph3():
    x = [340, 560,290]
    courses = ['CS', 'Eletrical', 'Production']
    plt.axis('equal')
    plt.pie(x, labels=courses, autopct='%1.1f%%', explode=(0.1,0,0))
    plt.show()

#graph 4 - geometric

def plt_graph4():
    
    height = 7
    lenght = 5

    squared = plt.figure()
    squared1 = squared.add_subplot(111, aspect='equal')

    squared1.add_patch(patches.Rectangle((2,1), 5,7, color='green'))
    plt.ylim(0, 10)
    plt.xlim(0, 10)

    plt.show()

#tridimensional graphs
def plt_graph5():

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(x ,y)
    z = x**2 + y**2

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z)

    plt.show()

#studies 1
def testing_exam():
    y = -7*350**2+5200*350-80000
    print(y)

#diffs - derivadas

def diffs():
    x, f = symbols('x f')
    f = -2*x**3-4*x**2+13*x-1
    m = diff(f, x)
    print(m)

def diffs_sen():
    x, h = symbols('x h')
    h = sin(x)
    m = diff(h, x)
    print(m)

def diffs_second():
    x, f = symbols('x f')
    f = -2*x**3-4*x**2+13*x-1
    m = diff(f, x, 2)
    print(m)

#maximo e minimo
#derivada positiva -> ponto minimo
#derivada negativa -> ponto maximo
def diffs_max():
    x, y = symbols('x y')
    y = -4*x**2+4000*x-200000
    d = diff(y, x)
    d2 = diff(y, x, 2)
    m = solve(Eq(d, 0))
    n = y.subs(x, m[0])
    ds = d2.subs(x, m[0])
    print('Price: ', m[0])
    print('Max value: ', n)
    print('Second diff: ', ds)

def diffs_max_graph():
    x = np.linspace(0, 25, 100)
    c = x**2-20*x+300
    plt.plot(x, c)
    plt.show()


#3d optimization
def optimization_3d():
    x,y,f = symbols("x y f")
    f = x**2+y**2
    fx = diff(f, x)
    fy = diff(f, y)
    fxx = diff(f,x,2)
    fyy = diff(f, y, 2)
    fxy = diff(fx, y)
    fyx = diff(fy, x)

    px = solve(Eq(fx, 0))
    py = solve(Eq(fy, 0))

    fxxp = fxx.subs({x:px[0], y:py[0]})
    fyyp = fyy.subs({x:px[0], y:py[0]})
    fxyp = fxy.subs({x:px[0], y:py[0]})
    fyxp = fyx.subs({x:px[0], y:py[0]})

    D = fxxp*fyyp-fxyp*fyxp
    print('Solution: (%.2f, %.2f)' % (px[0], py[0]))
    print('Det: ', D)
    print('Det relation x: ', fxxp)

def optimization_3d_2():
    xx = np.linspace(-5, 5, 100)
    yy = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(xx, yy)
    f = (1 - x**2)**2+100*(y-x**2)**2

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, f)
    plt.show()


#integrates 

def integral_indef():
    x, f = symbols("x f")

    f = -2*x**3-4*x**2+13*x-1
    i = integrate(f, x)
    print(i)

def integral_def():
    x, f = symbols("x, f")

    f = -2*x**3-4*x**2+13*x-1
    i = integrate(f, (x, 1, 2))
    print(i)


#areas

def areas_math():

    x,f = symbols('x,f')
    f = x**3
    A = integrate(f, (x,1,3))

    x = np.linspace(0.5,3.5,1000)
    f = x**3

    plt.plot(x,f,color='blue')
    plt.axhline(color='blue')

    plt.fill_between(x, f, where=[(x>1) and (x<3) for x in x],color='magenta')
    print('Area: ', A)
    plt.show()