## FAST API project-of-the-week

This repo is part of the [#project-of-the-week](https://datatalks.club/slack) channel in slack. 

## Contect

```requirements.txt ```
* The libraries needed to run this repo

```data and model.ipynb ```
* Is notebook that contains the data and the trained model for this repo.

```model/bcancer_model_v1.pkl ```
* Contains the model pkl that is used in the fast-api service.

```fast_api_test.py```
* FastAPI testing script with no conncetion to the model

```ml_serve_fast_api.py```
* Contains the service that in the /predict gives the bcancer prediciton.

## Instructions (using UI swager)

You can install your enviroment (recomended Python 3.8 or 3.9) and install the requimrents.txt libraries

Then run ml_serve_fast_api.py and go to http://localhost:8000/docs

Press Try it out

<img src="images\part1.png" width="400">

Then execute

<img src="images\part2.png" width="240">

Check the result in the response body

<img src="images\part3.png" width="400">