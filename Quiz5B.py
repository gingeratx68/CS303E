# CS 303E Quiz 5B
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Resolution Reduction
def resolutionReduction(matrix, row, col):
    count=0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            row+=1
            col+=1
            count+=row
            if (row==[row+2]) and (col==[col+2]):
                return count/9
            #else:
                #continue 
                
       
            
        



# Problem 2: First Uppercase Locations
def firstUppercaseLocations(strings):
    dicts={}
    for i in range(0, len(strings)):
        if ([i].istitle()):
            dicts=dicts.index(i)
        return dicts
            
            
            



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    grid = [[0.814, 0.573, 0.548, 0.539, 0.85, 0.695, 0.502, 0.75, 0.118], [0.103, 0.166, 0.857, 0.945, 0.592, 0.948, 0.843, 0.726, 0.105], [0.863, 0.925, 0.065, 0.1, 0.315, 0.811, 0.607, 0.537, 0.966], [0.565, 0.345, 0.423, 0.937, 0.027, 0.679, 0.855, 0.173, 0.655], [0.308, 0.701, 0.479, 0.535, 0.9, 0.907, 0.14, 0.702, 0.524], [0.977, 0.146, 0.943, 0.351, 0.195, 0.977, 0.617, 0.551, 0.3], [0.258, 0.794, 0.863, 0.014, 0.299, 0.304, 0.355, 0.852, 0.826], [0.45, 0.466, 0.705, 0.005, 0.877, 0.687, 0.394, 0.17, 0.657], [0.608, 0.486, 0.256, 0.934, 0.239, 0.124, 0.524, 0.763, 0.621]]
    print(resolutionReduction(grid, 1, 1))
    # print(resolutionReduction(grid, 3, 3))
    # grid2 = [[.5, .6, .7], [.8, .9, .1], [.2, .3, .4]]
    # print(resolutionReduction(grid2, 1, 1))

    #print(firstUppercaseLocations({"I", "lovE", "TWICE", "!"}))
    # print(firstUppercaseLocations({"Who's", "yoUr", "biaS", "iN", "TWICE", "?"}))
    # print(firstUppercaseLocations(set()))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
