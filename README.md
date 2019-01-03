# Rock_Paper_Scissors_PyTorch
Builiding a basic neuronal network with 2 fully connected layers in order to classify 3 hand positions : Rock Paper Scissors
## Create a custom dataset
Taking several pictures of Rock,paper and Scissors with your hand under different angles, light, or background in order to make it a bit strong.
For the purpose of making it quick the picture were reshaped and the shape chosen was 32x32 using the file resize.
```bash
# Dont forget to modify the Path.

python resize.py

```
## Building the NN
First splitting the dataset into two pieces : Train & Test.
### Split dataset

```python

train_size = int(0.8 * len(image_data)) //image_data is your image Folder
test_size = len(image_data) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(image_data, [train_size, test_size])

```
## The model
The model has 3 fully connected layers: an input layer (1024), two hidden layers (256->64) and an output layer (3 ...Obviously!).
The activation function chosen here was the Selu. It increases the accuracy and made the epochs faster.
### The Layers
```python

        fc0 = nn.Linear(32 * 32, 16*16)
        fc1 = nn.Linear(16 * 16, 8*8)
        fc2 = nn.Linear(8*8, 3)
```
### Activation function
```python
        x = x.view((-1, 1024))
        h = F.selu(self.fc0(x))
        h = F.selu(self.fc1(h))
        out = self.fc2(h)
        return F.log_softmax(out) 
  ```

## Accuracy and loss results
With a 202 pictures in my datasets here is the results and it's a decent accuracy for a small dataset. 

![screenaccuracy](https://user-images.githubusercontent.com/45148200/49187963-6c5dc380-f369-11e8-8522-34c4e09b7c17.PNG)
