# pdf-emotions

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About <a name = "about"></a>
ML project combining Tensorflow multiclass classification with pdfreader to distinguish pdf files by their emotion

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

- Python 3.12.3
- pip

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Create project folder

```sh
mkdir pdf-emotions
```
```sh
cd pdf-emotions
```

Clone this repository

```sh
git clone https://github.com/CalifornianNightmare/pdf-emotions
```

Set up virtual enviroment and log in

```sh
python -m venv .venv
```
```sh
source .venv/bin/activate
```

Install requirements

```sh
pip install --no-cache-dir -r requirements.txt
```

Run the app

```sh
python app.py
```

### Runing in Docker

Build the image (replace __pdfemotion__ with custom name if necessary)

```sh
sudo docker build -t pdfemotion .
```

Run the image

```sh
sudo docker run -it pdfemotion
```

Run the image in bash (For debugging purposes)

```sh
sudo docker run -it --entrypoint /bin/bash pdfemotion
```


## Usage <a name = "usage"></a>

> ### Select a PDF

Searches for a PDF, transforms it to text, returns percieved emotional tone (Can be: Anger, Sadness, Fear, Joy)

The files are read from the `/files/` folder. Only `.pdf` types are allowed

> ### Manual text input

Waits for user text input, returns percieved emotional tone

> ### About

Shows short info box about the app

> ### Exit

Exits the app