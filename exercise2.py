import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig


def ex2(a, b, c, d, initial):
    A = np.array([[a, b], [c, d]])
    equation(A, initial)
    plt.legend()
    plt.show()
    phase_portrait(A, initial)
    plt.legend()
    plt.show()


def equation(A, initial):
    t = np.linspace(0, 10, 1000)
    e_val, e_vec = eig(A)
    if e_val[0] == e_val[1]:
        e_vec[:, 1] = 0, e_vec[0, 0]/A[0, 1]
        c1, c2 = np.dot(np.linalg.inv(e_vec), initial)
        R = (c1*e_vec[0, 0]+c2*(e_vec[0, 0]*t+e_vec[0, 1]))*np.e**(e_val[0]*t)
        J = (c1*e_vec[1, 0]+c2*(e_vec[1, 0]*t+e_vec[1, 1]))*np.e**(e_val[0]*t)
    else:
        c1, c2 = np.dot(np.linalg.inv(e_vec), initial)
        R = c1*np.e**(e_val[0]*t)*e_vec[0, 0]+c2*np.e**(e_val[1]*t)*e_vec[0, 1]
        J = c1*np.e**(e_val[0]*t)*e_vec[1, 0]+c2*np.e**(e_val[1]*t)*e_vec[1, 1]

    plt.plot(t, R, label="Romeo's love")
    plt.plot(t, J, label="Juliet's love")
    plt.xlabel("Time", color="brown")
    plt.ylabel("Love for the other", color="brown")
    str1 = type_of_love(A[0, 0], A[0, 1])
    str2 = type_of_love(A[1, 1], A[1, 0])
    if(str1 == str2):
        plt.title(("love between " + str1+"s").upper(), color="blue")
    else:
        if(str1 == "Eager Beaver"):
            str1 = "an "+str1
        else:
            str1 = "a "+str1
        if(str2 == "Eager Beaver"):
            str2 = "an "+str2
        else:
            str2 = "a "+str2
        plt.title(("love between " + str1+" and "+str2).upper(), color="blue")

    plt.legend()


def phase_portrait(A, initial):
    vector_field(A)
    nullcline(A)
    e_val, e_vec = eig(A)
    print(e_vec)

    trajectory(A, e_vec[:, 0])  # optional
    trajectory(A, e_vec[:, 1])  # optional
    trajectory(A, initial)  # optional
    trajectory(A, -initial)  # optional

    plt.scatter(0, 0, marker="o", label="Fixed point")
    plt.xlabel("Romeo's love for Juliet", c="brown")
    plt.ylabel("Juliet's love for Romeo", c="brown")
    str1 = type_of_love(A[0, 0], A[0, 1])
    str2 = type_of_love(A[1, 1], A[1, 0])
    if(str1 == str2):
        plt.title(("love between " + str1+"s").upper(), color="blue")
    else:
        if(str1 == "Eager Beaver"):
            str1 = "an "+str1
        else:
            str1 = "a "+str1
        if(str2 == "Eager Beaver"):
            str2 = "an "+str2
        else:
            str2 = "a "+str2
        plt.title(("love between " + str1+" and "+str2).upper(), color="blue")
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)


def trajectory(A, initial):
    t = np.linspace(0, 10, 1000)
    e_val, e_vec = eig(A)

    if e_val[0] == e_val[1]:
        e_vec[:, 1] = 0, e_vec[0, 0]/A[0, 1]
        c1, c2 = np.dot(np.linalg.inv(e_vec), initial)
        R = (c1*e_vec[0, 0]+c2*(e_vec[0, 0]*t+e_vec[0, 1]))*np.e**(e_val[0]*t)
        J = (c1*e_vec[1, 0]+c2*(e_vec[1, 0]*t+e_vec[1, 1]))*np.e**(e_val[0]*t)
    else:
        c1, c2 = np.dot(np.linalg.inv(e_vec), initial)
        R = c1*np.e**(e_val[0]*t)*e_vec[0, 0]+c2*np.e**(e_val[1]*t)*e_vec[0, 1]
        J = c1*np.e**(e_val[0]*t)*e_vec[1, 0]+c2*np.e**(e_val[1]*t)*e_vec[1, 1]

    plt.plot(R, J, label="Trajectory")


def vector_field(A):
    x = np.linspace(-4, 4, 17)
    y = np.linspace(-4, 4, 17)
    u = np.array([(i, j) for i in x for j in y])
    du = np.dot(A, u.T).T
    plt.quiver(u.T[0], u.T[1], du.T[0], du.T[1], width=0.001, color="#0099CC",
               label="Vector field")


def nullcline(A):
    R = np.linspace(-4, 4, 1000)
    plt.plot(R, -A[0, 0]*R/A[0, 1], ls=':', label="Nullcline 1")
    plt.plot(R, -A[1, 0]*R/A[1, 1], ls=':', label="Nullcline 2")


def type_of_love(a, b):
    if a > 0 and b > 0:
        return "Eager Beaver"
    elif a > 0 and b < 0:
        return "Narcissistic Nerd"
    elif a < 0 and b > 0:
        return "Cautious Lover"
    else:
        return "Hermit"


def main():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    R0 = int(input("R0 = "))
    J0 = int(input("J0 = "))
    ex2(a, b, c, d, np.array([R0, J0]))


if __name__ == "__main__":
    main()
