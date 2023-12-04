import numpy as np
import tensorflow as tf
from reformatting_data import format
from reformatting_data import change
from testing import playRockPaperScissors


sequence = [
0,1,2,0,1,1,0,2,1,2,0,0,2,1,0,1,1,1,2,2,2,0,1,2,
0,2,2,1,0,2,1,0,0,1,2,0,0,1,2,1,1,0,0,2,1,0,1,2,
0,1,1,0,0,1,2,2,2,0,0,1,1,0,2,2,0,1,2,0,0,1,2,0,
0,0,1,2,2,1,0,0,2,1,1,0,2,1,1,0,2,2,0,1,0,0,2,1,
1,2,2,0,1,0,1,2,1,0,1,2,0,1,2,0,1,1,2,0,0,2,2,0,
2,0,2,0,1,1,2,1,0,1,2,0,1,1,2,0,0,2,1,0,1,0,2,2,
2,0,2,1,1,2,0,2,0,1,1,2,2,0,0,1,2,0,1,0,2,1,2,1,
1,2,0,1,0,2,0,2,2,0,1,1,1,2,0,1,0,2,0,1,1,2,0,0,
1,2,0,2,1,2,2,1,0,0,1,1,0,0,2,1,2,0,1,2,0,1,0,2,
2,1,0,1,0,2,0,2,1,1,2,0,1,0,0,1,2,1,1,2,0,0,2,1,
0,2,1,1,0,1,0,0,2,2,1,0,2,1,2,0,1,1,2,2,1,0,0,1,
0,1,1,2,0,2,1,0,1,2,1,1,2,0,0,1,1,2,0,0,2,0,0,1,
0,2,1,1,2,1,0,0,1,2,0,0,1,2,1,2,0,0,1,1,2,1,0,0,
0,1,0,1,1,2,2,0,1,1,2,2,0,1,2,0,0,2,2,1,0,0,2,1,
0,1,1,2,0,0,2,1,0,0,1,1,2,0,0,2,1,0,0,1,1,2,2,0,
1,2,0,0,0,1,1,2,2,0,0,1,2,2,0,1,1,2,2,0,1,1,2,0,
2,1,1,0,0,1,2,1,0,0,1,2,0,0,1,2,2,0,0,1,2,0,0,0,
2,2,0,0,2,1,1,0,0,2,1,0,1,1,0,2,0,0,1,2,1,1,1,0,
0,2,0,0,2,1,1,0,0,2,1,1,0,0,1,2,2,0,1,2,0,0,1,1,
2,2,0,0,1,2,0,1,1,2,0,2,1,1,0,1,2,0,0,1,2,0,0,1,
2,2,1,1,0,1,2,2,1,0,2,1,1,0,0,1,2,0,0,1,2,0,2,1,
0,2,1,1,0,2,2,0,0,1,2,0,1,1,0,2,2,0,1,1,2,0,0,1,
0,2,2,1,0,1,2,1,0,2,1,1,0,2,1,1,0,2,0,1,2,2,0,1,
0,1,0,2,0,2,1,0,2,0,2,1,0,2,1,1,1,2,1,1,0,1,2,0,
0,1,0,2,1,2,2,0,0,1,2,0,0,2,1,1,0,2,1,2,1,0,2,0,
0,2,1,1,0,1,2,2,0,2,1,2,0,0,1,1,2,0,2,1,0,0,1,2,
0,2,1,2,0,2,1,0,0,1,2,0,2,1,1,0,0,2,0,1,2,0,0,2,
0,2,1,2,0,2,1,1,2,0,0,1,2,2,1,0,1,2,1,0,0,1,2,2,
2,1,0,0,1,2,0,1,2,0,1,2,0,2,1,0,0,2,1,0,0,2,1,1,
2,1,0,0,1,2,1,2,2,1,0,1,2,2,0,2,1,2,1,0,2,1,1,2,
0,1,1,2,0,0,2,1,0,2,0,1,1,2,1,1,2,0,1,2,0,2,1,2,
0,2,1,0,0,1,2,2,1,0,2,1,0,0,1,2,2,1,0,0,1,2,2,1,
0,0,2,2,1,2,2,1,0,0,2,1,2,1,1,0,2,2,2,1,1,0,1,2,
2,0,1,2,1,1,2,0,0,1,2,2,1,2,0,0,1,1,2,0,2,0,0,1,
2,0,1,2,0,0,1,2,2,2,0,0,1,2,2,0,1,1,2,2,0,2,1,0,
0,2,1,2,0,0,2,1,1,2,0,0,2,1,1,2,0,2,1,1,0,1,2,0,
0,2,1,1,0,0,2,2,1,0,2,1,1,2,0,0,1,2,0,0,1,2,0,0,
2,2,1,1,0,0,2,1,2,0,1,1,2,0,2,1,0,2,0,0,1,2,2,0,
1,2,0,2,1,0,0,1,1,2,0,0,1,1,2,2,2,0,2,1,0,0,1,1,
2,0,0,2,1,0,2,1,1,0,0,2,1,0,0,2,0,2,0,2,0,1,1,2,
0,0,1,1,2,2,0,1,2,1,1,2,0,0,2,1,1,2,1,0,2,2,1,2,
0,1,2,2,0,0,1,2,1,1,2,0,0,1,1,2,0,0,1,2,2,0,0,2,
1,1,0,0,2,2,0,1,1,2,0,0,2,1,0,0,1,1,2,2,0,0,1,2,
0,1,2,1,1,0,0,1,2,0,0,1,2,2,0,1,1,2,1,1,0,0,1,1,
2,0,0,1,1,2,0,0,1,2,0,0,1,2,0,0,1,2,2,1,1,2,0,0,
1,2,2,0,0,2,0,0,1,1,2,2,0,0,1,2,0,0,0,1,2,2,0,0,
1,2,0,0,0,1,2,0,0,2,0,2,0,0,1,2,2,0,0,1,2,2,2,0,
0,2,1,1,2,0,0,2,0,1,2,1,1,2,2,1,1,0,2,0,0,1,1,2,
2,0,2,0,0,2,0,1,2,0,0,1,1,2,2,0,0,1,1,0,2,0,0,1,
2,0,0,1,1,2,0,0,2,1,1,2,0,1,2,0,2,0,1,2,0,2,1,1,
0,0,2,1,0,0,2,1,1,0,2,1,2,0,0,2,1,1,0,2,1,0,0,2,
1,1,2,0,0,2,1,0,1,2,2,0,2,2,0,1,1,2,1,1,0,1,2,0,
0,1,2,0,0,1,2,0,0,1,1,2,0,2,0,0,2,1,1,0,2,0,0,1,
2,2,0,2,1,0,2,0,0,2,0,2,0,0,1,2,0,2,0,2,0,0,1,0,
0,2,0,2,1,1,0,2,0,2,0,2,0,0,2,0,0,2,1,1,0,0,2,1,
0,0,1,2,0,0,2,0,0,2,0,0,2,1,1,0,0,2,0,0,1,2,2,0,
0,1,1,2,2,0,1,2,0,0,2,2,0,1,2,0,0,2,0,0,2,0,0,1,
1,2,0,0,1,1,0,2,0,2,0,2,0,0,2,0,2,0,0,2,1,0,1,2,
0,2,0,1,1,2,1,0,2,0,1,0,0,2,0,1,1,2,0,2,0,0,1,1,
2,0,0,2,1,1,0,1,2,0,0,1,1,0,0,2,0,1,2,0,2,0,1,2,
0,1,0,1,2,0,0,1,0,2,0,2,0,0,1,2,0,0,2,0,0,2,1,1,
0,1,2,0,1,1,0,2,1,1,2,0,2,0,0,1,2,1,0,0,1,2,2,0,
1,1,0,1,2,0,0,1,2,2,0,1,1,0,2,2,0,2,0,1,0,1,1,2,
0,0,1,2,2,1,1,0,0,1,2,0,2,1,0,1,2,0,0,2,2,1,0,1,
0,2,1,0,0,1,2,0,1,0,2,2,1,0,2,0,1,1,0,2,1,0,0,1,
2,0,2,0,0,1,2,2,0,2,0,2,0,0,1,2,2,1,1,0,2,0,0,1,
1,0,1,1,0,2,2,0,2,1,0,2,1,1,0,2,2,1,1,0,2,0,0,2,
1,0,0,2,1,0,0,0,1,2,1,1,0,2,0,1,2,2,0,2,1,1,0,1,
2,0,0,2,1,1,0,2,2,1,0,2,1,0,0,1,2,0,2,1,0,2,1,0,
0,2,0,1,2,1,1,0,2,1,1,0,1,2,0,2,2,1,1,0,2,1,0,1,
2,0,0,2,1,1,0,0,0,1,1,2,0,2,1,1,0,2,1,2,2,1,1,0,
1,2,1,0,2,1,0,0,1,1,0,1,2,2,0,1,1,2,0,0,1,2,0,2,
0,1,2,2,1,0,0,2,1,0,2,1,1,0,2,0,2,1,0,0,2,1,1,0,
2,1,0,2,2,0,2,1,0,2,1,1,0,2,1,0,2,1,1,0,2,0,2,1,
0,0,2,1,0,2,0,0,2,1,0,2,1,0,0,2,0,2,0,0,2,0,1,0
]

