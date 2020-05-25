#importing
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window 
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
import random

easy_dic = ['Hi', 'two', 'i', 'a', 'e', 'i', 'o','u', 'it', 'he', 'she', 'm','n', 'o', 'p', 'q', 'r','u', 's', 't', 'bye', 'one', 'to', 'for','its', 'his', 'her', 'me','my', 'any', 'hot', 'coy', 'why', 'who', 'how','fit', 'bit', 'hit', 'bot', 'tot', 'pot', 'rot', 'lol']

medium_dic = ['oka', 'kurniawan', 'is', 'the', 'best!', 'I', 'love', 'python', 'SUTD', 'IS', 'GREAT', 'roses', 'are', 'red', 'violets','are', 'blue', 'I', 'hate', 'you', 'and', 'love', 'hate', 'me', 'too', 'orange', 'is','a','fruit', 'and', 'tiger', 'snow','red','blue', 'green', 'painful', 'thanks','for', 'coming','to', 'my', 'TEDx' ,'what', 'where', 'world'] + easy_dic

hard_dic = ['Chiaroscurist','COVID-19', 'intelligence',  'pneumonoultramicroscopicsilicovolcanoconiosis', ',',':', 'dictionary','operators', 'corona','jewellery','birthday', 'Pronunciation','furries', 'Pharaoh', 'Hippopotomonstrosesquippedaliophobia', 'pizazzes', 'pappox', 'bezazz', 'Supercalifragilisticexpialidocious', 'Methionylglutamin', 'antidisestablishmentarianism', 'floccinaucinihilipilification', 'otorhinolaryngological', 'psychophysicotherapeutics', 'pseudopseudohypoparathyroidism', 'hepaticocholangiogastrostomy']

class SM:
    def __init__(self): 
        self.state = None 
    
    def start(self):  #self is the object instance you created
        self.state = self.start_state #apply the state you created to start
    
    def step(self, inp, disp):
        # step function: moves the state machine to the next state based on the input
        state = self.state 
        
        #look into the state transition diagram to get the next state and the output 
        ns, out = self.get_next_values(state, inp, disp)
        self.state = ns #changes from current state to next state
        return out 
    
    def transduce(self, lst): #help to repeat steps
        final = []
        for inp in lst: 
            final.append(step(inp))
        return final
    
class Typing_sm(SM):
    start_state = 'norm'
    
    def get_next_values(self, state, inp, disp):
        if inp == disp:
            if state =='norm':
                ns = 'norm' 
                output = 'next word'
        else: 
            ns = 'wrong'
            output = 'stop'
        return ns, output 

class menuButtons(Button): 
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)
        self.font_size = 24
        self.background_normal = 'brick_nom-02.png'
        self.background_down = 'brick_down-03.png'


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        with self.canvas:
            self.rectangle = Rectangle (source ='menu-01.png', size = self.size, pos_hint = self.pos)
            self.bind(pos = self.update_rect, size = self.update_rect)
                
        self.layout = BoxLayout(spacing = 300)
        self.layout.pos_hint = {"top":1, "center_y":0.5}
        
        play_btn = menuButtons(text = "START", on_release = self.change_to_lvl, size_hint=(.075, .15),
                pos_hint={'x':.4, 'y':.4})
        self.layout.add_widget(play_btn)
        
        quit_btn = menuButtons(text = "Quit?",  on_release = self.quitApp, size_hint=(.075, .15),
                pos_hint={'x':.4, 'y':.4})
        self.layout.add_widget(quit_btn)
        self.add_widget(self.layout)
        
    def update_rect(self, *args): 
        self.rectangle.pos = self.pos 
        self.rectangle.size = self.size 
    
    def change_to_lvl(self, value):                                                       #why got value???
        #access the Main widget Screen Manager
        self.manager.transition.direction = 'up' 
        # modify the current screen to a different "name"
        self.manager.current = 'lvl'
     
    def quitApp(self,instance):
        App.get_running_app().stop()
        Window.close()
        
