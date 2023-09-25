# Laptop-Price-Prediction

This project aims to predict the prices of laptops using machine learning techniques. Given various features of a laptop, such as screen size, RAM, storage type, and more, a predictive model to estimate the price of a laptop was developed.

## Table of Contents

- [Project Overview](#project-overview)
- [Data](#data)
- [Methodology](#methodology)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Predicting laptop prices can be valuable for both consumers and retailers. Consumers can make informed decisions about which laptop to purchase based on their budget and requirements, while retailers can optimize pricing strategies.

In this project, we utilize machine learning models to predict laptop prices based on various features and specifications. A dataset containing information about laptops, including their screen size, RAM, storage type, company, and more was used.

## Data

The dataset used for this project contains the following columns:

- `Inches`: Screen size in inches
- `Ram (GB)`: RAM capacity in gigabytes
- `SSD`: Solid State Drive storage in gigabytes
- `HDD`: Hard Disk Drive storage in gigabytes
- `Flash_Storage`: Flash storage capacity in gigabytes
- `TouchScreen`: Indicates whether the laptop has a touchscreen (1 for yes, 0 for no)
- `Company`: Laptop manufacturer (e.g., HP, Dell, Acer)
- `TypeName`: Type or category of the laptop (e.g., Gaming, Ultrabook)
- `CPU Brand`: Processor brand (e.g., Intel Core i5, AMD)
- `GPU Brand`: Graphics card brand (e.g., Nvidia, AMD)

## Methodology

A machine learning pipeline for this project, including data preprocessing, model selection, hyperparameter tuning, and evaluation. The following models have been considered:

- Random Forest
- XGBoost
- Gradient Boosting
- Decision Tree
- K-Nearest Neighbors (KNN)

Hyperparameters for each model are tuned using Grid Search Cross-Validation to optimize their performance.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Set up your Python environment with the required libraries (see `requirements.txt`).
3. Explore the dataset (`laptop_price.csv`) and the Jupyter Notebook (`laptop_price_prediction.ipynb`) for detailed analysis and model development.

## Usage

You can use the trained machine learning models to predict laptop prices based on the laptop's features. You can also integrate these models into your applications or services for real-time price predictions.

To make a laptop price prediction using the trained models, follow the example in the `util.py` file.

```python
# Example usage
predicted_price = predict_laptop_price(15.6, 8, 256, 1000, 0, 1, 'Company_HP', 'TypeName_Gaming', 'CPU Brand_Intel Core i5', 'GPU Brand_Nvidia')
print(f"Predicted Price: €{predicted_price:.2f}")
