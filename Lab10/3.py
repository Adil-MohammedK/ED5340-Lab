import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os

if os.path.exists("Lab10"):
    print("Exists")
    os.chdir("Lab10")
# Define logistic regression model:
class LogisticRegression(object):
    def __init__(self, x, y, lr=0.01, method="entropy"):
        self.lr = lr
        self.x_train = x
        self.y_train = y
        self.method = method
        print("method is: ", self.method)
        n = x.shape[1]  # determine the number of independent variables
        self.w = np.ones((1, n)) * (0)  # initialize weight matrix and set weights to zero
        self.b = 0.5  # set starting value for b to 0.5
        fig, ax = plt.subplots()
        plt.scatter(self.x_train[:, 0], self.x_train[:, 1])
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.show()

    def predict(self, x):  # returns prediction
        z = x @ self.w.T + self.b  # @: matrix multiplication
        p = self.sigmoid(z)  # logistic sigmoid function
        return p

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def pred_3d_curve(self, X, w, b):  # predicts y-values for regression curve spanned by n0s and n1s (see below)
        p = self.sigmoid(X @ w.T + b)
        return p

    def cost(self, x, y):  # cost function
        z = x @ self.w.T + self.b
        p = self.sigmoid(z)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))  # Cross-entropy cost function

    def CrossEntropy_cost(self, x, y, w, b):
        p = self.sigmoid(x @ w.T + b)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

    def MSE_cost(self, x, y, w, b):  # define MSE-cost function
        pred = self.sigmoid(x @ w.T + b)
        # Calculate mean squared error between predicted and actual y-values:
        mse = np.mean((y - pred) ** 2, axis=0)
        return mse

    def step(self, x, y):
        z = x @ self.w.T + self.b
        p = self.sigmoid(z)

        # Partial derivatives:
        dw = np.mean((p - y) * x, axis=0)  # dJ/dw
        db = np.mean(p - y)  # dJ/db
        self.w = self.w - dw * self.lr  # update w
        self.b = self.b - db * self.lr  # update b

    def fit(self, x, y, numberOfEpochs=100000):
        # Create arrays to store weights, biases, costs, predicted y-values for plots..
        # ... and predicted y-values for connection lines in:
        self.AllWeights = np.zeros((numberOfEpochs, x.shape[1]))
        self.AllBiases = np.zeros((numberOfEpochs, x.shape[1]))
        self.AllCosts = np.zeros((numberOfEpochs, x.shape[1]))
        self.All_cl = np.zeros((numberOfEpochs, len(x)))  # cl: # predicted y-values for connection lines
        self.iterations = numberOfEpochs

        for step in range(numberOfEpochs):
            # for each step of gradient descent assign new parameter value to respective array element:
            self.AllWeights[step] = self.w
            self.AllBiases[step] = self.b
            if self.method == "entropy":
                self.AllCosts[step] = self.cost(x, y)
            elif self.method == "msd":
                self.AllCosts[step] = self.MSE_cost(x, y, self.w, self.b)
            self.All_cl[step] = (self.predict(x)).T.flatten()
            self.step(x, y)  # update parameter values

    def fitDataPlot(self):
        fig = plt.figure(figsize=(18, 7))
        ax = fig.add_subplot(1, 2, 1)
        ax.scatter(self.x_train[:, 0], self.x_train[:, 1])
        x = np.arange(0, 9, 1)
        y = (-self.b - self.w[0][0] * x) / self.w[0][1]
        ax.plot(x, y, "r-")
        ax.set_xlabel("x0")
        ax.set_ylabel("x1")
        ax.set_title("Logistic regression fit", fontsize=20)  # set title
        plt.show()

    def plotCostCurve(self):
        w0 = self.AllWeights.T[0]
        w1 = self.AllWeights.T[1]
        cl = self.All_cl
        c = self.AllCosts
        b_fixed = self.b

        xs = np.array([np.linspace(-150, 200)])
        n0s = np.linspace(-13, 13, 100)
        n1s = np.linspace(-13, 13, 100)
        N1, N2 = np.meshgrid(n0s, n1s)  # create meshgrid for regression curve

        if self.method == "entropy":
            m0s = np.linspace(-1, 1, 100)
            m1s = np.linspace(-1, 1, 100)
        elif self.method == "msd":
            m0s = np.linspace(-5, 5, 100)
            m1s = np.linspace(-5, 5, 100)
        M1, M2 = np.meshgrid(m0s, m1s)  # create meshgrid for surface plot/contour plot
        if self.method == "entropy":
            zs_1 = np.array(
                [
                    self.CrossEntropy_cost(self.x_train, self.y_train, np.array([[wp0, wp1]]), np.array([[b_fixed]]))
                    for wp0, wp1 in zip(np.ravel(M1), np.ravel(M2))
                ]
            )
        elif self.method == "msd":
            zs_1 = np.array(
                [
                    self.MSE_cost(self.x_train, self.y_train, np.array([[wp0, wp1]]), np.array([[b_fixed]]))
                    for wp0, wp1 in zip(np.ravel(M1), np.ravel(M2))
                ]
            )
        Z_1 = zs_1.reshape(M1.shape)  # z-values of surface plot/contour plot

        # Create plot:
        fig = plt.figure(figsize=(8, 10))  # create figure

        # Customize subplots:
        label_font_size = 25  # size of label fonts
        tick_label_size = 17  # size of tick labels
        ax0 = fig.add_subplot(2, 1, 1, projection="3d")
        ax0.set_title("Logistic regression curve (3D)", fontsize=20)  # set title
        ax0.view_init(elev=38.0, azim=-25)
        ax0.set_xlabel(r"$x_0$", fontsize=label_font_size, labelpad=8)
        ax0.set_ylabel(r"$x_1$", fontsize=label_font_size, labelpad=7)
        ax0.set_zlabel("y", fontsize=label_font_size, labelpad=6)
        ax0.tick_params(axis="both", which="major", labelsize=tick_label_size)
        ax0.tick_params(axis="x", pad=3, which="major", labelsize=tick_label_size)
        ax0.tick_params(axis="y", pad=-2, which="major", labelsize=tick_label_size)
        ax1 = fig.add_subplot(2, 1, 2, projection="3d")
        ax1.view_init(elev=38.0, azim=-25)
        ax1.view_init(elev=38.0, azim=140)
        ax1.tick_params(axis="both", which="major", labelsize=tick_label_size)
        ax1.tick_params(axis="x", pad=3, which="major", labelsize=tick_label_size)
        ax1.tick_params(axis="y", pad=-2, which="major", labelsize=tick_label_size)
        ax1.set_xlabel(r"$w_0$", fontsize=label_font_size, labelpad=14)
        ax1.set_ylabel(r"$w_1$", fontsize=label_font_size, labelpad=14)
        ax1.set_zlabel("costs", fontsize=label_font_size, labelpad=3)
        ax1.set_xticks([0.5, 0.3, 0.1, -0.1])
        ax1.set_xticklabels(["0.5", "0.3", "0.1", "-0.1"], fontsize=tick_label_size)
        ax1.set_yticks([0.6, 0.4, 0.2, 0])
        ax1.set_yticklabels(["0.6", "0.4", "0.2", "0"], fontsize=tick_label_size)
        ax1.set_zticks([0.6, 0.7, 0.8, 0.9, 1.0])
        ax1.set_zticklabels(["0.6", "0.7", "0.8", "0.9", "1.0"], fontsize=tick_label_size)

        # In[5]

        w = model.w
        zs_0 = np.array(
            [
                self.pred_3d_curve(np.array([[wp0, wp1]]), w, np.array([[b_fixed]]))
                for wp0, wp1 in zip(np.ravel(N1), np.ravel(N2))
            ]
        )
        Z_0 = zs_0.reshape(N1.shape)  # z-values of regression curve
        ax0.plot_surface(N1, N2, Z_0, rstride=1, cstride=1, alpha=0.4, cmap=cm.coolwarm, antialiased=False)

        # Scatter plot of training data:
        ax0.scatter(self.x_train.T[0], self.x_train.T[1], self.y_train.flatten(), marker="x", s=28 * 2, color="black")

        # Surface plot of costs:
        ax1.plot_surface(M1, M2, Z_1, rstride=1, cstride=1, alpha=0.73, cmap=cm.coolwarm)

        # Customize legends:
        plt.show()

    def plotCostContour(self, levels=[0.2, 0.3, 0.6, 0.7, 0.8, 0.9, 1]):

        w0 = model.AllWeights.T[0]
        w1 = self.AllWeights.T[1]
        cl = self.All_cl
        c = self.AllCosts
        b_fixed = self.b

        fig = plt.figure(figsize=(10, 10))  # create figure
        ax1 = fig.add_subplot(111)
        # set levels for contour lines
        if self.method == "msd":
            m0s = np.linspace(-50, 50, 100)
            m1s = np.linspace(-50, 50, 100)
        elif self.method == "entropy":
            m0s = np.linspace(-5, 5, 100)
            m1s = np.linspace(-5, 5, 100)
        M1, M2 = np.meshgrid(m0s, m1s)  # create meshgrid for surface plot/contour plot
        if self.method == "entropy":
            zs_1 = np.array(
                [
                    self.CrossEntropy_cost(self.x_train, self.y_train, np.array([[wp0, wp1]]), np.array([[b_fixed]]))
                    for wp0, wp1 in zip(np.ravel(M1), np.ravel(M2))
                ]
            )
        elif self.method == "msd":
            zs_1 = np.array(
                [
                    self.MSE_cost(self.x_train, self.y_train, np.array([[wp0, wp1]]), np.array([[b_fixed]]))
                    for wp0, wp1 in zip(np.ravel(M1), np.ravel(M2))
                ]
            )
        Z_1 = zs_1.reshape(M1.shape)  # z-values of surface plot/contour plot

        # Customize subplots:
        label_font_size = 25  # size of label fonts
        tick_label_size = 17  # size of tick labels
        fig.suptitle("Logistic contour curve", fontsize=20, y=0.95)

        ax1.tick_params(axis="both", which="major", labelsize=tick_label_size)
        ax1.set_xlabel(r"$w_0$", fontdict=None, labelpad=2, fontsize=label_font_size)
        ax1.set_ylabel(r"$w_1$", fontdict=None, labelpad=-2, fontsize=label_font_size)

        # Contour plot of costs:
        cp = ax1.contour(M1, M2, Z_1, levels, colors="black", linestyles="dashed", linewidths=1)  # contour plot
        plt.clabel(cp, inline=1, fmt="%1.1f", fontsize=15)  # add labels to contour lines
        cp = plt.contourf(M1, M2, Z_1, alpha=0.85, cmap=cm.coolwarm)  # filled contour plot

        for i in range(0, len(w0), 100):
            # Plot trajectory of gradient descent:
            plt.scatter(w0[i], w1[i], marker="o", s=2 ** 2, color="black")
            plt.plot(w0[0:i], w1[0:i], linestyle="dashed", color="black")

        plt.show()

    def plotCostIter(self):
        c = self.AllCosts
        x = np.arange(0, self.iterations, 1)
        plt.plot(x, c)
        plt.xlabel("Iterations")
        plt.ylabel("Cost")
        plt.title("Cost vs Iterations")
        plt.show()


