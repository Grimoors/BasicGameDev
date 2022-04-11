
class beam(obstacle):
    def __init__(self, xpos, ypos, orientation):
        if(orientation == 'h'):
            k = np.full((2*safe_region+1, length_of_beam+2*safe_region), ' ')
            k[safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+length_of_beam-1):
                k[safe_region][i] = '-'
            k[safe_region][safe_region+length_of_beam-1] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, 2*safe_region+1,
                             length_of_beam+2*safe_region, sh, 'Hbeam')
        elif(orientation == 'v'):
            k = np.full((int(length_of_beam/2)+2 *
                         safe_region, 2*safe_region+1), ' ')
            k[safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+int(length_of_beam/2)-1):
                k[i][safe_region] = '|'
            k[safe_region+int(length_of_beam/2)-1][safe_region] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, int(length_of_beam/2) +
                             2*safe_region, 2*safe_region+1, sh, 'Vbeam')
        elif(orientation == 'd1'):
            k = np.full((int(length_of_beam/1.5)+2*safe_region,
                         int(length_of_beam/1.5)+2*safe_region), ' ')
            k[safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+int(length_of_beam/1.5)-1):
                k[i][i] = '\\'
            k[safe_region+int(length_of_beam/1.5) -
              1][safe_region+int(length_of_beam/1.5)-1] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, int(length_of_beam/1.5)+2*safe_region,
                             int(length_of_beam/1.5)+2*safe_region, sh, 'Dbeam1')
        elif(orientation == 'd2'):
            k = np.full((int(length_of_beam/1.5)+2*safe_region,
                         int(length_of_beam/1.5)+2*safe_region), ' ')
            k[safe_region+int(length_of_beam/1.5)-1 -
              safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+int(length_of_beam/1.5)-1):
                k[safe_region+int(length_of_beam/1.5)-1-i][i] = '/'
            k[safe_region+int(length_of_beam/1.5)-1-safe_region-int(
                length_of_beam/1.5)+1][safe_region+int(length_of_beam/1.5)-1] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, int(length_of_beam/1.5)+2*safe_region,
                             int(length_of_beam/1.5)+2*safe_region, sh, 'Dbeam2')
class bullet(obstacle):
    def __init__(self):
        super().__init__(0, 0, 1, 2, [['≡', '>']], 'Bullet')
        self.__exist = 0
        self.__deployable = 0
    def check_if_exist(self):
        return self.__exist
    def check_if_deployable(self):
        return self.__deployable
    def make_deployable(self):
        self.__deployable = 1
    def delete_from_board(self):
        self.__exist = 0
    def move_right(self, board):
        if(self.check_if_exist() == 1):
            is_magnet = 0
            try:
                for i in range(-1, 4):
                    what_is_destroyed = board.destroy_object(
                        self._x, self._y+i)
                    if(what_is_destroyed == 'Coin'):
                        global_stuff.score += 5
                    elif what_is_destroyed in ['Hbeam', 'Vbeam', 'Dbeam1', 'Dbeam2']:
                        global_stuff.score += 20
                        self.delete_from_board()
                    elif(what_is_destroyed == 'Magnet'):
                        self.delete_from_board()
                        is_magnet = 1
            except:
                pass
            try:
                board.board[self._x][self._y][0] = ' '
                board.board[self._x][self._y][1] = 'Normal'
                if(is_magnet == 0):
                    board.board[self._x][self._y+1][0] = ' '
                    board.board[self._x][self._y+1][1] = 'Normal'
                board.board[self._x][self._y-1][0] = ' '
                board.board[self._x][self._y-1][1] = 'Normal'
                self._y += 2
                if(self._y+1 >= global_stuff.screen_length):
                    self.delete_from_board()
                elif(self.check_if_exist() == 1):
                    self.write_self_on_board(board)
                    if(global_stuff.debug == 1):
                        print('BULLET', self._x, self._y)
            except Exception as e:
                print(e)
                self.delete_from_board()
    def deploy(self, hero):
        if(self.check_if_deployable() == 0):
            return 0
        else:
            try:
                (self._x, self._y) = hero.get_coord()
                self._y += 4
                self.__exist = 1
                self.__deployable = 0
                global_stuff.bullets_left -= 1
                return 1
            except Exception as e:
                print(e)
                return 0
    def display(self, board):
        if(self.check_if_exist() == 1):
            self.write_self_on_board(board)
class coins(obstacle):
    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos, 1, 1, ['0'], 'Coin')
    def collect(self, board):
        super().destroy_self(board)
        global_stuff.coins_collected += 1
        global_stuff.score += 10
