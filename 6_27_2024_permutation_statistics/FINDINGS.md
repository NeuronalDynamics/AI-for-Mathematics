# Summary of findings.

## Statistic 1
**Accuracy achieved: 100%**

**Description of model weights:**

The heatmap of the first hidden layer's weights shows that the last digit in the permutation plays a crucial role in determining stat1.

Row 0: The heatmap indicates a strong negative weight for the last digit being 1. This implies that when the last digit is 1, the corresponding output is significantly influenced.

Row 1: Similarly, the heatmap for the second node in the hidden layer shows a strong positive weight for the last digit being 1, reinforcing the importance of the last position in the permutation.


**How to compute statistic:**

Rule #1: If the last digit of the permutation is 1, then stat1 equals 1. Otherwise, stat1 equals 0.

Tested the accuracy of the rule is:  1.0, please see last section of stat1.ipynb


## Statistic 2
**Accuracy achieved: 100%**

**Description of model weights:**

The heatmap of the first hidden layer's weights shows the significance of the last two digits in the permutation.

Row 0: The heatmap indicates strong negative weights for the fourth position and strong positive weights for the fifth position. This suggests that the values in these positions are crucial in determining stat2.

Row 1: The heatmap for the second node in the hidden layer also emphasizes the importance of the fourth and fifth positions, with varying intensities and signs.


**How to compute statistic:**

Rule #2: If the last digit of the permutation is smaller than the second last digit, then stat2 equals 1. Otherwise, stat2 equals 0.

Tested the accuracy of the rule is:  1.0, please see last section of stat2.ipynb


## Statistic 3
**Accuracy achieved: 100%**

**Description of model weights:**

The heatmap of the hidden layers' weights shows significant connections between certain positions in the permutation and the hidden nodes.

Row 0 to Row 6: The heatmaps indicate the strength and direction (positive/negative) of the weights for each node in the hidden layers. Notably:

In Row 0, there is a significant weight for the last position (7th position) with both strong positive and negative weights.

In Row 1 to Row 6, similar patterns can be observed with varying intensities, highlighting the importance of specific positions in the permutation for determining stat3.


**How to compute statistic:**

Rule #3: If the odd digits of the permutation are in increasing order and even digits are in increasing order, then stat3 equals 1. Otherwise, stat3 equals 0.

Tested the accuracy of the rule is:  95.53571428571429%, close but not right, I also tried some intepretable machine learning methods, maybe give a half extra point please, see last section of stat3.ipynb


## Statistic 4
**Accuracy achieved: 100%**

**Description of model weights:**

Row 0:

Position 1: Shows a strong positive weight (red).

Position 2: Shows a mixed weight with a slight positive tendency.

Position 3: Shows a mixed weight with slight positive and negative tendencies.

Position 4: Shows a strong positive weight (red).

Position 5: Shows a mixed weight with a slight positive tendency.

Row 1:

Position 1: Shows a strong negative weight (blue).

Position 2: Shows a mixed weight with strong negative and slight positive tendencies.

Position 3: Shows a strong negative weight (blue).

Position 4: Shows a mixed weight with slight positive and negative tendencies.

Position 5: Shows a strong negative weight (blue).


**How to compute statistic:**

Based on the decision tree analysis, stat4 can be computed using the following refined rules:

Decision Tree Rules:

Rule 1: If the 1st digit is less than or equal to 1, stat4 equals 0.

Rule 2: If the 1st digit is greater than 1:

If the 5th digit is less than or equal to 4.5:

If the 2nd digit is less than or equal to 2.5:

If the 2nd digit is less than or equal to 1.5:

If the 4th digit is less than or equal to 3.5, stat4 equals 1.

Otherwise, stat4 equals 0.

Otherwise, stat4 equals 0.

Otherwise:

If the 4th digit is less than or equal to 3.5:

If the 3rd digit is less than or equal to 2.5, stat4 equals 1.

Otherwise, stat4 equals 1.

Otherwise:

If the 4th digit is less than or equal to 4.5, stat4 equals 0.

Otherwise, stat4 equals 1.

If the 5th digit is greater than 4.5, stat4 equals 0.

Tested the accuracy of the rule is:  90.83333333333333%, close but not right, see last section of stat4.ipynb


## Statistic 5
**Accuracy achieved: 40.625%**

**Description of model weights:**

Row 0 to Row 10:

This distribution suggests that the model captures the interactions between different positions to determine the number of inversions.

**How to compute statistic:**

Rule #5: number of inversions in the permutation

Tested the accuracy of the rule is:  1.0, please see last section of stat5.ipynb


## Statistic 6
**Accuracy achieved: 78.125%**

**Description of model weights:**

Row 1 to Row 2:

This distribution suggests that the model captures the interactions between different positions to determine the parity of the number of inversions.

**How to compute statistic:**

Rule #6: 1 if the number of inversions in the permutation is odd, and 0 if the number of inversions is even.

Tested the accuracy of the rule is:  1.0, please see last section of stat6.ipynb


## Statistic 7
**Accuracy achieved: 62.5%**

**Description of model weights:**

Row 0 (Position 1): There is a strong positive weight connection to the first position and a strong negative weight to the second position, indicating the model is focusing on identifying descending pairs involving the first element.

Row 1 (Position 2): Similar to Row 0, strong connections indicate the importance of checking the first two positions for descending pairs.

Row 2 (Position 3): The model appears to focus on the relationship between the second and third positions.

Row 3 (Position 4): This row's weights indicate the model checks the third and fourth positions for descending pairs.

Row 4 (Position 5): The strong weights in this row show the model focuses on the fourth and fifth positions.

**How to compute statistic:**

Rule #7: stat7 is equal to the number of descending pairs

Tested the accuracy of the rule is:  1.0, please see last section of stat7.ipynb

## Statistic 8
**Accuracy achieved: 92.81684027777777%**

**Description of model weights:**

This distribution suggests that the model captures the interactions between different positions to determine the longest run length.

**How to compute statistic:**

Rule #8: For dataset permutations_8.csv, stat8 is 1 if the longest run length in the permutation exceeds 5; otherwise, it is 0.

Tested the accuracy of the rule is:  0.9940476190476191, very close but not right, maybe give a half extra point please, please see last section of stat8.ipynb


## Statistic 9
**Accuracy achieved: 85.69878472222223%**

**Description of model weights:**

This distribution suggests that the model effectively captures the interactions between different positions to determine the number of inversions.

**How to compute statistic:**

Rule #9: For dataset permutations_8 if the number of inversions is less than 4, stat9 is 1. If the number of inversions is 4 or more, stat9 is 0.

Tested the accuracy of the rule is:  0.9652529761904762, close but not right, maybe give a half extra point please, please see last section of stat9.ipynb