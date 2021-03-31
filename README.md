# Fashion MNIST

Simple fashion accessories model predictions using the Fashion MNIST dataset in 
Tensorflow's keras library.

## Installation and usage.

This project uses `pipenv` for dependency management. You need to ensure that you have `pipenv`
installed on your system.

Here's how to install the dependencies, and get started.

- Install it using **`pipenv sync -d`**
- Once done, spawn a shell to run the files: `pipenv shell`

And you're done, and you can run any of the files, and test them.

## Adding your own images.

Sometimes to try predicting on new images and test using `predictions.py`, You need to add them.
Here's how to do it.

- Add the images in the `images` folder.

If you want to test them, Go to `src/predictions.py` and then replace the line with your image name.
Which looks like this: `np.array([get_image("...")`.

<div align="center">
Made by Sunrit Jana with <3
</div>
