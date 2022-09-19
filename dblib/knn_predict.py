import pandas as pd 
import numpy as np
import math

class KNN:
    def __init__(self, dist_metric='euclidean', k=3):
        if dist_metric == "euclidean":
            self.dist_metric = self.euclidean_distance
        elif dist_metric == 'manhattan':
            self.dist_metric = self.manhattan_distance
        self.k = k
        #self.train_data_X = train_data_X
        #self.train_data_y = train_data_y
        pass

    def fit(self, X, y):
        self.train_data_X = X 
        self.train_data_y = y

    
    def predict(self, test_data_X):
        '''
        predict the y labels for the dataframe test_data_X 
        '''
        # list of y_hats
        y_hat_list = []
        # iterrate through each test row
        for test_i, test_row in test_data_X.iterrows():
            self.closest_points_dist = [] # list of the k smallest distances for a given test_row
            self.closest_points_ys = [] # list of corresponding y's associated with the train row with the smallest distances
            for train_i, train_row in self.train_data_X.iterrows():
                # get distance
                new_dist = self.dist_metric(test_row.values.flatten().tolist(), train_row.values.flatten().tolist())
                # check largest dist and if new dist is less then replace it and its corresponding y
                self.check_largest_dist(new_dist, train_i)
            y_mean = sum(self.closest_points_ys)/len(self.closest_points_ys)
            # determine the label for y_hat
            if y_mean >= .5:
                y_hat_list.append(1)
            else:
                y_hat_list.append(0)
        return y_hat_list
    
    
    def check_largest_dist(self, new_dist, train_index):
        '''
        check to see if the distance between the training point and the test point
        is smaller than the largest distance in the list of k smallest distances
        '''
        if len(self.closest_points_dist) > 0:
            max_in_list = max(self.closest_points_dist) # get largest value in list
        # if list doesnt have k elements already just add new distance and train_y to respective lists
        if len(self.closest_points_dist) < self.k: 
            self.closest_points_dist.append(new_dist)
            self.closest_points_ys.append(self.train_data_y.iloc[train_index].values[0])
        # else check if the newest distance is less than the largest distance in the list of k elements
        # if it is switch them out and switch out their respective y's
        elif new_dist < max_in_list:
            index_of_max = self.closest_points_dist.index(max_in_list)
            self.closest_points_dist.pop(index_of_max) # drop the old largest distance from list
            self.closest_points_dist.append(new_dist) # add the new distance to the list
            self.closest_points_ys.pop(index_of_max) # drop the y value corresponding to the point that was just dropped
            self.closest_points_ys.append(self.train_data_y.iloc[train_index].values[0]) # add the y of the new distance
        

    def euclidean_distance(self, test_row, train_row): # train and test are lists
        dist = 0
        for i in range(len(train_row)):
            dist = dist + (train_row[i] - test_row[i])**2
        dist = (dist)**(1/2)
        return dist


    def manhattan_distance(self, test_row, train_row): # train and test are lists
        dist = 0
        for i in range(len(train_row)):
            dist = dist + abs(train_row[i] - test_row[i])
        return dist