life = {'hearts':3}
difficulty = {2:'hard', 1:'medium', 0:'easy', 'choice':0}
dictionaries = {'hard': hard_dic, 'medium':medium_dic, 'easy':easy_dic}

class HeartButtons(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)
        self.size_hint = (0.1,0.1)
        self.background_normal = 'heart-04.png'
        
class LevelScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        with self.canvas:
            self.rectangle = Rectangle (source = 'lvl_5.png', size = self.size, pos_hint = self.pos)
            self.bind(pos = self.update_rect, size = self.update_rect)
        self.layout = FloatLayout()
    
        plus_btn = Button(text = "+", size_hint=(.1, .1),background_normal= '', color = [0,0,0,1],
                pos_hint={'x':.4, 'y':.5}, on_release = self.life_plus)
        minus_btn = Button(text = "-", size_hint=(.1, .1),background_normal= '', color = [0,0,0,1],
                pos_hint={'x':.2, 'y':.5}, on_release = self.life_minus)
        self.layout.add_widget(plus_btn)
        self.layout.add_widget(minus_btn)
               
        self.lifelines = Label(text = 'Lifelines: 0' + str(life['hearts']), font_size = 24, size_hint =(.1,.1), pos_hint = {'x':.3, 'y': .6})
        self.layout.add_widget(self.lifelines)
        
        self.difficulty = 0
        up_btn = Button(text = ">", size_hint=(.1, .1), background_normal= '', color = [0,0,0,1], 
                        pos_hint ={'x':.8, 'y':.5}, on_release = self.difficulty_up)
        down_btn = Button(text = "<", size_hint=(.1, .1),background_normal= '', color = [0,0,0,1],
                pos_hint={'x':.6, 'y':.5}, on_release = self.difficulty_down)                  
        self.layout.add_widget(up_btn)                               
        self.layout.add_widget(down_btn)
        
        self.diff_lvl = Label(text = difficulty[self.difficulty], font_size = 24, size_hint =(.1,.1), pos_hint = {'x':.7, 'y': .6})
        self.layout.add_widget(self.diff_lvl)
                         
        confirm_btn = Button(text = 'confirm', size_hint = (.2,.1), background_normal= '', color = [0,0,0,1], 
                             pos_hint = {'x':.45, 'y': .2}, on_release = self.change_to_game)
        self.layout.add_widget(confirm_btn)                    
                          
        self.add_widget(self.layout)
        
    def update_rect(self, *args): 
        self.rectangle.pos = self.pos 
        self.rectangle.size = self.size 
    
    def life_plus (self, instance): 
        if life['hearts'] < 9: 
            life['hearts'] += 1
        else: 
            life['hearts'] = life['hearts'] 
        self.lifelines.text = 'Lifelines: 0' + str(life['hearts'])
        lives = sm.get_screen('game').life_indicator
        lives.text = 'Lifelines: 0' + str(life['hearts'])
        
    def life_minus (self, instance): 
        if life['hearts'] > 1: 
            life['hearts'] -=1
        else: 
            life['hearts'] = life['hearts']
        self.lifelines.text = 'Lifelines: 0' + str(life['hearts'])
        game_life = sm.get_screen('game').life_indicator
        game_life.text = 'Lives left: 0' + str(life['hearts'])
            
    def difficulty_up (self, instance): 
        self.difficulty +=1
        if self.difficulty >2: 
            self.difficulty= 0 
        elif self.difficulty < 0: 
            self.difficulty = 2
        self.diff_lvl.text = difficulty[self.difficulty]
        difficulty['choice'] = self.difficulty
    
    def difficulty_down (self, instance): 
        self.difficulty -=1
        if self.difficulty >2: 
            self.difficulty= 0 
        elif self.difficulty < 0: 
            self.difficulty = 2
        self.diff_lvl.text = difficulty[self.difficulty]
        difficulty['choice'] = self.difficulty
    
    def change_to_game(self, instance):
        game = sm.get_screen('game')
        game.heartlayout = FloatLayout()
        for i in range(life['hearts']):
            game.hearts = HeartButtons(text = '',pos =(30+ 70*i,500))
            game.heartlayout.add_widget(game.hearts)
        game.add_widget(game.heartlayout)
        game_diff_lvl = sm.get_screen('game').diff_lvl
        game_diff_lvl.text = 'Level: ' + difficulty[difficulty['choice']]
        #access the Main widget Screen Manager
        self.manager.transition.direction = 'left' 
        # modify the current screen to a different "name"
        self.manager.current = 'game'
        
        
