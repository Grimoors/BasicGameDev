# DEBUG MODE
debug = 0
powerUpTesting = 0
test_enemy = 0

# THE PLAYER PERSONAL STUFF
username = 'Player'
score = 0
coins_collected = 0

# GAME CONSTANTS
screen_length = 120
screen_height = 30
length_of_beam = 10
safe_region = 1
frame_refresh_time = 0.05
total_life = 10
total_bullets = 10
total_no_screens = 15
enemy_comes_after = 5
boss_total_life = 200
move_left_time = 0.1
total_time = 2000

# GAME RELATED GLOBAL VARIABLES
game_start_time = 0
shown_until = screen_length
bullets_left = 3  # count of deployable bullets
enemy_come = 0
magnet_y_pos_fullboard = 0
time_left = total_time
ball_gravity_count = 0
last_move_up_time = 0

# POWER UP RELATED VARIABLES
speeded = 0
snek = 0
shielded = 0
shielded_power_up_counter = -1
speeded_power_up_counter = -1
snek_power_up_counter = -1
snake_timer = 50
speed_timer = 100
speeded_active_timer = 0
trigger = 0
snake_collected = 0

# ENEMY STYLES

enemy_style_1 = [
    [' ', '|', '\\', '_', '/', '/', '|', ' ', ' ', ' ', '/', '_', '('],
    [' ', '_', '/', '(', 'o', ')', '/', ' ', ' ', '/', '_', '(', ' '],
    ['/', '_', '_', '.', '-', '.', ' ', '\\', '/', '_', '_', '(', ' '],
    [' ', ' ', '_', '_', '/', '_', '_', '/', '_', '_', '_', '(', ' '],
    [' ', '¨', '-', '¨', '-', '¨', '-', '¨', '-', '¨', ' ', ' ', ' ']
]

enemy_style_2 = [
    [' ', '|', '\\', '_', '/', '/', '|', ' ', ' ', ' ', '/', '_', '('],
    [' ', '_', '/', '(', 'o', ')', '/', ' ', ' ', '/', '_', '(', ' '],
    ['/', 'o', '_', '.', '-', '.', ' ', '\\', '/', '_', '_', '(', ' '],
    [' ', ' ', '_', '_', '/', '_', '_', '/', '_', '_', '_', '(', ' '],
    [' ', '¨', '-', '¨', '-', '¨', '-', '¨', '-', '¨', ' ', ' ', ' ']
]

enemy_style_dead = [
    [' ', '|', '\\', '_', '/', '/', '|', ' ', ' ', ' ', '/', '_', '('],
    [' ', '_', '/', 'x', 'x', 'x', '/', ' ', ' ', '/', '_', '(', ' '],
    ['/', 'o', '_', '.', '-', '.', ' ', '\\', '/', '_', '_', '(', ' '],
    [' ', ' ', '_', '_', '/', '_', '_', '/', '_', '_', '_', '(', ' '],
    [' ', '¨', '-', '¨', '-', '¨', '-', '¨', '-', '¨', ' ', ' ', ' ']
]

snake_test = [
    [' ', ' ', ' ', '.', '-', '-', ',', ' ', '/', '[', '▄'],
    ['-', '-', '/', ' ', ' ', ' ', ' ', '\\', '-', '|', '|']
]
snake = [['-', '_'], ['-', '_']]
# STUFF TO BE DONE BEFORE THE START OF THE GAME


def homework():
    # FIX THE SHAPE OF THE DRAGON
    for i in enemy_style_1:
        i = i.reverse()
    for i in enemy_style_2:
        i = i.reverse()
    for i in enemy_style_dead:
        i = i.reverse()


# CHECKING IF DEAD VARIABLES
hit_by_a_magnet = 0
touch_boss = 0
boss_dead = 0

# NEWLY ADDED STUFF
shield_countdown = 0
shield_active_timer = 0

######################################################
#   NEXT MAJOR CHANGE GLOBAL VARIABLES
######################################################

# FRAME REFRESHING
FPS = 20
FRAME_TIME = 1/FPS

# COUNT OF FRAME REFRESHES
COUNT = 0

# WHEN TO MOVE SCREEN
TO_SHIFT_SCREEN_TIME = 0.2  # put difficulty levels
TO_SHIFT_SCREEN = TO_SHIFT_SCREEN_TIME / FRAME_TIME

# TOTAL TIME THINGS
TOTAL_TIME = enemy_comes_after*2*screen_length*TO_SHIFT_SCREEN_TIME
MAXIMUM_NO = TOTAL_TIME / FRAME_TIME
REMAINING_NO = MAXIMUM_NO - COUNT

# POWER UPS
MAX_SHIELD_ACTIVE_TIME = 10  # 10 seconds active
MAX_SHIELD_COOLDOWN_TIME = 60  # 60 seconds cooldown
MAX_SPEED_ACTIVE_TIME = 30  # 30 seconds active, personal choice
MAX_SHIELD_ACTIVE = MAX_SHIELD_ACTIVE_TIME / FRAME_TIME
MAX_SHIELD_COOLDOWN = MAX_SHIELD_COOLDOWN_TIME / FRAME_TIME
MAX_SPEED_ACTIVE = MAX_SPEED_ACTIVE_TIME / FRAME_TIME

# GRAVITY
GRAVITY_TIME_START = TO_SHIFT_SCREEN*4
GRAVITY_STEP = 1

# BULLETS RESTORATION
BULLETS_RESTORATION_TIME = 2  # 2 seconds per bullet to restore
BULLETS_RESTORATION = BULLETS_RESTORATION_TIME/FRAME_TIME

# SCORES
SCORE = 0
COINS = 0
BEAMS = 0

# SNAKE DESIGNS
snake_generator = [
    [' ', ' ', ' ', ' ', '.', '-', '-', '-', ',', ' '],
    ['-', '-', '-', '/', ' ', ' ', ' ', ' ', ' ', '\\']
]
hero = [['▄', '['], ['|', '|']]
