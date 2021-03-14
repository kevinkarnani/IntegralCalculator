# IntegralCalculator

## Introduction

This is an Integral Calculator I wrote after learning about the Monte-Carlo Integration method in my AI class.

## Getting Started

### Prerequisites

You must have Python 3.x installed. You will also need `numpy` and `matplotlib` installed via `pip`.

### Functionality

Given the limits of integration, the number of subdividing rectangles, and the function to integrate, it prints the results of different integration techniques. Additionally, it displays a histogram of the frequencies of different yielded results from the Monte-Carlo technique.

For example, given this input:

```
Welcome to the Numerical Integral Calculator!
Initial Limit of Integration:
1
Final Limit of Integration:
3
Number of Rectangles:
1000
Enter the function you want to integrate (pythonic form):
sin(x) + (x ** 2)/exp(x)
```

The output will look like:

```
Monte-Carlo Integral: 2.514052366092158
Left Reimann Sum: 2.5239313103628587
Middle Reimann Sum: 2.5221315015652013
Trapezoid Reimann Sum: 2.5233111635602508
Right Reimann Sum: 2.522691016757641
```
![Histogram](https://i.imgur.com/0ElvsY8.png)

Unfortunately, the reciprocal and inverse reciprocal trig functions are not supported right now.

### Running The Calculator

After downloading the code, run:

```bash
python integralCalculator.py
```

## Author

Kevin Karnani