# In[2]
my_data = pd.read_csv("Logistic_regression_ls.csv")
# Split into X and y
x_train = np.ones((len(my_data), 2))
x_train[:, 0] = my_data.x1
x_train[:, 1] = my_data.x2
# y_train = my_data.label

y_train = my_data.iloc[:, 2:3].values


# In[3]
xs = np.array([np.linspace(-150, 200)])  # x-values later used for regression curve plot

# Fit model to training data:
model = LogisticRegression(x_train, y_train, lr=0.01)  # set up model and define learning rate
model.fit(x_train, y_train, numberOfEpochs=50000)  # set number of epochs

# Print results:
print("Final weight: ")
print(model.w)
# print("Final bias: " + model.b)
print("Final costs: " + str(model.cost(x_train, y_train)))

model.fitDataPlot()
model.plotCostCurve()
model.plotCostContour()
model.plotCostIter()

# In[4]

model2 = LogisticRegression(x_train, y_train, 0.01, method="msd")
model2.fit(x_train, y_train, 10000)
# Print results:
print("Final MSD weight: ")
print(model2.w)
# print("Final bias: " + model.b)
print("Final MSD costs: " + str(model2.cost(x_train, y_train)))

model2.fitDataPlot()
model2.plotCostCurve()
model2.plotCostContour(levels=[0.2, 0.3, 0.6, 0.7, 0.8, 1, 1.5, 2, 3, 4])
model2.plotCostIter()
