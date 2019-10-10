
# coding: utf-8

# In[21]:


import numpy as np
from numpy import genfromtxt


# In[22]:


train_data = genfromtxt('./data/train1.csv', delimiter=',')
train_X, train_Y = train_data[:,:2], train_data[:,2:]


# In[23]:


mean, std = train_X.mean(axis=0, keepdims=True), train_X.std(axis=0, keepdims=True)
mean = mean - mean
std = std/std
normalized_X = (train_X - mean)/std
normalized_X = np.expand_dims(normalized_X, axis=2)
train_Y = np.expand_dims(train_Y, axis=2)

orig_normalized_X = np.copy(normalized_X)
orig_train_Y = np.copy(train_Y)
permutation = np.random.permutation(len(train_X))
normalized_X = normalized_X[permutation]
train_Y = train_Y[permutation]


# In[24]:


class Model():
    def __init__(self, hidden_units=10):
        self.input_units, self.hidden_units, self.output_units = 2, hidden_units, 2 
        self.W_1 = np.random.normal(0, 1,(self.hidden_units, 2))
        self.b_1 = np.random.normal(0, 1, (1,1))
        self.W_2 = np.random.normal(0, 1,(self.output_units, self.hidden_units))
        self.b_2 = np.random.normal(0, 1, (1,1))
    
    def forward(self, j):
        self.f_1 = np.dot(self.W_1, self.X_train[j]) + self.b_1
        self.a_1 = 1/(1+np.exp(-self.f_1))
        self.f_2 = np.dot(self.W_2, self.a_1) + self.b_2
        self.a_2 = 1/(1+np.exp(-self.f_2))
        return self.a_2
    
    def calculate_gradients(self, error, lr, j):
        grad_se = -error
        grad_a_2 = np.multiply(grad_se, np.multiply(self.a_2, 1-self.a_2)) 
        grad_b_2 = grad_a_2.sum(axis=0, keepdims=True) 
        grad_W_2 = np.dot(grad_a_2, self.a_1.T)
        grad_a_1 = np.dot(self.W_2.T, grad_a_2)
        grad_f_1 = np.multiply(grad_a_1, np.multiply(self.a_1, 1-self.a_1))  
        grad_b_1 = grad_f_1.sum(axis=0, keepdims=True)
        grad_W_1 = (np.dot(self.X_train[j], grad_f_1.T)).T
        
        self.W_1 -= lr*grad_W_1 
        self.b_1 -= lr*grad_b_1 
        
        self.W_2 -= lr*grad_W_2 
        self.b_2 -= lr*grad_b_2 
        
    
    def train(self, X_train, Y_train, n_epochs=50, lr=0.1):
        self.X_train = X_train
        self.Y_train = Y_train
        self.n_epochs = n_epochs
        self.lr = lr
        
        for i in range(n_epochs):
            e_loss = 0
            e_acc = 0
            for j in range(len(X_train)):
                pred = self.forward(j)
                error = Y_train[j] - pred
                self.calculate_gradients(error, lr, j)
                
                squared_loss = np.power(Y_train[j] - pred,2).sum()/2
                e_loss += squared_loss
                e_acc += (np.argmax(Y_train[j]) == np.argmax(pred)) and pred[np.argmax(pred)] >= 0.5

        print('Loss, acc:', e_loss, (e_acc/len(X_train))*100)
            
    def predict(self, X, Y):
        e_loss = 0
        e_acc = 0
        for j in range(len(X)):
            f_1 = np.dot(self.W_1, X[j]) + self.b_1
            a_1 = 1/(1+np.exp(-f_1))
            f_2 = np.dot(self.W_2, a_1) + self.b_2
            a_2 = 1/(1+np.exp(-f_2))
            pred = a_2
            error = Y[j] - pred
            squared_loss = np.power(Y[j] - pred,2).sum()/2
            e_loss += squared_loss
            e_acc += (np.argmax(Y[j]) == np.argmax(pred)) and pred[np.argmax(pred)] >= 0.5

        print('Loss, acc:', e_loss, (e_acc/len(X))*100)
        
def report_results_on_test_set():
    for i in range(1,4):
        data = genfromtxt('./data/test'+str(i)+'.csv', delimiter=',')
        X, Y = data[:,:2], data[:,2:]
        X = (X - mean)/std
        X = np.expand_dims(X, axis=2)
        Y = np.expand_dims(Y, axis=2)
        model.predict(X, Y)        


# In[28]:


model = Model(hidden_units=10)
print('Training set results:')
model.train(normalized_X, train_Y, n_epochs=10, lr=0.1)
print(' ')
print('Test set results:')
report_results_on_test_set()


# In[40]:


'''
import matplotlib.pyplot as plt
import numpy as np
 
# Data
df={'x': np.array([0.001,0.01,0.1,1]), 'y': np.array([44,97, 98, 98])}
 
# multiple line plot
plt.plot( 'x', 'y', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
#plt.legend()
plt.suptitle('Effect of learning rate on training set accuracy', fontsize=12)
plt.xlabel('learning rate', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
#plt.xticks(np.arange(0, 51, 1.0))
'''

