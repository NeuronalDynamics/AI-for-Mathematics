import torch
from torch.utils.data import DataLoader
def train_one_epoch(training_loader, model, loss_fn, optimizer, device):
    """
    Trains the model for one epoch using the given training data loader, model, loss function, and optimizer.
    
    Args:
        training_loader (torch.utils.data.DataLoader): The data loader for the training data.
        model (torch.nn.Module): The model to be trained.
        loss_fn (torch.nn.loss._Loss): The loss function used to compute the loss.
        optimizer (torch.optim.Optimizer): The optimizer used to update the model parameters.
        
    Returns:
        float: The total loss computed over the entire epoch.
    """
    # TODO: Use https://pytorch.org/tutorials/beginner/introyt/trainingyt.html#the-training-loop as a reference.
    # Set the model to training mode
    model.train()
    
    # Initialize the total loss for the epoch
    total_loss = 0.0
    
    # Iterate over the training data loader
    for batch in training_loader:
        # Get the inputs and targets from the batch
        inputs, targets = batch
        
        # Move inputs and targets to the appropriate device (CPU or GPU)
        inputs, targets = inputs.to(device), targets.to(device)
        
        # Zero the parameter gradients
        optimizer.zero_grad()
        
        # Forward pass: compute the model output
        outputs = model(inputs)
        
        # Compute the loss
        loss = loss_fn(outputs, targets)
        
        # Backward pass: compute the gradients
        loss.backward()
        
        # Update the model parameters
        optimizer.step()
        
        # Accumulate the loss
        total_loss += loss.item()
    
    # Compute the average loss over the epoch
    average_loss = total_loss / len(training_loader)
    
    return average_loss

def evaluate_model(model, test_dataset):
    """
    Evaluates the model using the provided test dataset and returns the confusion matrix.

    Args:
        model (torch.nn.Module): The model to be evaluated.
        test_dataset (torch.utils.data.Dataset): The dataset used for evaluation.

    Returns:
        list: A 2x2 confusion matrix where rows represent true labels and columns represent predicted labels.
    """
    '''
    model.eval()

    with torch.no_grad():
        confusion_matrix = [[0, 0], [0, 0]]
        # TODO
        pass
    '''
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.eval()
    
    # Create a DataLoader for the test dataset
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    # Initialize the confusion matrix
    confusion_matrix = [[0, 0], [0, 0]]
    
    with torch.no_grad():
        for inputs, true_labels in test_loader:
            # Move inputs and true labels to the appropriate device
            inputs, true_labels = inputs.to(device), true_labels.to(device)
            
            # Get the model predictions
            outputs = model(inputs)
            _, predicted_labels = torch.max(outputs, 1)
            
            # Update the confusion matrix
            for true_label, predicted_label in zip(true_labels, predicted_labels):
                confusion_matrix[true_label.item()][predicted_label.item()] += 1

    return confusion_matrix