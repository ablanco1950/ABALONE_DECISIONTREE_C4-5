ABALONE_DECISIONTREE_C4-5: A procedure is attached that uses the Abalone file (https://archive.ics.uci.edu/ml/datasets/abalone) as test and training .

 After evaluating the entropy of each field, a tree has been built with the nodes corresponding to fields 0, 7 and 4 and branch values in each node: 1 for the root node corresponding to field 0, 29 for the next node in the hierarchy corresponding to field 7, and 33 in the last node corresponding to field 4.

The values of each field have been associated with indices, which can encompass several real values. the values of these indices are those that have been considered afterr the calculation of entropies and for making a branching of values at each node.

A hit rate of around 58% is obtained, that is, in the low range of the existing procedures to treat this multiclass file, which are detailed in the documentation to download from https://archive.ics.uci.edu/ml/datasets/abalone

The depth of the tree has been increased without obtaining significant improvements. Nor has it been significantly improved by applying adaboost.
 

Resources: Spyder 4

On the c: drive there should be the abalone-1.data file downloaded from https://archive.ics.uci.edu/ml/datasets/abalone

Functioning:

From Spyder run:

AbaloneDecisionTree_C4-5-ThreeLevels.py

The screen indicates the number of hits and failures and in the file C:\AbaloneCorrected.txt the records of the test file (records 3133 to 4177 of abalone-1.data) with an indication of whether their predicted class values ??coincide with the reals, the predicted class value and the order number of the record in abalone-1.data

The following programs are also attached: AbaloneDecisionTree_ID3.py and AbaloneDecisionTree_C4-5_parameters.py that have served to calculate the necessary parameters to build the tree.


Cite this software as:

** Alfonso Blanco García ** ABALONE_DECISIONTREE_C4-5

References:

https://archive.ics.uci.edu/ml/datasets/abalone
