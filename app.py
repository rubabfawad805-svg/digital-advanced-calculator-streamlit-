import streamlit as st
import math

# --- App Config ---
st.set_page_config(page_title="Advanced Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Digital Advanced Calculator")
st.write("Perform basic and advanced math operations easily!")

# --- Input Fields ---
st.subheader("Enter Expression")
expression = st.text_input("Type your mathematical expression (e.g., 2 + 3 * (4 - 1)):")

# --- Supported Functions ---
functions = {
    "sqrt(x)": "Square Root",
    "log(x)": "Natural Logarithm",
    "log10(x)": "Base 10 Logarithm",
    "sin(x)": "Sine (radians)",
    "cos(x)": "Cosine (radians)",
    "tan(x)": "Tangent (radians)",
    "exp(x)": "Exponential (e^x)",
    "pow(x, y)": "Power (x^y)",
    "factorial(x)": "Factorial"
}

with st.expander("📘 Supported Functions"):
    st.json(functions)

# --- Calculate ---
if st.button("Calculate"):
    try:
        # Restrict available names for safety
        allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        allowed_names["abs"] = abs
        allowed_names["round"] = round

        # Evaluate expression safely
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# --- Clear Button ---
if st.button("Clear"):
    st.experimental_rerun()

# --- Footer ---
st.caption("Created with ❤️ using Streamlit and Python")
