# Summary of findings.

## Statistic 1
**Accuracy achieved: 100%**

**Description of model weights:**
Model Architecture:
The model consists of an input layer with n^2 nodes (one-hot encoded permutations of length n).
There is one hidden layer with a specified number of nodes (in this case, 2 nodes).
The output layer produces a binary output, indicating the value of stat1.

Heatmap Visualization:

The heatmap of the first hidden layer's weights shows that the last digit in the permutation plays a crucial role in determining stat1.
Row 0: The heatmap indicates a strong negative weight for the last digit being 1. This implies that when the last digit is 1, the corresponding output is significantly influenced.
Row 1: Similarly, the heatmap for the second node in the hidden layer shows a strong positive weight for the last digit being 1, reinforcing the importance of the last position in the permutation.

Model Feature Connections:

The connection plot visualizes the weights between the input layer and the hidden layer.
The lines' thickness and color (red for positive weights, blue for negative weights) illustrate the influence of each input feature (each position in the permutation) on the hidden nodes.
The plot shows that the connections from the last position in the permutation to the hidden nodes are the most significant, further supporting the observation that the last digit is critical in determining stat1.

**How to compute statistic:**

Rule #1: If the last digit of the permutation is 1, then stat1 equals 1. Otherwise, stat1 equals 0.

Tested the accuracy of the rule is:  1.0, please see last section of stat1.ipynb


## Statistic 2
**Accuracy achieved: 100%**

**Description of model weights:**
Model Architecture:

The model consists of an input layer with n^2 nodes (one-hot encoded permutations of length n).
There is one hidden layer with a specified number of nodes (in this case, 2 nodes).
The output layer produces a binary output, indicating the value of stat2.

Heatmap Visualization:

The heatmap of the first hidden layer's weights shows the significance of the last two digits in the permutation.
Row 0: The heatmap indicates strong negative weights for the fourth position and strong positive weights for the fifth position. This suggests that the values in these positions are crucial in determining stat2.
Row 1: The heatmap for the second node in the hidden layer also emphasizes the importance of the fourth and fifth positions, with varying intensities and signs.

Model Feature Connections:

The connection plot visualizes the weights between the input layer and the hidden layer.
The lines' thickness and color (red for positive weights, blue for negative weights) illustrate the influence of each input feature (each position in the permutation) on the hidden nodes.
The plot shows that the connections from the last two positions in the permutation to the hidden nodes are the most significant, supporting the observation that these positions are critical in determining stat2.

**How to compute statistic:**

Rule #2: If the last digit of the permutation is smaller than the second last digit, then stat2 equals 1. Otherwise, stat2 equals 0.

Tested the accuracy of the rule is:  1.0, please see last section of stat2.ipynb


## Statistic 3
**Accuracy achieved: 100%**

**Description of model weights:**
Model Architecture:

The model consists of an input layer with n^2 nodes (one-hot encoded permutations of length n).
There are multiple hidden layers with specified nodes.
The output layer produces a binary output, indicating the value of stat3.

Heatmap Visualization:**

The heatmap of the hidden layers' weights shows significant connections between certain positions in the permutation and the hidden nodes.**
Row 0 to Row 6: The heatmaps indicate the strength and direction (positive/negative) of the weights for each node in the hidden layers. Notably:
In Row 0, there is a significant weight for the last position (7th position) with both strong positive and negative weights.
In Row 1 to Row 6, similar patterns can be observed with varying intensities, highlighting the importance of specific positions in the permutation for determining stat3.

Model Feature Connections:

The connection plot visualizes the weights between the input layer and the hidden layers.
The lines' thickness and color (red for positive weights, blue for negative weights) illustrate the influence of each input feature (each position in the permutation) on the hidden nodes.
The plot shows complex connections from multiple positions in the permutation to the hidden nodes, supporting the observation that multiple positions are critical in determining stat3.

**How to compute statistic:**

Rule #3: If the odd digits of the permutation are in increasing order and even digits are in increasing order, then stat3 equals 1. Otherwise, stat3 equals 0.

Tested the accuracy of the rule is:  95.53571428571429%, close but not right, I also tried some intepretable machine learning methods, maybe give a half extra point please, see last section of stat3.ipynb


## Statistic 4
**Accuracy achieved:**

**Description of model weights:**

**How to compute statistic:**

## Statistic 5
**Accuracy achieved:**

**Description of model weights:**

**How to compute statistic:**

## Statistic 6
**Accuracy achieved:**

**Description of model weights:**

**How to compute statistic:**

## Statistic 7
**Accuracy achieved:**

**Description of model weights:**

**How to compute statistic:**

## Statistic 8
**Accuracy achieved:**

**Description of model weights:**

**How to compute statistic:**

## Statistic 9
**Accuracy achieved:**

**Description of model weights:**

**How to compute statistic:**