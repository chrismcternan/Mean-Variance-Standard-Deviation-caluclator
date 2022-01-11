import numpy as np

def calculate(my_list):
  # # set up 3 x 3 matrix for stats calculations
    if len(my_list) < 9:
      raise ValueError("List must contain nine numbers.")
    my_arr = np.asarray(my_list)
    my_arr = my_arr[0:9].reshape(3,3)
  
    # calculate mean, var, st. dev, max, min, and sum...
    # initialize calculations dictionary
    calculations = {}
    ops = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    for operation in ops:
      calculations[operation] = list()

    # mean
    calculations['mean'].append(my_arr.mean(axis = 0).tolist())
    calculations['mean'].append(my_arr.mean(axis = 1).tolist())
    calculations['mean'].append(my_arr.mean().tolist())
    # variance
    calculations['variance'].append(my_arr.var(axis = 0).tolist())
    calculations['variance'].append(my_arr.var(axis = 1).tolist())
    calculations['variance'].append(my_arr.var().tolist())
    # standard deviation
    calculations['standard deviation'].append(my_arr.std(axis = 0).tolist())
    calculations['standard deviation'].append(my_arr.std(axis = 1).tolist())
    calculations['standard deviation'].append(my_arr.std().tolist())
    # max
    calculations['max'].append(my_arr.max(axis = 0).tolist())
    calculations['max'].append(my_arr.max(axis = 1).tolist())
    calculations['max'].append(my_arr.max().tolist())
    # min
    calculations['min'].append(my_arr.min(axis = 0).tolist())
    calculations['min'].append(my_arr.min(axis = 1).tolist())
    calculations['min'].append(my_arr.min().tolist())
    # sum
    calculations['sum'].append(my_arr.sum(axis = 0).tolist())
    calculations['sum'].append(my_arr.sum(axis = 1).tolist())
    calculations['sum'].append(my_arr.sum().tolist())

    # print (calculations)
    return calculations
  

if __name__ == '__main__':
  my_list = [2,6,2,8,4,0,1,5,7]
  print (calculate(my_list))
  
