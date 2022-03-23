import random

state = 'still'
last_seen = 'right'


def getEnemy(distance):
    if distance < 300:
        return distance
    else:
        return False


def getBorder(light):
    if light > 0.25:
        return True
    else:
        return False


def control(inputs):
    front_left = inputs["front-left"]
    front_right = inputs["front-right"]
    distance_left = inputs["distance-left"]
    distance_right = inputs["distance-right"]
    global state
    global last_seen

    speed = 20
    left_speed = 0
    right_speed = 0

    if getEnemy(distance_left) and getEnemy(distance_right):
        state = 'forward'
        speed = 15
    elif getEnemy(distance_left):
        state = 'turning-left'
        last_seen = 'left'
    elif getEnemy(distance_right):
        state = 'turning-right'
        last_seen = 'right'
    else:
        state = 'searching'

    if getBorder(front_left) and getBorder(front_right):
        state = 'backwards'
    elif getBorder(front_left):
        state = 'turning-right'
    elif getBorder(front_right):
        state = 'turning-left'

    if state == 'still':
        left_speed = 0
        right_speed = 0
    elif state == 'forward':
        left_speed = speed
        right_speed = -speed
    elif state == 'backwards':
        left_speed = -200
        right_speed = 200
    elif state == 'turning-left':
        left_speed = -speed
        right_speed = -speed
    elif state == 'turning-right':
        left_speed = speed
        right_speed = speed
    elif state == 'searching':
        if last_seen == 'right':
            left_speed = 5
            right_speed = 5
        elif last_seen == 'left':
            left_speed = -5
            right_speed = -5

    return {
        'leftSpeed': left_speed,
        'rightSpeed': right_speed,
        'log': [
            {'name': 'Left', 'value': left_speed, 'min': -45, 'max': 45},
            {'name': 'Right', 'value': right_speed, 'min': -45, 'max': 45}
        ]
    }