class MyInput(TextInput):
    def __init__(self, **kwargs): #**kwargs allows for variable number of agruments (in this case is dictionary)
        super().__init__(**kwargs) #gives parent class of input
        self.font_size = 24
        self.multiline = False
        self.size_hint= (.2, .07)
        self.height=  30

class Countdown(Label): 
    def __init(self, **kwargs): 
        super().__init__(**kwargs)
        self.font_size = 48
    
    time = NumericProperty(60)  # seconds

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(time = 0, duration=self.time)
        self.anim.bind(on_complete = self.finish)
        self.anim.start(self)

    def finish(self, *args):
        if sm.current == 'game':
            total = sm.get_screen('game').total_words
            characters = len(total)
            if difficulty[difficulty['choice']] == 'easy':
                if characters > 80:
                    self.final_win(characters)
                else: 
                    self.final_fail(characters)
            elif difficulty[difficulty['choice']] == 'medium':
                if characters > 100:
                    self.final_win(characters)
                else:
                    self.final_fail(characters)
            elif difficulty[difficulty['choice']] == 'hard':
                if characters > 130:
                    self.final_win(characters)
                else:
                    self.final_fail(characters)
            else: 
                self.final_fail()
        if sm.current == 'fail':
            pass  
        
    def final_win(self, characters):
        win = sm.get_screen('win')
        stat = Label(text = 'you typed ' + str(characters) + ' characters per minute.', size_hint=(.1,.1), pos_hint = {'x':.3, 'y': .5})
        win.layout.add_widget(stat)
        sm.current = 'win'
    
    def final_fail(self, characters): 
        fail = sm.get_screen('fail')
        stat = Label(text = 'you typed ' + str(characters) + ' characters per minute.', size_hint=(.1,.1), pos_hint = {'x':.3, 'y': .5})
        fail.layout.add_widget(stat)
        sm.current = 'fail'
        
    
    def on_time(self, instance, value):
        self.text = str(round(value, 1))    
        
class GamesScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        with self.canvas:
            self.rectangle = Rectangle (source = 'game-06.png', size = self.size, pos_hint = self.pos)
            self.bind(pos = self.update_rect, size = self.update_rect)
#         Window.bind(on_key_up=self._keyup)
        Window.bind(on_key_down=self._keydown)
        
        self.layout= FloatLayout()
        self.sm = Typing_sm()
        self.sm.start()
        
        self.diff_lvl = Label(text = 'Level: ' + difficulty[difficulty['choice']], font_size = 24,size_hint = (.1,.1),pos_hint = {'x':0.1, 'y': 0})
        self.layout.add_widget(self.diff_lvl)
        self.life_indicator = Label(text = 'Lives left: 0' + str(life['hearts']), font_size = 24, size_hint = (.1,.1), pos_hint = {'x':0.1, 'y': 0.9})
        self.layout.add_widget(self.life_indicator)
        self.timer = Countdown(font_size = 48, pos_hint = {'x':0, 'y': 0.1})
        self.layout.add_widget(self.timer)
        self.label = Label(text = 'Start', font_size = 24,size_hint =(.1,.1), pos_hint = {'x':.4, 'y': .75})
        self.layout.add_widget(self.label)
        self.reminder = Label (text = 'DOUBLE CLICK TEXTBOX!!', font_size = 24, pos_hint = {'x':0, 'y': 0.1})
        self.layout.add_widget(self.reminder)
        self.total_words = ''
        self.inp = MyInput(hint_text = "type here", pos_hint = {'x':.4, 'y': .65}, on_double_tap = self.startCountdown)
        self.layout.add_widget(self.inp)
        self.add_widget(self.layout)
      
    def update_rect(self, *args): 
        self.rectangle.pos = self.pos 
        self.rectangle.size = self.size 
    