test_vals1 = [0,2,0,1,1,0,2,0,2,0,1,1,0,2,1,1,0,2,0,1,2,2,0]
test_vals2 = [1,0,2,0,1,1,0,2,0,2,0,1,2,0,2,1,0,0,2,1,1,0,2]
test_vals3 = [0,2,0,1,2,0,2,1,0,1,2,0,0,1,2,2,0,1,1,0,0,1,2]
test_vals4 = [0,0,1,0,2,0,2,1,0,2,1,0,1,1,2,0,2,0,1,2,0,0,2]
test_vals5 = [0,1,0,2,0,2,0,1,2,0,1,1,0,2,0,1,2,0,0,1,0,0,1]
test_vals6 = [0,2,0,1,1,2,0,2,1,0,1,0,2,0,1,1,0,2,0,2,1,1,0]
        
#anwer = 1
# Define the input sequence length and number of classes
sequence_length = 23
num_classes = 3

input_sequences, target_values = format(sequence, sequence_length)

# Define the RNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(64, input_shape=(sequence_length, num_classes)),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Prepare the training data
# X_train is a list of input sequences, y_train is a list of target values
# Each input sequence and target value should be in one-hot encoded format
X_train = np.array(input_sequences)  # shape: (num_examples, sequence_length, num_classes)
y_train = np.array(target_values)  # shape: (num_examples, num_classes)
# Train the model
model.fit(X_train, y_train, epochs=150, batch_size=75, verbose=2)


def toMove(val):
    predict = 'predicted move not valid'
    if (val == 0):
        predict = 'rock'
    elif(val == 1):
        predict = 'paper'
    elif(val == 2):
        predict = 'scissors'
    return (predict)

# Use the trained model to make predictions
# X_test is a list of input sequences for prediction  # shape: (num_examples, sequence_length, num_classes)
def makePredictions(vals, should):
    X_test = np.array([change(num) for num in vals])
    X_test = X_test.reshape(-1, sequence_length, num_classes)

    # Use the trained model to make predictions
    predictions = model.predict(X_test)
    index_of_largest = np.argmax(predictions)
    predict = toMove(index_of_largest)
    # Decode the predictions to obtain the final numbers
    print('my prediction for the test value is: ' + predict + 'the array is ' + str(predictions))
    print('should return ' + toMove(should))
    
makePredictions(test_vals1, 1)
makePredictions(test_vals2, 2)
makePredictions(test_vals3, 2)
makePredictions(test_vals4, 1)
makePredictions(test_vals5, 2)
makePredictions(test_vals6, 2)

xx, bb = playRockPaperScissors()
makePredictions(xx, bb)
