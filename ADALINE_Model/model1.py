import numpy as np
orange = np.array([1,0])
apple = np.array([0,1])
apple_value = 1
orange_value =- 1
weight_1=0.3
weight_2=0.2
coef=0.5
threshold=0.1
function1=0
resultA=-1
resultO=1
weights=np.array([weight_1,weight_2])
for i in range(0,5):

    if resultO!=orange_value:
        function1=weights*(np.transpose(orange))+threshold
        if(function1[1]>0):
            resultO=1

        else:
            resultO=-1
        if resultO !=orange_value:
            E=orange_value-resultO
            E=coef*E
            weights=weights+(E*orange)
            threshold=threshold+(E)


        if (resultA != apple_value):
            function1 = weights * (np.transpose(apple)) + threshold
            if function1[1] > 0:
                resultA = 1
            else:
                resultA = -1
            if(resultA !=apple_value):
                E=apple_value-resultA
                E=coef*E
                weights=weights+(E*apple)
                threshold=threshold+(E)
        print(weights)
        if(resultO==orange_value & resultA==apple_value):
            break









