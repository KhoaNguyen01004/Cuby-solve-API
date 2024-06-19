from flask import Flask, request, jsonify
from app import app
from app.models import solve_rubiks_cube


@app.route('/solve/<cubeString>', methods=['GET'])
def solve(cubeString):
    try:
        solution = solve_rubiks_cube(cubeString)
        return jsonify({'solution': solution})
    except ValueError:
        return jsonify({'error': 'Invalid cube string'}), 400
