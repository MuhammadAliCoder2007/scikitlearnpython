%pip install --upgrade scikit-learn==0.23.0
from sklearn.datasets import load_boston
X,y = load_boston(return_X_y=True)
from sklearn.neigbors import KNeighborsRegressor
mod = KNeighborsRegressor()
mod.fit(X,y)