COLORS = {
    'Normal': '\x1b[40;37m',
    'Bg1': '\x1b[40;37m',
    'Bg2': '\x1b[40;100m',
    'Bg3': '\x1b[40;47m',
    'Top Bar': '\x1b[1;97;44m',
    'Bottom Bar': '\x1b[1;97;44m',
    'Life': '\x1b[31;1;100m',
    'Time': '\x1b[32;1;100m',
    'Progress': '\x1b[1;100m',
    'Hero': '\x1b[1;36;47m',
    'ShieldedHero': '\x1b[1;32;47m',
    'SpeededHero': '\x1b[1;35;47m',
    'Bullet': '\x1b[38;5;208m',
    'Hbeam': '\x1b[1;31;40m',
    'Vbeam': '\x1b[1;31;40m',
    'Dbeam1': '\x1b[1;31;40m',
    'Dbeam2': '\x1b[1;31;40m',
    'Enemy': '\x1b[1;31;40m',
    'Ice Ball': '\x1b[1;36;40m',
    'Coin': '\x1b[1;33;40m',
    'ExtraLife': '\x1b[41;1;37m',
    'ShieldPU': '\x1b[46;1;37m',
    'SpeedBoost': '\x1b[42;5;37m',
    'Snek': '\x1b[0;37;42m',
    'Magnet': ''
}
END_COLOR = '\033[m'
def color_text(text, color):
    if '\x1b' in color:
        return color + text + END_COLOR
    else:
        try:
            return COLORS[color] + text + END_COLOR
        except:
            return text
class enemy(person):
    def __init__(self):
        super().__init__(2, global_stuff.screen_length-2,
                         5, 13, global_stuff.enemy_style_1, 'Enemy')
        self._state = 0
        self.ball = ball()
    def print_direct(self):
         if(self._state == 0):
            self._style = global_stuff.enemy_style_1
        elif(self._state == 1):
            self._style = global_stuff.enemy_style_2
        elif(self._state == 'DEAD'):
            self._style = global_stuff.enemy_style_dead
        super().print_direct()
        if(self.ball.check_if_exists() == 1):
            self.ball.print_direct()
    def follow(self, h):
        (hx, _) = h.get_coord()
        if(global_stuff.debug == 1):
            print('Following ', hx, self._x, global_stuff.screen_height-5-3)
        if(hx > self._x):
            if(self._x <= global_stuff.screen_height-9):
                super().move('down')
        elif(hx < self._x):
            super().move('up')
    def release_balls(self):
        if(self.ball.check_if_exists() == 0):
            p = random.randint(0, 4)
            self.ball.deploy(self._x+p, self._y)
    def move_balls(self, board, hero):
        self.ball.move_left(board, hero)
    def check_collision(self, board, h):
        (hx, hy) = h.get_coord()
        (hh, hw) = h.get_dim()
        for i in range(self._h):
            for j in range(self._w):
                for k in range(hh):
                    for l in range(hw):
                        if((self._x+i, self._y-j) == (hx+k, hy-l)):
                            global_stuff.touch_boss = 1  
                            return
        bullet_accounted = 0
        for i in range(self._h):
            if(bullet_accounted == 1):
                break
            for j in range(self._w):
                if(board.board[self._x+i][self._y-j][1] == 'Bullet'):
                    global_stuff.boss_life_remaining -= 1
                    bullet_accounted = 1
                    break
        self.ball.check_collision(board, h)
