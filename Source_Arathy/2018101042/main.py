import global_stuff
import inputs
import term
import gameboard
import time
from person import person
from hero import hero
from coins import coins
from full_board import full_board
from enemy import enemy
from bullet import bullet
from snake import snake

if __name__ == '__main__':

    term.clrscr()  # clear the screen

    # SCREEN 1
    print('THE MANDALORIAN : THE GAME')
    print()
    global_stuff.username = input('Enter your name: ')
    print()
    print('SELECT DIFFICULTY')
    print("1- TA mode: Completely chill, slow gameplay, not much complicated, easy to win")
    print("2- Challenger: Fast with not many lives; best of luck if you survive")
    print("3- Practice: Check your skills with the end dragon")
    difficulty = int(input('Enter difficulty: '))
    term.setup(difficulty)

    # SET UP THE INPUT
    keys = inputs.NBInput()
    keys.nbTerm()
    keys.flush()

    # MAKE THE BOARDS, HERO AND THE ENEMY
    fb = full_board(global_stuff.screen_height,
                    global_stuff.screen_length)  # full board
    fb.prepare_board()
    board = gameboard.gameboard(
        global_stuff.screen_height, global_stuff.screen_length)  # Partial board displayed on the screen
    # Write to the partial board on the screen
    board.write_full_on_board(fb, 0)
    h = hero()  # Hero
    e = enemy()  # Enemy

    # MAKE THE ENEMY COME IN THE 1st SCREEN IF IN TESTING MODE
    global_stuff.homework()
    if(global_stuff.test_enemy == 1):
        global_stuff.enemy_come = 1

    # BULLETS
    bullet_list = [bullet() for _ in range(10)]
    for i in range(global_stuff.bullets_left):
        bullet_list[i].make_deployable()
    if(global_stuff.debug == 1):
        print('Game starts at '+str(global_stuff.game_start_time))

    # TIME MANAGEMENT
    global_stuff.game_start_time = time.time()  # get the start time of the game

    # INITIALISE THE LOCAL COUNTERS USED
    gravity_ok = 0
    restore_bullet = 0

    # OTHER LOCAL GAME VARIABLES
    isdead = 'Alive'
    gravity_counter = 0

    # COUNT
    global_stuff.COUNT = 0
    global_stuff.REMAINING_NO = global_stuff.MAXIMUM_NO
    down_move = -1
    last_left_shift_count = 0

    # SNEK CHECK
    if(global_stuff.snek == 1):
        (hx, hy) = h.get_coord()
        h = snake(hx, hy)

    # GAME LOOP
    while(1):
        # INCREASE THE COUNT AND DECREASE THE REMAINING NO
        global_stuff.COUNT += 1
        global_stuff.REMAINING_NO -= 1
        last_left_shift_count += 1

        # DISPLAY THE BOARD, HERO, BULLETS AND ENEMY(if applicable)
        term.next_play()
        board.print(h, e)
        h.print_direct()
        if(global_stuff.enemy_come == 1):
            e.print_direct()
            e.follow(h)  # make the enemy follow our hero
            e.check_collision(board, h)

        # IF IN DEBUG MODE, DISPLAY THE FOLLOWING
        if(global_stuff.debug == 1):
            #  THE SCREEN COLUMN THAT WILL BE DISPLAYED NEXT
            print(global_stuff.shown_until)
            #  WHETHER THE MAGNET IS ON THE SCREEN
            if(board.is_magnet_on_screen() != 'NOT ON SCREEN'):
                print('YES MAGNET ON SCREEN')

        # POLL FOR THE INPUT EVERY FRAME CYCLE
        if keys.kbHit():

            # GET THE INPUT AND STORE IT IN A VARIABLE
            control_pressed = keys.getCh()
            if(control_pressed == 'w'):
                gravity_counter = 1
                last_pressed_up = 0
                down_move = global_stuff.GRAVITY_TIME_START
            if(global_stuff.debug == 1):
                print(h.get_coord(), control_pressed)

            # MOVE THE HERO AND CHECK FOR HIS COLLISIONS WITH BOTH THE ENEMY AND THE BOARD OBSTACLES
            h.move(control_pressed)
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  # make the enemy follow our hero
                e.check_collision(board, h)

            # SHOOT BULLETS BY THE HERO
            if(global_stuff.snek == 0 and control_pressed == 'x'):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].deploy(h) == 1):
                        break

            # SHIELD ACTIVATE
            if(control_pressed == ' '):
                if(h.is_shield() == 0 and global_stuff.shield_countdown == 0):
                    # global_stuff.shield_countdown = global_stuff.shield_total_countdown
                    global_stuff.shield_active_timer = global_stuff.MAX_SHIELD_ACTIVE_TIME
                    h.shield_self()

            # QUIT THE GAME
            elif(control_pressed == 'q'):
                break

            # RESET IT ALL
            control_pressed = None

        # MOVE THE BOARD BACKWARDS EVERY FEW 100s OF MILLISECONDS
        # if(global_stuff.COUNT % global_stuff.TO_SHIFT_SCREEN==0):
        if(last_left_shift_count-global_stuff.TO_SHIFT_SCREEN >= 0):
            last_left_shift_count = 0

            # SHIFT THE BOARD
            if(global_stuff.debug == 1):
                print('SHIFTING EVERYTHING')
            for i in range(global_stuff.total_bullets):
                bullet_list[i].move_right(board)
            board.shift_right(fb, global_stuff.shown_until)
            global_stuff.shown_until += 1

            # CHECK WHETHER ENEMY SHOULD COME
            if(global_stuff.shown_until >= global_stuff.enemy_comes_after*global_stuff.screen_length):
                global_stuff.enemy_come = 1

            # MANAGE ALL COLLISIONS
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  # make the enemy follow our hero
                e.check_collision(board, h)

            # ENEMY DOING STUFF ;p
            if(global_stuff.enemy_come == 1):  # add condition later for checking if there is an enemy hero
                e.release_balls()
                e.move_balls(board, h)
                e.check_collision(board, h)

            # SNAKEY STUFF
            if(global_stuff.snek==1):
                h.move_balls(board)

            # MOVE THE HERO DEPENDING ON THE POSITION OF THE MAGNET
            h.magnet_attraction(board)

        # GRAVITY MANAGEMENT WOULD BE DIFFERENT
        gravity_counter += 1
        if(gravity_counter % down_move == 0):
            # GRAVITY
            down_move -= global_stuff.GRAVITY_STEP
            if(down_move <= 0):
                down_move = 1
            gravity_counter = 1
            h.move('down')
            gravity_ok = 0
            # check for collisions
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  # make the enemy follow our hero
                e.check_collision(board, h)

        if(global_stuff.COUNT % global_stuff.BULLETS_RESTORATION == 0):
            # RESTORE BULLETS ONCE EVERY 5 SHIFTS
            for i in range(global_stuff.total_bullets):
                if(bullet_list[i].check_if_deployable() == 0 and bullet_list[i].check_if_exist() == 0):
                    bullet_list[i].make_deployable()
                    global_stuff.bullets_left += 1
                    break
            if(global_stuff.bullets_left > global_stuff.total_bullets):
                global_stuff.bullets_left = global_stuff.total_bullets

        # POWER-UP RUN OUT CHECK

        # SHIELD POWER-UP
        if(h.is_shield() == 1):
            global_stuff.shield_active_timer -= 1
            if(global_stuff.shield_active_timer <= 0):
                h.unshield_self()
        else:
            # SHIELD RESTORATION
            if(global_stuff.shield_countdown > 0):
                global_stuff.shield_countdown -= 1

        # SPEED POWER UP
        if(global_stuff.speeded == 1):
            global_stuff.speeded_active_timer -= 1
            if(global_stuff.speeded_active_timer < 0):
                global_stuff.speeded_active_timer = -1
                global_stuff.speeded = 0
                global_stuff.TO_SHIFT_SCREEN = global_stuff.TO_SHIFT_SCREEN * 2

        # CHECK IF THE GAME IS OVER
        isdead = h.check_if_dead()
        if(isdead != '' and isdead != 'Alive'):
            break
        # SNAKE DEAD CHECK
        if(global_stuff.trigger == 1):
            global_stuff.trigger = 0
            h = hero()
        # SNAKE COLLECTED CHECK
        if(global_stuff.snake_collected == 1):
            global_stuff.snake_collected = 0
            global_stuff.snek = 1
            (hx, hy) = h.get_coord()
            h = snake(hx, hy)

        # DEFINE THE FRAME RATE
        time.sleep(global_stuff.FRAME_TIME)

    # THE LAST GAME OVER SCREEN
    term.clrscr()
    if(isdead in ['', 'Alive']):
        print("GAME OVER")
        print()
        print("WHY DID YOU QUIT ", global_stuff.username, "?")
        print("Baby Yoda still needs your help")
        print()
    elif(isdead == "Boss Dead"):
        print("CONGRATULATIONS ", global_stuff.username)
        print()
        print(
            "Baby Yoda has been successfully rescued and the evil dragon has been killed.")
        print(
            "The developer likes you for playing this game (please rate/mark it with love)")
        print()
    elif(isdead == "Death by Magnet"):
        print("GAME OVER")
        print()
        print("Don't you know that touching a magnet in that full iron suit can kill you with its really strong attractive force ",
              global_stuff.username, "?")
        print("But don't give up!")
        print("Baby Yoda still needs your help")
        print()
    elif(isdead == "No Lives Remaining"):
        print("GAME OVER")
        print()
        print("You have died. You had been electrocuted way too many times by beams and frozen many more times by ice balls..")
        print("But don't give up!")
        print("Baby Yoda still needs your help")
        print()
    elif(isdead == "Time out"):
        print("GAME OVER")
        print()
        print("You ran out of precious time. Baby Yoda has now been slaughtered by the dragon, as you were too slow.")
        print("But don't give up!")
        print("Zombie Baby Yoda still needs your help! Try again!")
        print()
    elif(isdead == "Touched Boss"):
        print("GAME OVER")
        print()
        print("Oh dear, you thought you can fight the dragon with your bare hands(without using the bullet). Sadly, the dragon has annihilated you..")
        print("But don't give up!")
        print("Baby Yoda still needs your help")
        print()

    print('STATISTICS')

    print('Score: '+str(global_stuff.score))
    print('Time left: '+str(global_stuff.REMAINING_NO*global_stuff.FRAME_TIME))
