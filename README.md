# Univariate-and-Multivariate-Gaussian-Estimation

This repository contains Python implementations for estimating univariate and multivariate Gaussian distributions, as part of an exercise for the Introduction to Machine Learning (IML) course. These estimators are based on the principles of estimation theory and mathematical foundations covered in the course.

**Univariate Gaussian Estimation**

The UnivariateGaussian class in learners.gaussian_estimators.py provides functionality to estimate the parameters of a univariate Gaussian distribution, namely the mean (expectation) and variance. The class offers methods to fit the model to given data and calculate the probability density function (PDF) for observations under the fitted Gaussian model.

**Usage**

**1. Drawing Samples and Fitting the Model**

To demonstrate the fitting process, the test_univariate_gaussian() function in the main script (test.py) draws 1000 samples from a univariate Gaussian distribution with mean (mu) 10 and variance (sigma^2) 1. It then fits a univariate Gaussian model to these samples and prints the estimated expectation and variance.

**2. Plotting Absolute Distance of Estimated Expectation**

The script also plots the absolute distance between the estimated and true values of the expectation as a function of the sample size. This visualization helps understand how the estimation accuracy improves with increasing sample size.

**3. Plotting Empirical PDF of Fitted Model**

Additionally, the script computes the PDF of the drawn samples using the fitted model and plots the empirical PDF function under the fitted model. This scatter plot visualizes the distribution of the samples and their PDF values under the estimated Gaussian model.

**Multivariate Gaussian Estimation**

The MultivariateGaussian class in learners.gaussian_estimators.py extends the functionality to estimate parameters of a multivariate Gaussian distribution, including the mean vector (expectation) and covariance matrix. Similar to the univariate case, it provides methods to fit the model to given data and calculate the PDF for observations under the fitted multivariate Gaussian model.

**Usage**

**1. Drawing Samples and Fitting the Model**

The test_multivariate_gaussian() function in the main script draws 1000 samples from a multivariate Gaussian distribution with specified mean vector and covariance matrix. It then fits a multivariate Gaussian model to these samples and prints the estimated expectation vector and covariance matrix.

**2. Calculating Log-Likelihood for Different Parameters**

The script calculates the log-likelihood of the data under various specified Gaussian models with different parameters. It generates a heatmap showing the log-likelihood as a function of the parameters, providing insights into the likelihood of different parameter combinations.

**3. Identifying Maximum Likelihood Model**

Lastly, the script identifies the model (pair of parameter values) that achieves the maximum log-likelihood value among all tested values.


![q1_result](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/8e5cef44-53b0-4096-89b5-ce3db4babf34)


![q2_graph](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/68212ce4-438a-4dd0-817b-f822aab6e8e3)


![q3_graph](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/ce6d5b3f-f536-49ce-8671-9707aba28dcf)


![q4_cov](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/e3bb08ec-2721-42d8-bf64-4eeb4684e8dc)


![q4_mu](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/5adeb23f-736e-4551-a84c-a0bb53c74c9f)


![q5_graph](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/9a91a459-297d-4dff-bac7-f97e8ac5ad91)


![q6_max_log_likelihood](https://github.com/libbyyosef/Machine-Learning---Univariate-and-Multivariate-Gaussian-Estimation/assets/36642026/057ea4c5-b609-47e6-90ff-a7539625b462)


**Instructions**

To use these estimators:

1. Ensure you have Python installed along with necessary dependencies such as NumPy, Plotly, and Pandas.
2. Clone this repository to your local machine.
3. Execute the test.py script to run the provided test functions for both univariate and multivariate Gaussian estimators.
