# Integral Simulator
Integral Simulator is a Streamlit-based application that demonstrates various numerical integration methods, including Simpson's 1/3rd Rule, Simpson's 3/8th Rule, and the Trapezoidal Rule. The app provides a user-friendly interface for calculating integrals and visualizing the results with plots.

## Features
- Support for Unequal Intervals: Calculate integrals using the Trapezoidal Rule for data with unequal intervals.
- Integration for Equal Intervals: Choose between Simpson's Rules and the Trapezoidal Rule based on input.
- Visualization: Plot the function and highlight the integration area for better understanding.

## Getting Started
Follow the steps below to set up and run the project on your local machine.

### Prerequisites
Ensure you have the following installed on your system:

- Python 3.8 or later
- pip (Python package manager)

### Installation and Setup

1. Clone repository:
```

git clone https://github.com/Areeba-Kabir/Integral_Simulator.git

cd Integral_Simulator/

```
2. Create a Virtual Environment:
```

python -m venv .env

```
3. Activate the Virtual Environment:
- On Windows:
```

.env\Scripts\activate

```
- On macOS/Linux:

```

source .env/bin/activate

```
4. Install Dependencies:
```

pip install -r requirements.txt

```

## Running the Application
1. Run streamlit app

```
streamlit run project.py

```

or 

```

python -m streamlit run project.py

```

## Usage
- Enter the mathematical equation, range, step size, and other parameters in the app interface.
- Choose the integration method based on intervals.
- View results and visualize the integration area.