#     def _keyup(self,*args):
#         print('key up!!', args)

    def startCountdown(self, *args):
        self.layout.remove_widget(self.reminder)
        self.timer.start()
    
    def _keydown(self,*args):
        diff_name = difficulty[difficulty['choice']]
        word_dic = dictionaries[diff_name]
        if self.sm.state == 'norm':
            if args[3] == None and args[1] == 13 and args[2] == 40: #'enter key'
                user = self.inp.text.strip()
                word = self.label.text
                self.sm.step(user, word)
                self.total_words += user
                self.inp.text = ' '
                self.inp.focus = True
                num = random.randrange(0, len(word_dic))
                word = word_dic[num]
                self.label.text = word
        elif self.sm.state == 'wrong' and life['hearts'] > 0:
            #removing hearts
            self.remove_widget(self.heartlayout)
            
            #update lives and state
            life['hearts']-= 1
            self.sm.state = 'norm'
            self.life_indicator.text = 'Lives left: 0' + str(life['hearts'])
            
            #adding hearts
            self.heartlayout = FloatLayout()
            for i in range(life['hearts']): 
                self.hearts = HeartButtons(text = '',pos =(30+ 70*i,500))
                self.heartlayout.add_widget(self.hearts)
            self.add_widget(self.heartlayout)
        if life['hearts'] == 0:
            #access the Main widget Screen Manager
            self.manager.transition.direction = 'up' 
            # modify the current screen to a different "name"
            fail = sm.get_screen('fail')
            characters = str(len(self.total_words))
            stat = Label(text = 'you typed ' + characters + ' characters per minute.', size_hint=(.1,.1), pos_hint = {'x':.3, 'y': .5})
            fail.layout.add_widget(stat)
            self.manager.current = 'fail'
        return True
        
class SuccessScreen(Screen): 
    def __init__ (self, **kwargs): 
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
        
        label = Label(text = 'MISSION SUCCESS', font_size = 48,size_hint =(.2,.2), pos_hint = {'x':.4, 'y': .6})
        self.layout.add_widget(label)
        play_btn = Button(text = "Bye!",  on_release = self.bye, size_hint=(.2, .1), pos_hint = {'x':.4,'y':.3})
        self.layout.add_widget(play_btn)
        self.add_widget(self.layout)
        
    def bye(self, instance):
        App.get_running_app().stop()
        Window.close()       
    
        
class FailureScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = FloatLayout()
        
        label = Label(text = 'MISSION FAILED', font_size = 48,size_hint =(.2,.2), pos_hint = {'x':.4, 'y': .6})
        self.layout.add_widget(label)
        retry_btn = Button(text = "Bye!",  on_release = self.bye, size_hint=(.2, .1), pos_hint = {'x':.4,'y':.3})
        self.layout.add_widget(retry_btn)
        self.add_widget(self.layout)
                      
    def bye(self, instance):
        App.get_running_app().stop()
        Window.close()       
    
    
class TypingGameApp(App):
    def build(self):  #MAIN class application 
        global sm
        sm = ScreenManager()  
        menu = MenuScreen(name = 'menu')
        sm.add_widget(menu)
        lvl = LevelScreen(name = 'lvl')
        sm.add_widget(lvl)
        game = GamesScreen(name = 'game')
        sm.add_widget(game)
        win = SuccessScreen(name = 'win')
        sm.add_widget(win)
        fail = FailureScreen(name = 'fail')
        sm.add_widget(fail)
        sm.current = 'menu'
        return sm #root widget of the App as it is return by the build method
    
TypingGameApp().run()