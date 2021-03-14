import numpy as np
from math import sin, cos, tan, asin, acos, atan, exp, log10, log2, log
import matplotlib.pyplot as plt

class IntegralCalculator:
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.n = n
        self.f = f
    
    def monteCarloIntegral(self):
        integral = 0.0
        dx = (self.b - self.a)/float(self.n)
        values = np.random.uniform(self.a, self.b, self.n)

        for element in values:
            integral += self.f(element)

        return integral * dx

    def plotHistogram(self):
        areas = np.array([], dtype=np.float64)
        for _ in range(self.n):
            areas = np.append(areas, self.monteCarloIntegral())
        plt.title("Area Distribution")
        plt.hist(areas, bins=30, ec='black')
        plt.xlabel("Area Calculated")
        plt.ylabel("Number of Calculations")
        plt.show()

    def leftReimannSum(self):
        integral = 0.0
        dx = (self.b - self.a)/float(self.n)

        for i in range(self.n):
            integral += self.f(self.a + i * dx)
        
        return integral * dx

    def rightReimannSum(self):
        integral = 0.0
        dx = (self.b - self.a)/float(self.n)

        for i in range(1, self.n + 1):
            integral += self.f(self.a + i * dx)
        
        return integral * dx

    def midReimannSum(self):
        integral = 0.0
        dx = (self.b - self.a)/float(self.n)

        for i in range(1, self.n):
            integral += self.f(self.a + float(i - .5) * dx)
        
        return integral * dx

    def trapezoidReimannSum(self):
        integral = 0.0
        dx = (self.b - self.a)/float(self.n)

        for i in range(self.n):
            integral += (self.f(self.a + i * dx) + self.f(self.a + (i + 1) * dx))/2
        
        return integral * dx

if __name__ == "__main__":
    print("Welcome to the Numerical Integral Calculator!")
    try:
        A = float(input("Initial Limit of Integration:\n"))
        B = float(input("Final Limit of Integration:\n"))
        N = int(input("Number of Rectangles:\n"))
        func_inp = input("Enter the function you want to integrate (pythonic form):\n")
        calculator = IntegralCalculator(A, B, N, lambda x: eval(func_inp))
        print(f'Monte-Carlo Integral: {calculator.monteCarloIntegral()}')
        print(f'Left Reimann Sum: {calculator.leftReimannSum()}')
        print(f'Middle Reimann Sum: {calculator.midReimannSum()}')
        print(f'Trapezoid Reimann Sum: {calculator.trapezoidReimannSum()}')
        print(f'Right Reimann Sum: {calculator.rightReimannSum()}')
        calculator.plotHistogram()
    except Exception:
        print("Bad Input. Try Again")
