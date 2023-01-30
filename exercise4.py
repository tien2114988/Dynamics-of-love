import numpy as np
import matplotlib.pyplot as plt


def plot(t, R, J):
    plt.plot(t, R, label="Romeo's love")
    plt.plot(t, J, label="Juliet's love")
    plt.xlabel("Time", color="brown")
    plt.ylabel("Love for the other", color="brown")
    plt.title("Love between Romeo and Juliet")
    plt.legend()
    plt.show()


def implicit_euler1(t1, R0, J0, h):
    R1 = (R0+J0*h/(1-h))/(1-h-t1*h*h/(1-h))
    J1 = (J0+R1*t1*h)/(1-h)
    return R1, J1


def implicit_euler2(t1, R0, J0, h):
    R1 = R0/(1-J0*t1*h/(1-(np.e**t1)*h))
    J1 = J0/(1-(np.e**t1)*h)
    return R1, J1


def implicit_euler3(t1, R0, J0, h):
    R1 = (R0/(1-np.sin(t1))*h)
    J1 = J0+(R0/(1-np.sin(t1)*h))*(np.e)*np.cos(t1)
    return R1, J1


def implicit_euler4(t1, R0, J0, h):
    R1 = R0/(1-h*np.log(t1))
    J1 = (J0+R1*h)/(1+h*np.e**t1)
    return R1, J1


def implicit_euler5(t1, R0, J0, h):
    R1 = (R0+h*np.sin(t1**2))/(1-h*2)
    J1 = (J0+np.cos(R1)*h)/(1-h*2)
    return R1, J1


def ex4(R0, J0,  t0, h, implicit_euler):
    R = [R0]
    J = [J0]
    t = [t0]
    while(t0 < 4):
        t0 += h
        R0, J0 = implicit_euler(t0, R0, J0, h)
        t.append(t0)
        R.append(R0)
        J.append(J0)
    plot(t, R, J)


def main():
    R0 = 2
    J0 = 3
    t0 = 0
    h = 0.1
    ex4(R0, J0, t0, h, implicit_euler1)
    ex4(R0, J0, t0, h, implicit_euler2)
    ex4(R0, J0, t0, h, implicit_euler3)
    ex4(R0, J0, t0, h, implicit_euler4)
    ex4(R0, J0, t0, h, implicit_euler5)


if __name__ == "__main__":
    main()