class full_board():
    def __init__(self, rows, columns):
        self.__rows = rows-5
        self.__columns = columns*global_stuff.total_no_screens
        self.board = np.full((self.__rows, self.__columns, 2),
                             ' '*global_stuff.total_no_screens)
    def getrows(self):
        return self.__rows
    def generate_background(self):
        for i in range(self.__rows):
            for j in range(global_stuff.screen_length*global_stuff.enemy_comes_after):
                self.board[i][j][0] = ' '
                prob = random.random()
                if(prob > 0.9):
                    self.board[i][j][1] = 'Bg2'
                else:
                    self.board[i][j][1] = 'Bg1'
        for i in range(self.__rows):
            for j in range(global_stuff.screen_length*global_stuff.enemy_comes_after, self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Normal'
    def check_if_permissible(self, X, Y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if self.board[X+i][Y+j][1] not in ['Normal', 'Bg1', 'Bg2']:
                        if(global_stuff.debug == 1):
                            print(self.board[X+i][Y+j][1])
                        return 0
                except:
                    continue
        return 1
    def put_coins_block(self, screen_no):
        h = random.randint(2, 7)
        w = random.randint(10, 30)
        xpos = random.randint(3, self.__rows-2)  
        ypos = random.randint(int((screen_no-1)*global_stuff.screen_length),
                              int(screen_no*global_stuff.screen_length))  
        if(global_stuff.debug == 1):
            print(ypos)
            getch.getch()
        for i in range(h):
            for j in range(w):
                c = coins(xpos+i, ypos+j)
                try:
                    c.write_self_on_board(self)
                except:
                    continue
    def put_beam_block(self, ty, screen_no):
        attempt = 0
        while (attempt <= 100):
            try:
                if(ty == 'h'):
                    xpos = random.randint(2, self.__rows-4)
                elif(ty in ['d1', 'd2', 'v']):
                    xpos = random.randint(
                        2, self.__rows-int(global_stuff.length_of_beam/2)+2*global_stuff.safe_region-3)
                ypos = random.randint(int((screen_no-1)*global_stuff.screen_length), int(
                    screen_no*global_stuff.screen_length))
                beami = beam(xpos, ypos, ty)
                ifp = 1
                for I in range(beami._h):
                    for J in range(beami._w):
                        if(self.check_if_permissible(xpos+I, ypos+J) == 0):
                            ifp = 0
                            break
                    if(ifp == 0):
                        break
                if(ifp == 1):
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                        getch.getch()
                    beami.write_self_on_board(self)
                    return
                else:
                    attempt += 1
            except:
                if(global_stuff.debug == 1):
                    print('Error')
                    getch.getch()
                attempt += 1
    def put_powerup(self, ty, screen_no):
        attempt = 0
        while (attempt <= 100):
            try:
                xpos = random.randint(5, self.__rows-5)
                ypos = random.randint(int((screen_no-1)*global_stuff.screen_length), int(
                    screen_no*global_stuff.screen_length))
                pu = powerup(xpos, ypos, ty)
                if(self.check_if_permissible(xpos, ypos) != 0):
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                        getch.getch()
                    pu.write_self_on_board(self)
                    return
                else:
                    attempt += 1
            except:
                if(global_stuff.debug == 1):
                    print('Error')
                    getch.getch()
                attempt += 1
    def randomly_add_coins_everywhere(self):
        if(global_stuff.debug == 1):
            print('Generating coins...')
        for _ in range(2):
            
            self.put_coins_block(1)
        for screen in range(2, 10):  
            for _ in range(4):  
                
                self.put_coins_block(screen)
    def randomly_add_beams(self):
        for typ in ['h', 'v', 'd1', 'd2']:
            if(global_stuff.debug == 1):
                print('Generating '+typ+' beams....')
            for i in range(1, 5):
                for _ in range(2):
                    self.put_beam_block(typ, i+0.5)
    def randomly_add_powerups(self):
        if(global_stuff.debug == 1):
            print('Generating extra life powerups...')
        for screen in range(1, 10):
            self.put_powerup('ExtraLife', screen)
        if(global_stuff.debug == 1):
            print('Generating Speed Up powerups...')
        for screen in range(1, 5):
            self.put_powerup('SpeedBoost', screen)
        if(global_stuff.debug == 1):
            print('Generating Shield powerups...')
        for screen in range(1, 5):
            for _ in range(2):
                self.put_powerup('ShieldPU', screen)
        if(global_stuff.debug == 1):
            print('Generating Snake powerups...')
        for screen in range(1, 2):
            self.put_powerup('Snek', screen+0.5)
    def add_magnet(self):
        if(global_stuff.debug == 1):
            print('Generating magnet...')
        if(global_stuff.powerUpTesting == 1):
            kdd = 0
        else:
            kdd = 3
        while(True):
            xpos = random.randint(3, 4)
            ypos = random.randint(
                (kdd-1)*global_stuff.screen_length, kdd*global_stuff.screen_length)
            m = magnet(xpos, ypos)
            try:
                ok = 1
                for i in range(m._h):
                    for j in range(m._w):
                        if(self.check_if_permissible(xpos+i, ypos+j) == 0):
                            ok = 0
                            if(global_stuff.debug == 1):
                                print('Not ok at ', xpos+i, ypos+j)
                            break
                    if(ok == 0):
                        break
                if(ok == 1):
                    m.write_self_on_board(self)
                    global_stuff.magnet_y_pos_fullboard = ypos
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                        getch.getch()
                    return
                else:
                    if(global_stuff.debug == 1):
                        print('occupied', xpos, ypos)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue
    def prepare_board(self):
        self.generate_background()
        self.randomly_add_coins_everywhere()
        self.randomly_add_beams()
        self.randomly_add_powerups()
        self.add_magnet()
class gameboard:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.board = np.full((rows, columns, 2), ' '*10)
        for i in range(0, 2):
            for j in range(self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Top Bar'
        for i in range(2, self.__rows-3):
            for j in range(self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Normal'
        for i in range(self.__rows-3, self.__rows):
            for j in range(self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Bottom Bar'
        self.gamename_display()
    def gamename_display(self):
        gamename = 'THE MANDALORIAN: THE GAME'
        leng = len(gamename)
        startat = 2
        for i in range(leng):
            self.board[0][i+startat][0] = gamename[i]
    def score_update(self):
        scorename = 'SCORE: '+str(global_stuff.score).rjust(10, '0')
        leng = len(scorename)
        startat = self.__columns-2-leng
        for i in range(leng):
            self.board[0][i+startat][0] = scorename[i]
    def coins_collected_update(self):
        scorename = 'COINS COLLECTED:   ' + \
            str(global_stuff.coins_collected).rjust(5, ' ')
        leng = len(scorename)
        startat = int(self.__columns/2)+5
        for i in range(leng):
            self.board[self.__rows-1][i+startat][0] = scorename[i]
    def life_display(self):
        lf = 'LIFE:     '
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-3][i][0] = lf[i]
        percentage_to_fill = global_stuff.lives_remaining/global_stuff.total_life
        totwid = int(self.__columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-3][i+leng][0] = k[i]
            self.board[self.__rows-3][i+leng][1] = 'Life'
    def time_display(self):
        lf = 'TIME LEFT:'
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-2][i][0] = lf[i]
        global_stuff.time_left = int(
            global_stuff.total_time+global_stuff.game_start_time-time.time())
        percentage_to_fill = global_stuff.time_left/global_stuff.total_time
        totwid = int(self.__columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-2][i+leng][0] = k[i]
            self.board[self.__rows-2][i+leng][1] = 'Time'
    def game_progress_display(self):
        
        lf = 'PROGRESS: '
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-1][i][0] = lf[i] 
        progress = global_stuff.shown_until-global_stuff.screen_length
        percentage_to_fill = progress / \
            ((global_stuff.enemy_comes_after-1)*global_stuff.screen_length)
        if(percentage_to_fill >= 1):
            percentage_to_fill = 1
        totwid = int(self.__columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-1][i+leng][0] = k[i]  
            self.board[self.__rows-1][i+leng][1] = 'Progress'
    def bullets_display(self):
        lf = 'BULLETS LEFT:      '
        k = ''
        for _ in range(global_stuff.bullets_left):
            k += '> '
        for _ in range(global_stuff.bullets_left, global_stuff.total_bullets):
            k += '  '
        lf += k
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-3][i +
                                      int(global_stuff.screen_length/2)+5][0] = lf[i]
    def display_powerups_active(self):
        l = 'POWERUPS ACTIVE:   '
        leng = len(l)
        i = int(global_stuff.screen_length/2)+5
        for j in range(leng):
            self.board[self.__rows-2][i][0] = l[j]
            i += 1
        if(global_stuff.snek == 1):
            p = powerup(self.__rows-2, i, 'Snek')
            p.write_self_on_board(self)
        else:
            self.board[self.__rows-2][i][0] = ' '
            self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        self.board[self.__rows-2][i][0] = ' '
        self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        if(global_stuff.shielded == 1):
            p = powerup(self.__rows-2, i, 'ShieldPU')
            p.write_self_on_board(self)
        else:
            self.board[self.__rows-2][i][0] = ' '
            self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        self.board[self.__rows-2][i][0] = ' '
        self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        if(global_stuff.speeded == 1):
            p = powerup(self.__rows-2, i, 'SpeedBoost')
            p.write_self_on_board(self)
        else:
            self.board[self.__rows-2][i][0] = ' '
            self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        self.board[self.__rows-2][i][0] = ' '
        self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
    def print_enemy_life(self):
        lf = 'ENEMY: '
        leng = len(lf)
        for i in range(leng):
            self.board[1][i][0] = lf[i] 
        percentage_to_fill = global_stuff.boss_life_remaining / global_stuff.boss_total_life
        if(percentage_to_fill <= 0):
            global_stuff.boss_dead = 1
        totwid = int(self.__columns-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[1][i+leng][0] = k[i]  
            self.board[1][i+leng][1] = 'Life'
    def prepare_board(self):
        self.score_update()
        self.life_display()
        self.time_display()
        self.bullets_display()
        self.game_progress_display()
        self.display_powerups_active()
        self.coins_collected_update()
    def print(self):
        self.prepare_board()
        if(global_stuff.enemy_come == 1):
            self.print_enemy_life()
        for i in range(self.__rows):
            for j in range(self.__columns):
                print(color_text(self.board[i][j]
                                 [0], self.board[i][j][1]), end='')
            print()
    def write_full_on_board(self, full_board, start_in):
        try:
            for i in range(0, full_board.getrows()):  
                for j in range(0, self.__columns):  
                    self.board[i+2][j] = full_board.board[i][j+start_in]
        except Exception as e:
            print(i, j)
            print(full_board.getrows(), self.__columns)
            print(self.board.shape, full_board.board.shape)
            print(e)
    def shift_right(self, full_board, line_to_add):
        for i in range(full_board.getrows()):
            for j in range(self.__columns-1):
                self.board[i+2][j] = self.board[i+2][j+1]
        for i in range(full_board.getrows()):
            self.board[i+2][self.__columns -
                            1] = full_board.board[i][line_to_add]
    def is_magnet_on_screen(self):
        position = global_stuff.magnet_y_pos_fullboard - \
            global_stuff.shown_until+global_stuff.screen_length
        if(position < global_stuff.screen_length and position >= -7):
            return position
        return 'NOT ON SCREEN'
    def destroy_object(self, X, Y):  
        if(self.board[X][Y][1] == 'Normal' or self.board[X][Y][1] == 'Bg1' or self.board[X][Y][1] == 'Bg2'):
            return 'No collision'
        elif(self.board[X][Y][1] == 'Coin'):
            self.board[X][Y][0] = ' '
            self.board[X][Y][1] = 'Normal'
            return 'Coin'
        elif(self.board[X][Y][1] == 'Hbeam'):  
            try:  
                i = 0
                while (self.board[X][Y+i][1] == 'Hbeam'):
                    self.board[X][Y+i][0] = ' '
                    self.board[X][Y+i][1] = 'Normal'
                    i += 1
            except:
                pass
            try:  
                i = 1
                while (self.board[X][Y-i][1] == 'Hbeam'):
                    self.board[X][Y-i][0] = ' '
                    self.board[X][Y-i][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Hbeam'
        elif (self.board[X][Y][1] == 'Vbeam'): 
            try:  
                i = 0
                while (self.board[X+i][Y][1] == 'Vbeam'):
                    self.board[X+i][Y][0] = ' '
                    self.board[X+i][Y][1] = 'Normal'
                    i += 1
            except:
                pass
            try:  
                i = 1
                while (self.board[X-i][Y][1] == 'Vbeam'):
                    self.board[X-i][Y][0] = ' '
                    self.board[X-i][Y][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Vbeam'
        elif (self.board[X][Y][1] == 'Dbeam1'): 
            try:  
                i = 0
                while (self.board[X+i][Y+i][1] == 'Dbeam1'):
                    self.board[X+i][Y+i][0] = ' '
                    self.board[X+i][Y+i][1] = 'Normal'
                    i += 1
            except:
                pass
            try:  
                i = 1
                while (self.board[X-i][Y-i][1] == 'Dbeam1'):
                    self.board[X-i][Y-i][0] = ' '
                    self.board[X-i][Y-i][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Dbeam1'
        elif(self.board[X][Y][1] == 'Dbeam2'): 
            try: 
                i = 0
                while (self.board[X-i][Y+i][1] == 'Dbeam2'):
                    self.board[X-i][Y+i][0] = ' '
                    self.board[X-i][Y+i][1] = 'Normal'
                    i += 1
            except:
                pass
            try: 
                i = 1
                while (self.board[X+i][Y-i][1] == 'Dbeam2'):
                    self.board[X+i][Y-i][0] = ' '
                    self.board[X+i][Y-i][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Dbeam2'
        elif(self.board[X][Y][1] in ['ExtraLife' , 'ShieldPU' , 'SpeedBoost' , 'Snek']):
            t = self.board[X][Y][1]
            self.board[X][Y][0] = ' '
            self.board[X][Y][1] = 'Normal'
            return t
        elif(self.board[X][Y][1] == 'Magnet'):
            return 'Magnet'
debug = 0
powerUpTesting = 0
test_enemy = 0
username = 'Player'
score = 0
coins_collected = 0
screen_length = 120
screen_height = 30
length_of_beam = 10
safe_region = 1
frame_refresh_time = 0.05
total_life = 10
total_bullets = 10
total_no_screens = 10
enemy_comes_after = 5
boss_total_life = 200
move_left_time = 0.4
total_time = int(min(enemy_comes_after*2*screen_length *
                     move_left_time, total_no_screens*screen_length*move_left_time))
game_start_time = 0
shown_until = screen_length
lives_remaining = total_life
bullets_left = 3  
boss_life_remaining = boss_total_life
enemy_come = 0
magnet_y_pos_fullboard = 0
time_left = total_time
ball_gravity_count = 0
speeded = 0
snek = 0
shielded = 0
shielded_power_up_counter = -1
speeded_power_up_counter = -1
snek_power_up_counter = -1
shield_timer = 100
snake_timer = 50
speed_timer = 100
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
def homework():
    for i in enemy_style_1:
        i = i.reverse()
    for i in enemy_style_2:
        i = i.reverse()
    for i in enemy_style_dead:
        i = i.reverse()
hit_by_a_magnet = 0
touch_boss = 0
boss_dead = 0
def check_if_dead():
    if(hit_by_a_magnet == 1):
        return 'Death by Magnet'
    elif (lives_remaining <= 0):
        return 'No Lives Remaining'
    elif(time_left <= 0):
        return 'Time out'
    elif(touch_boss == 1):
        return 'Touched Boss'
    elif(boss_dead == 1):
        return 'Boss Dead'
    else:
        return 'Alive'
class hero(person):
    def __init__(self):
        super().__init__(global_stuff.screen_height - 5,
                         0, 2, 2, [['▄', '['], ['|', '|']], 'Hero')
    def print_direct(self):
        if(global_stuff.shielded == 1):
            self.change_type('ShieldedHero')
            super().print_direct()
        elif(global_stuff.speeded == 1):
            self.change_type('SpeededHero')
            super().print_direct()
        else:
            self.change_type('Hero')
            super().print_direct()
    def collision_manager(self, board):
        for i in range(self._h):
            for j in range(self._w):
                what_is_destroyed = board.destroy_object(self._x+i, self._y+j)
                if(global_stuff.debug == 1):
                    if(what_is_destroyed != 'No collision'):
                        print(what_is_destroyed)
                
                if(what_is_destroyed == 'Coin'):
                    global_stuff.coins_collected += 1
                    global_stuff.score += 10
                
                elif what_is_destroyed in ['Hbeam', 'Vbeam', 'Dbeam1', 'Dbeam2']:
                    if(global_stuff.shielded == 1):
                        global_stuff.shielded = 0
                        global_stuff.shielded_power_up_counter = -1
                    else:
                        global_stuff.lives_remaining -= 1
                
                elif what_is_destroyed in ['ExtraLife', 'ShieldPU', 'SpeedBoost', 'Snek']:
                    p = powerup(self._x+i, self._y+j, what_is_destroyed)
                    p.collect(board)
                
                elif(what_is_destroyed == 'Magnet'):
                    global_stuff.hit_by_a_magnet = 1
    def magnet_attraction(self, board):
        is_magnet_on_screen = board.is_magnet_on_screen()
        if(is_magnet_on_screen != 'NOT ON SCREEN'):
            if(global_stuff.debug == 1):
                print('Moving the guy close to ', is_magnet_on_screen)
            if(is_magnet_on_screen+4-1 > self._y):
                self.move('right')
            elif(is_magnet_on_screen+4-1 < self._y):
                self.move('left')
            self.collision_manager(board)
class ball(obstacle):
    def __init__(self):
        super().__init__(0, 0, 1, 5, [['·', '░', '▒', '▓', '█']], 'Ice Ball')
        self.__exist = 0
    def check_if_exists(self):
        return self.__exist
    def check_collision(self, board, h):  
        if(self.check_if_exists() == 1):
            try:
                for i in range(0, 5):
                    
                    board.destroy_object(self._x, self._y+i)
                    
                    (hh, hw) = h.get_dim()
                    (hx, hy)=h.get_coord()
                    for k in range(hh):
                        for l in range(hw):
                            if((hx+k, hy-l) == (self._x, self._y+i)):
                                
                                global_stuff.lives_remaining -= 2
                                self.__exist = 0
                                return
            except Exception as e:
                if(global_stuff.debug):
                    print(e)
                pass
    def move_left(self, board, h):
        if(self.check_if_exists() == 1):
            try:
                self.check_collision(board, h)
            except:
                pass
            self._y -= 5
            if(global_stuff.ball_gravity_count==3):
                if(self._x<global_stuff.screen_height-4):
                    self._x+=1
                global_stuff.ball_gravity_count=0      
            else:
                global_stuff.ball_gravity_count+=1
            if(self._y <= 0):
                self.__exist = 0
            try:
                self.check_collision(board, h)
            except:
                pass
    def deploy(self, x, y):
        self._x = x
        self._y = y
        self.__exist = 1
        self.print_direct()
class NBInput:
    def __init__(self):s
        self.old_settings = termios.tcgetattr(sys.stdin)
    def nbTerm(self):
        tty.setcbreak(sys.stdin.fileno())
    def orTerm(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
    def kbHit(self):
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    def getCh(self):
        return sys.stdin.read(1)
    def flush(self):
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
class magnet(obstacle):
    def __init__(self, xpos, ypos):
        k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', '\x1b[1;31m█', '\x1b[1;31m█', '\x1b[1;31m█', '\x1b[1;31m█',
                 '\x1b[1;31m█', '\x1b[1;31m█', '\x1b[1;31m█', ' '],
             [' ', '\x1b[1;31m█', '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;30m░',
                 '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;31m█', ' '],
             [' ', '\x1b[1;31m█', '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;30m░',
                 '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;31m█', ' '],
             [' ', '\x1b[1;37m█', '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;30m░',
                 '\x1b[1;30m░', '\x1b[1;30m░', '\x1b[1;37m█', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        super().__init__(xpos, ypos, 6, 9, k, 'Magnet')
if __name__ == '__main__':
    term.clrscr()  
    print('THE MANDALORIAN : THE GAME')
    print()
    print('Enter your name: ')
    global_stuff.username = input()
    keys = inputs.NBInput()
    keys.nbTerm()
    keys.flush()
    fb = full_board(global_stuff.screen_height,
                    global_stuff.screen_length)  
    fb.prepare_board()
    board = gameboard.gameboard(
        global_stuff.screen_height, global_stuff.screen_length)  
    board.write_full_on_board(fb, 0)
    h = hero()  
    e = enemy()  
    global_stuff.homework()
    if(global_stuff.test_enemy == 1):
        global_stuff.enemy_come = 1
    bullet_list = [bullet() for _ in range(10)]
    for i in range(global_stuff.bullets_left):
        bullet_list[i].make_deployable()
    if(global_stuff.debug == 1):
        print('Game starts at '+str(global_stuff.game_start_time))
    global_stuff.game_start_time = time.time()  
    last_shift_time = global_stuff.game_start_time
    gravity_ok = 0
    restore_bullet = 0
    isdead = 'Alive'
    while(1):
        term.next_play()
        board.print()
        h.print_direct()
        if(global_stuff.enemy_come == 1):
            e.print_direct()
            e.follow(h)  
            e.check_collision(board, h)
        if(global_stuff.debug == 1):
            
            print(global_stuff.shown_until)
            
            if(board.is_magnet_on_screen() != 'NOT ON SCREEN'):
                print('YES MAGNET ON SCREEN')
        if keys.kbHit():
            
            control_pressed = keys.getCh()
            if(global_stuff.debug == 1):
                print(h.get_coord(), control_pressed)
            
            h.move(control_pressed)
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  
                e.check_collision(board, h)
            
            if(control_pressed == ' '):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].deploy(h) == 1):
                        break
            
            elif(control_pressed == 'q'):
                break
            
            control_pressed = None
        if(time.time()-last_shift_time >= global_stuff.move_left_time):
            last_shift_time = time.time()
            
            if(global_stuff.debug == 1):
                print('SHIFTING EVERYTHING')
            for i in range(global_stuff.total_bullets):
                bullet_list[i].move_right(board)
            board.shift_right(fb, global_stuff.shown_until)
            global_stuff.shown_until += 1
            
            if(global_stuff.shown_until >= global_stuff.enemy_comes_after*global_stuff.screen_length):
                global_stuff.enemy_come = 1
            
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  
                e.check_collision(board, h)
            
            if(global_stuff.enemy_come == 1):  
                e.release_balls()
                e.move_balls(board, h)
                e.check_collision(board, h)
            
            h.magnet_attraction(board)
            
            gravity_ok += 1
            if(gravity_ok == 2):  
                h.move('down')
                gravity_ok = 0
                
                h.collision_manager(board)
                if(global_stuff.enemy_come == 1):
                    e.follow(h)  
                    e.check_collision(board, h)
            
            restore_bullet += 1
            if(restore_bullet == 5):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].check_if_deployable() == 0 and bullet_list[i].check_if_exist() == 0):
                        bullet_list[i].make_deployable()
                        global_stuff.bullets_left += 1
                        break
                if(global_stuff.bullets_left > global_stuff.total_bullets):
                    global_stuff.bullets_left = global_stuff.total_bullets
                restore_bullet = 0
            
            
            if(global_stuff.shielded == 1):
                global_stuff.shielded_power_up_counter += 1
                if(global_stuff.shielded_power_up_counter >= global_stuff.shield_timer):
                    global_stuff.shielded_power_up_counter = -1
                    global_stuff.shielded = 0
            
            if(global_stuff.speeded == 1):
                global_stuff.speeded_power_up_counter += 1
                if(global_stuff.speeded_power_up_counter >= global_stuff.speed_timer):
                    global_stuff.speeded_power_up_counter = -1
                    global_stuff.speeded = 0
                    global_stuff.move_left_time *= 2
            
            if(global_stuff.snek == 1):
                global_stuff.snek_power_up_counter += 1
                if(global_stuff.snek_power_up_counter >= global_stuff.snake_timer):
                    global_stuff.snek_power_up_counter = -1
                    global_stuff.snek = 0
        isdead = global_stuff.check_if_dead()
        if(isdead != '' and isdead != 'Alive'):
            break
        time.sleep(global_stuff.frame_refresh_time)
    term.clrscr()
    print('GAME OVER')
    print()
    print('Congratulations '+global_stuff.username)
    print('Score: '+str(global_stuff.score))
    print('Time left: '+str(global_stuff.time_left))
    if(isdead == '' or isdead == 'Alive'):
        print('Baby Yoda still needs your help.. why you quit my friend?')
    else:
        print('Reason of death: '+isdead)
class obj:
    def __init__(self, x, y, h, w, style, ty):
        self._x = x
        self._y = y
        self._h = h
        self._w = w
        self._style = style
        self._type = ty
    def write_self_on_board(self, gameboard):
        for i in range(self._h):
            for j in range(self._w):
                if(self._style[i][j] != ' '):
                    gameboard.board[i+self._x][j +
                                               self._y][0] = self._style[i][j]
                    gameboard.board[i+self._x][j+self._y][1] = self._type
                else:
                    gameboard.board[i+self._x][j+self._y][0] = ' '
                    gameboard.board[i+self._x][j+self._y][1] = 'Normal'
    def print_direct(self):
        print('\033[s')  
        for i in range(self._h):
            for j in range(self._w):
                print('\033['+str(self._x+i+1)+';' +
                      str(self._y-j+2)+'H'+colored_printing.color_text(self._style[i][j], self._type))
        print('\033[u')  
    def destroy_self(self, gameboard):
        for i in range(self._h):
            for j in range(self._w):
                gameboard.board[i+self._x][j+self._y][0] = ' '
                gameboard.board[i+self._x][j+self._y][1] = 'Normal'
    def change_type(self, new_type):
        self._type = new_type
    def get_coord(self):
        return (self._x, self._y)
    def get_dim(self):
        return (self._h, self._w)
class obstacle(obj):
    def __init__(self, xpos, ypos, length, width, shape, style):
        super().__init__(xpos, ypos, length, width, shape, style)
class person(obj):
    def __init__(self, x, y, h, w, style, ty):
        super().__init__(x, y, h, w, style, ty)
    def move(self, direction):
        if direction in ['w', 'up']:
            if(self._x > 2):
                self._x -= 1
        elif direction in ['s', 'down']:
            if(self._x < global_stuff.screen_height-5):
                self._x += 1
        elif direction in ['a', 'left']:
            if(self._y > 0):
                self._y -= 1
        elif direction in ['d', 'right']:
            if(self._y < global_stuff.screen_length-2):
                self._y += 1
        if(global_stuff.debug == 1):
            print(self._x, self._y)
class powerup(obstacle):
    def __init__(self, xpos, ypos, ty):
        self._type = ty
        if(ty == 'ShieldPU'):
            super().__init__(xpos, ypos, 1, 1, '░', 'ShieldPU')
        elif(ty == 'SpeedBoost'):
            super().__init__(xpos, ypos, 1, 1, 'A', 'SpeedBoost')
        elif(ty == 'ExtraLife'):
            super().__init__(xpos, ypos, 1, 1, '+', 'ExtraLife')
        elif(ty == 'Snek'):
            super().__init__(xpos, ypos, 1, 1, '$', 'Snek')
    def collect(self, board):
        if(global_stuff.debug == 1):
            print(self._type)
        super().destroy_self(board)  
        if(self._type == 'ShieldPU'):
            global_stuff.shielded_power_up_counter = 0
            global_stuff.shielded = 1
        elif(self._type == 'SpeedBoost'):
            global_stuff.speeded_power_up_counter = 0
            if(global_stuff.speeded == 0):
                global_stuff.move_left_time /= 2
                global_stuff.speeded = 1
        elif(self._type == 'ExtraLife'):
            global_stuff.lives_remaining += 1
            if(global_stuff.lives_remaining >= global_stuff.total_life):
                global_stuff.lives_remaining = global_stuff.total_life
        elif(self._type == 'Snek'):
            global_stuff.snek = 1
def clrscr():
    sp.call('clear', shell=True)
def next_play():
    print('\033[0;0H', end='')
