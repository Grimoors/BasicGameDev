# THE MANDALORIAN : THE GAME

This is an terminal-based arcade game designed in python3 using OOPS concepts.

## HOW TO RUN

python3 main.py

## CONTROLS

| Key   | Action |
| ----- | ------ |
| w     | up     |
| s     | down   |
| a     | left   |
| d     | right  |
| space | shoot  |

## FUNCTIONALITIES

### - hero

The hero can be controlled by the user and can be made to go up, or down, or left, or right.  
He can also fire bullets that can destroy beams and hurt the enemy dragon.  
The bullets can also collect coins to give points

### - beam

Beams hurt the hero. However, these beams can be destroyed by bullets fired by the hero to give points (20)
They are of four types:

1. Horizontal
2. Vertical
3. Diagonal1 (/)
4. Diagonal2 (\)

### - coins

Give points according to the following metric:

| Collected by | Score |
| ------------ | ----- |
| Hero         | 10    |
| Bullet       | 5     |

### - powerups

Following are the powerups implemented

| Powerup Name | Look | Functionality                              |
| ------------ | ---- | ------------------------------------------ |
| SpeedUp      | A    | Doubles the speed of the game              |
| ExtraLife    | +    | Increases your life by 1                   |
| Snake        | $    | Convert to your dragon form                |
| shield       | ░    | Puts a shield that protects you from beams |
| Extra Time   | +    | Gives extra time                           |

### - enemy

The cool enemy dragon that can kill you with his freezing ice balls that destroy everything on its path! He even follows you!

### - magnet

The magnet attracts the hero towards it. However, if the hero touches the magnet, he dies due to the excessive attractive force.

## OTHER COOL STUFF IMPLEMENTED

- A timer that once run out, the player dies
- A long life span (10 lives)
- A gun with bullets that restore with time

## THE CODE

The classes used can be found in detail in the file: classes_used.md
