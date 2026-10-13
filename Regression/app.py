import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i]*y[i] for i in range(n))
    sum_x_square = sum(xi**2 for xi in x)

    denominator = (n*sum_x_square - sum_x**2)
    if denominator == 0:
        return 0, 0

    slope = (n*sum_xy - sum_x*sum_y) / denominator
    intercept = (sum_y - slope*sum_x) / n
    return slope, intercept

st.title("Linear Regression App")
st.write("Enter your X and Y data points below (comma-separated numbers).")

x_input = st.text_input("X Values", "1, 2, 3, 4, 5")
y_input = st.text_input("Y Values", "2, 4, 5, 4, 5")

try:
    x = [float(i.strip()) for i in x_input.split(",") if i.strip()]
    y = [float(i.strip()) for i in y_input.split(",") if i.strip()]

    if len(x) != len(y):
        st.error("Error: X and Y must have the same number of elements.")
    elif len(x) < 2:
        st.warning("Please enter at least 2 data points.")
    else:
        slope, intercept = linear_regression(x, y)
        
        st.subheader("Results")
        st.write(f"**Slope (b1):** {slope:.4f}")
        st.write(f"**Intercept (b0):** {intercept:.4f}")
        st.write(f"**Equation:** Y = {slope:.4f} * X + {intercept:.4f}")

        # Plotting
        fig, ax = plt.subplots()
        x_arr = np.array(x)
        y_arr = np.array(y)
        ax.scatter(x_arr, y_arr, color='red', label='Data points')
        
        x_vals = np.linspace(min(x_arr), max(x_arr), 100)
        y_vals = slope * x_vals + intercept
        ax.plot(x_vals, y_vals, color='blue', label='Regression Line')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.legend()
        
        st.pyplot(fig)
except ValueError:
    st.error("Please ensure all inputs are valid numbers separated by commas.")