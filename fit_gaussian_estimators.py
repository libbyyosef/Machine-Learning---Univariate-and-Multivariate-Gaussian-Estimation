from IMLearn.learners import UnivariateGaussian, MultivariateGaussian
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

pio.templates.default = "simple_white"


def test_univariate_gaussian():
    # Question 1 - Draw samples and print fitted model
    mu, sigma = 10, 1
    X = np.random.normal(mu, sigma, 1000)
    uni_gaussian = UnivariateGaussian()
    uni_gaussian_fit = uni_gaussian.fit(X)
    print((np.round(uni_gaussian_fit.mu_, 3), np.round(uni_gaussian_fit.var_,
                                                       3)))

    # Question 2 - Empirically showing sample mean is consistent
    range_ = np.arange(10, 1001, 10)
    samples = [np.abs(mu - uni_gaussian.fit(X[:num]).mu_) for num in \
               range_]
    dataframe_e = pd.DataFrame(samples, index=range_)
    graph_e = px.scatter(dataframe_e)
    graph_e.update_layout(xaxis_title="Number of Sample",
                          yaxis_title="Distance of True and Estimated "
                                      "Expectancy",
                          title="Distance Between the Estimated and "
                                "True Value of Expectation as a Function of "
                                "the Number of Sample")
    graph_e.show()

    # Question 3 - Plotting Empirical PDF of fitted model
    pdfs = uni_gaussian.fit(X).pdf(X)
    dataframe_e3 = pd.DataFrame(pdfs, index=X)
    graph_e3 = px.scatter(dataframe_e3)
    graph_e3.update_layout(xaxis_title="Ordered Sample values",
                           yaxis_title="PDF of Sample",
                           title="PDF of Sample From Q2")
    graph_e3.show()  # gaussian graph shape


def test_multivariate_gaussian():
    # Question 4 - Draw samples and print fitted model
    mean = np.array([0, 0, 4, 0])
    cov = np.array(
        [[1, 0.2, 0, 0.5],
         [0.2, 2, 0, 0],
         [0, 0, 1, 0],
         [0.5, 0, 0, 1]])
    multi_samples = np.random.multivariate_normal(mean, cov, 1000)
    multi_gaussian = MultivariateGaussian()
    multi_gaussian_fit = multi_gaussian.fit(multi_samples)
    print(np.round(multi_gaussian_fit.mu_, 3))
    print(np.round(multi_gaussian_fit.cov_, 3))

    # Question 5 - Likelihood evaluation
    mtx_results = np.zeros((200, 200))
    range_of_vals = np.linspace(-10, 10, 200)
    row = 0
    for f1 in range_of_vals:
        col = 0
        for f3 in range_of_vals:
            mtx_results[row, col] = multi_gaussian.log_likelihood(
                np.array([f1, 0, f3, 0]), cov, multi_samples)
            col += 1
        row += 1

    heat_map = go.Figure(go.Heatmap(x=range_of_vals, y=range_of_vals,
                                    z=mtx_results))
    heat_map.update_layout(title="Log-Likelihood as a Function of f1 and f3",
                           xaxis_title="first coordinate of expectation - f1",
                           yaxis_title="third coordinate of expectation - "
                                       "f3")
    heat_map.show()

    # Question 6 - Maximum likelihood
    print("maximum log likelihood value:",
          np.round(range_of_vals[list(np.unravel_index(mtx_results.argmax(),
                                                       mtx_results.shape))],
                   3))


if __name__ == '__main__':
    np.random.seed(0)
    test_univariate_gaussian()
    test_multivariate_gaussian()
