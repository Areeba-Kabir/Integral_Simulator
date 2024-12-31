import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify

# Define utility functions
def f(x, y, equation_func):
    """Evaluate the numerical equation at given x and y."""
    return equation_func(x, y)

def simpson_one_third(equation_func, a, b, n, y_value):
    """Simpson's 1/3rd Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(i, y_value, equation_func) for i in x]
    integral = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2])
    integral *= h / 3
    return integral

def simpson_three_eighth(equation_func, a, b, n, y_value):
    """Simpson's 3/8th Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(i, y_value, equation_func) for i in x]
    integral = y[0] + y[-1] + 3 * sum(y[1:-1:3]) + 3 * sum(y[2:-1:3]) + 2 * sum(y[3:-3:3])
    integral *= 3 * h / 8
    return integral

def trapezoidal(equation_func, a, b, n, y_value):
    """Trapezoidal Rule."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(i, y_value, equation_func) for i in x]
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
st.title("Numerical Integration Methods with Plotting")
st.write("Choose a method to calculate the integral of a function and visualize the process.")

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

                # Plot points
                fig, ax = plt.subplots()
                ax.plot(x_vals, y_vals, marker='o', label="Provided Points")
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.set_title("Scatter Plot of Provided Points")
                ax.legend()
                st.pyplot(fig)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.subheader("Integration for Equal Intervals")
    equation_str = st.text_input("Enter the mathematical equation (e.g., sin(x) + cos(y)):")
    h = st.number_input("Enter the step size (h):", min_value=0.0001, step=0.001, format="%.4f")
    x0 = st.number_input("Enter the start value (x0):", step=0.1, format="%.1f")
    xn = st.number_input("Enter the end value (xn):", step=0.1, format="%.1f")
    y_value = st.number_input("Enter the constant y value:", step=0.1, format="%.1f")

    if st.button("Calculate and Plot Integral"):
        try:
            x, y = symbols('x y')  # Define both symbols x and y
            equation = sympify(equation_str)  # Parse the equation string into a sympy expression
            equation_func = sp.lambdify((x, y), equation, modules=['numpy'])  # Convert to numerical function
            n = int((xn - x0) / h)

            if n % 2 == 0:
                if n % 3 == 0:
                    st.info("Using Simpson's 3/8th Rule.")
                    result = simpson_three_eighth(equation_func, x0, xn, n, y_value)
                else:
                    st.info("Using Simpson's 1/3rd Rule.")
                    result = simpson_one_third(equation_func, x0, xn, n, y_value)
            else:
                st.info("Using Trapezoidal Rule.")
                result = trapezoidal(equation_func, x0, xn, n, y_value)

            st.success(f"The integral value is: {result}")

            # Plotting
            x_vals = np.linspace(x0, xn, 100)
            y_vals = [f(i, y_value, equation_func) for i in x_vals]

            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label=str(equation))
            ax.fill_between(x_vals, y_vals, alpha=0.3, label="Integration Area")
            ax.set_xlabel("x")
            ax.set_ylabel("f(x, y)")
            ax.set_title("Plot of the Function and Integration Area")
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error: {e}")

st.write("You can reset the input fields to perform the calculations again.")
