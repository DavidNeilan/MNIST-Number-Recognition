# MNIST Number Recognition
As part of my Emerging Tech module I was tasked to develop a neural network to recognise hand-drawn digits using 
training data from the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). The project specification can be found
[here](https://github.com/ianmcloughlin/project-2019-emtech)

## Requirements
* *Python(3.7)*
* *opencv-python(1.1.1)*
* *tensorflow(2.0.0)*
* *numpy(1.17.4)*
* *Flask(1.1.1)*
* *mathplotlib(3.1.2)*
* *Keras(2.3.1)*

Requirements can be installed using: `pip install -r requirements.txt`

A trained model is also required. This can be generated using the Jupyter notebook or a pre-trained one is available
from the [Releases Page](https://github.com/DavidNeilan/MNIST-Number-Recognition/releases)

`server.py` may need to be altered if you store the model in a different directory.

## Research

I found the [Keras Documentation](https://keras.io/layers/core/) to be well written and a good source of information for
explaining the various levels.

I have watched [Sendex](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ/) for years and found his videos
discussing machine learning and MNIST to be an excellent addition on top of the lecturer videos received as part of my
GMIT course.

The [MNIST website](http://yann.lecun.com/exdb/mnist/) contained good information on the structure of the dataset.
Although this information could be sought from the dataset without the documentation it was good to get an insight as to
why the data is structured as it is. I had originally wrote a parser using the information from the website however it
was ultimately useless as Keras has inbuilt methods for extracting the data.

I have extensive experience with Flask and have learned mainly from [Flask's website](https://flask.palletsprojects.com/en/1.1.x/)
as well as previous Youtube tutorials.

I am familiar with using the HTML5 canvas as per previous GMIT projects. I have based my canvas drawing of a
[Codicode tutorial](https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx) and adapted it to suit
the project and remove jQuery as a dependency;

## References
* https://keras.io/
* https://stackoverflow.com/a/46275857
* https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ/
* https://flask.palletsprojects.com/en/1.1.x/
* https://opencv-python-tutroals.readthedocs.io
* https://www.codicode.com/art/how_to_draw_on_a_html5_canvas_with_a_mouse.aspx
