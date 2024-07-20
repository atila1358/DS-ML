import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

data  = pd.DataFrame({'ساعات مطالعه' : [2,3,5,4,6,7,2,1,4,3],
                      'ميانگين نمرات': [15,18,24,21,26,14,28,12,20,17]})

X = data['ساعات مطالعه'].to_numpy()[:,np.newaxis]
y = data['ميانگين نمرات'].to_numpy()

model = LinearRegression()
model.fit(X,y)


new_x = np.array([3.5])[:,np.newaxis]
predicted_y = model.predict(new_x)

print('Predict = ', predicted_y)

                     
                     
                    
