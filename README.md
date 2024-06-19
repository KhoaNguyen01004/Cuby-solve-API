# Cube-solve-API
Cube-solve-API is a Python-based web application that provides an API to solve a Rubik's cube. This project is built using the Flask framework and leverages the Kociemba algorithm to solve the Rubik's cube.  


## Features
- **Solve Rubik's Cube**: The API accepts a string representation of a Rubik's cube and returns a solution. 
- **Error Handling**: The API handles invalid cube strings and returns an appropriate error message.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.12
- pip
 
### Installation
#### 1. Clone the repository

```bash
git clone https://github.com/quentinformatique/Cube-solve-API.git
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the application
```bash
python run.py
```

The application should now be running on `http://127.0.0.1:5000/`.

## Usage

### Solve Rubik's Cube

To solve a Rubik's cube, make a GET request to the /solve/<cubeString> endpoint where cubeString is a string representation of the Rubik's cube.

Example:
```bash
curl http://127.0.0.1:5000/solve/your-cube-string
```

## Built With

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Web framework
- [Kociemba](http://kociemba.org/) - Rubik's cube solver algorithm

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project and help make it better. You can contribute by:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
