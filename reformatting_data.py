import numpy as np
import tensorflow as tf



def change(num):
    if num == 0:
        return np.array([1, 0, 0])
    elif num == 1:
        return np.array([0, 1, 0])
    elif num == 2:
        return np.array([0, 0, 1])
    
def format(sequence, sequence_length):
    input_sequences = []
    target_values = []
    i = 0
    while i < len(sequence) - sequence_length:
        input_seq = sequence[i:i + sequence_length]  # Extract the input sequence
        target_value = sequence[i + sequence_length]  # Extract the target value
        input_seq_encoded = [change(num) for num in input_seq]  # Convert input sequence to one-hot encoded format
        target_value_encoded = change(target_value)  # Convert target value to one-hot encoded format
        input_sequences.append(input_seq_encoded)
        target_values.append(target_value_encoded)
        i += sequence_length + 1

    return input_sequences, target_values

#def format(sequence, sequence_length):
    
    input_sequences = []
    target_values = []
    i = 0
    while(i < len(sequence) - sequence_length):
        input_seq = sequence[i:i+sequence_length]  # Extract the input sequence
        target_value = sequence[i+sequence_length:i+sequence_length+1]  # Extract the target value
        input_sequences.append(change(input_seq))
        target_values.append(change(target_value))
        i += (sequence_length + 1)

    return(input_sequences, target_values)

