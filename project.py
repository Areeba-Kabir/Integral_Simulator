import streamlit as st
import sympy as sp
import numpy as np
from sympy import symbols, sympify

# Define utility functions
def f(x, equation):
    """Evaluate the equation at a given x."""
    return equation.evalf(subs={symbols('x'): x})

def simpson_one_third(equation, a, b, n):
    """Simpson's 1/3rd Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(i, equation) for i in x]
    
    integral = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    integral *= h / 3
    return integral

def simpson_three_eighth(equation, a, b, n):
    """Simpson's 3/8th Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(i, equation) for i in x]

    integral = y[0] + y[-1] + 3 * sum(y[1:-1:3]) + 3 * sum(y[2:-1:3]) + 2 * sum(y[3:-3:3])
    integral *= 3 * h / 8
    return integral

def trapezoidal(equation, a, b, n):
    """Trapezoidal Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(i, equation) for i in x]

    integral = (y[0] + y[-1]) / 2 + sum(y[1:-1])
    integral *= h
    return integral

def unequal_intervals_trapezoidal(x_vals, y_vals):
    """Trapezoidal Rule for Unequal Intervals."""
    integral = 0
    for i in range(len(x_vals) - 1):
        h = x_vals[i + 1] - x_vals[i]
        integral += h * (y_vals[i] + y_vals[i + 1]) / 2
    return integral

# Streamlit GUI
st.title("Numerical Integration Methods")
st.write("Choose a method to calculate the integral of a function.")

# Option for unequal intervals
unequal_intervals = st.checkbox("Do you have unequal intervals?")

if unequal_intervals:
    st.subheader("Trapezoidal Rule for Unequal Intervals")
    x_vals = st.text_input("Enter x values separated by space (e.g., 0 1 1.5 2):")
    y_vals = st.text_input("Enter corresponding y values separated by space (e.g., 0 1 2.25 4):")

    if st.button("Calculate Integral for Unequal Intervals"):
        try:
            x_vals = list(map(float, x_vals.split()))
            y_vals = list(map(float, y_vals.split()))

            if len(x_vals) != len(y_vals):
                st.error("Error: The number of x and y values must be the same.")
            else:
                result = unequal_intervals_trapezoidal(x_vals, y_vals)
                st.success(f"The integral value is: {result}")
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.subheader("Integration for Equal Intervals")
    equation_str = st.text_input("Enter the mathematical equation (e.g., x**2 + 3*x + 2):")
    h = st.number_input("Enter the step size (h):", min_value=0.0001, step=0.001, format="%.4f")
    x0 = st.number_input("Enter the start value (x0):", step=0.1, format="%.1f")
    xn = st.number_input("Enter the end value (xn):", step=0.1, format="%.1f")

    if st.button("Calculate Integral for Equal Intervals"):
        try:
            x, y = symbols('x y')
            equation = sympify(equation_str)
            n = int((xn - x0) / h)

            if n % 2 == 0:
                if n % 3 == 0:
                    st.info("Using Simpson's 3/8th Rule because the number of intervals (n) is divisible by 3.")
                    result = simpson_three_eighth(equation, x0, xn, n)
                else:
                    st.info("Using Simpson's 1/3rd Rule because the number of intervals (n) is even but not divisible by 3.")
                    result = simpson_one_third(equation, x0, xn, n)
            else:
                st.info("Using Trapezoidal Rule because the number of intervals (n) is odd.")
                result = trapezoidal(equation, x0, xn, n)

            st.success(f"The integral value is: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

st.write("You can reset the input fields to perform the calculations again.")
