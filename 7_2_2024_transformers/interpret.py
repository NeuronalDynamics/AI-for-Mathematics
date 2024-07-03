import matplotlib.pyplot as plt
import torch
import seaborn as sns
import numpy as np

from data import PAD_TOKEN, padding_mask


def plot_linear_layer(
    layer,
):
    """
    Plots a heatmap of the weights for a linear layer.

    Parameters:
        layer (nn.Linear): The Linear layer for which the weights are to be visualized.
    """
    # TODO
    #return
    weights = layer.weight.detach().cpu().numpy()
    plt.figure(figsize=(10, 8))
    sns.heatmap(weights, annot=True, cmap='viridis')
    plt.title(f'Heatmap of {layer.__class__.__name__} weights')
    plt.xlabel('Input Units')
    plt.ylabel('Output Units')
    plt.show()



def incorrect_predictions(model, dataloader):
    """
    Given a model and a dataloader, this function evaluates the model by predicting the labels for each input in the dataloader.
    It keeps track of incorrect predictions and returns a list of inputs that were incorrectly predicted for each label.

    Args:
        model (torch.nn.Module): The model used for prediction.
        dataloader (torch.utils.data.DataLoader): The dataloader containing the input data.

    Returns:
        List[List[List[int]]]: A list of incorrect predictions for each label. The list contains two sublists, one for each label.
            Each sublist contains a list of inputs that were incorrectly predicted for that label.
            Each input is represented as a list of integers.
    """
    """
    model.eval()

    with torch.no_grad():
        # Initialize the list to track incorrect predictions for each class
        num_classes = 2  # Assuming binary classification, change this if you have more classes
        incorrect_predictions = [[] for _ in range(num_classes)]

        for data in dataloader:
            inputs, labels = data
            output = model(inputs, mask=padding_mask(inputs))
            predictions = torch.argmax(output, dim=1)

            for input, label, prediction in zip(inputs, labels, predictions):
                label_scalar = label.item() if label.dim() == 0 else label[0].item()
                prediction_scalar = prediction.item() if prediction.dim() == 0 else prediction[0].item()
                if label_scalar != prediction_scalar:
                    incorrect_predictions[label_scalar].append(input.tolist())

    return incorrect_predictions
    """

    model.eval()
    incorrect_predictions_list = [[], []]  # To store incorrect predictions for each label

    with torch.no_grad():
        for data in dataloader:
            inputs, labels = data
            output = model(inputs, mask=padding_mask(inputs))
            predictions = torch.argmax(torch.select(output, 1, 0), dim=1)  # Get predicted class labels

            for input_tensor, label, prediction in zip(inputs, labels, predictions):
                # Ensure label is a scalar
                if label.item() != prediction.item():
                    incorrect_predictions_list[label.item()].append(input_tensor.tolist())

    return incorrect_predictions_list


def token_contributions(model, single_input):
    """
    Calculates the contributions of each token in the single_input sequence to each class in the model's
    predicted output. The contribution of a single token is calculated as the difference between the
    model output with the given input and the model output with the single token changed to the other
    parenthesis.

    Args:
        model (torch.nn.Module): The model used for prediction.
        single_input (torch.Tensor): The input sequence for which token contributions are calculated.

    Returns:
        List[float]: A list of contributions of each token to the model's output.
    """
    """
    output = model(single_input, mask=padding_mask(single_input))

    result = []
    # TODO
    return result
    """
    output = model(single_input)
    contributions = []

    for i in range(single_input.size(1)):  # Loop over each token
        modified_input = single_input.clone()
        modified_input[0, i] = 1 - single_input[0, i]  # Flip the token
        
        # Ensure the modified input values are within valid range
        modified_input[0, i] = torch.clamp(modified_input[0, i], 0, model.embed.num_embeddings - 1)
        
        modified_output = model(modified_input)
        contribution = (output - modified_output).abs().sum().item()
        contributions.append(contribution)
    
    #plt.figure(figsize=(10, 6))
    #sns.heatmap([contributions], annot=True, cmap='viridis')
    #plt.title('Token Contributions')
    #plt.xlabel('Token Position')
    #plt.ylabel('Contribution')
    #plt.show()
    
    return contributions

def activations(model, dataloader):
    """
    Returns the frequency of each hidden feature's activation in the feedforward layer of the model
    over all inputs in the dataloader.

    Args:
        model (torch.nn.Module): The model used for prediction.
        dataloader (torch.utils.data.DataLoader): The dataloader containing the input data.

    Returns:
        List[int]: A list of frequencies for each hidden feature in the feedforward layer of the model.
    """
    """
    result = []
    # TODO
    return result
    """
    activation_counts = []

    def hook(module, input, output):
        print("Hook triggered")
        print("Output shape:", output.shape)
        activation_counts.append(output.detach().cpu().numpy())

    # Access the first transformer encoder layer
    transformer_layer = model.encoder.layers[0]
    hook_handle = transformer_layer.register_forward_hook(hook)

    with torch.no_grad():
        for inputs, _ in dataloader:
            model(inputs)

    hook_handle.remove()

    if not activation_counts:
        print("No activations recorded.")
        return []

    # Concatenate and sum activation counts over the batch and sequence length dimensions
    activation_counts = np.concatenate(activation_counts, axis=0)
    print("Activation counts shape:", activation_counts.shape)
    feature_activations = activation_counts.sum(axis=(0, 1))

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(feature_activations)), feature_activations)
    plt.title('Feedforward Layer Activations')
    plt.xlabel('Feature Index')
    plt.ylabel('Activation Count')
    plt.show()

    return feature_activations.tolist()