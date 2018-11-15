from _testcapi import raise_exception

import ply.yacc as yacc
import CodeLexer

tokensList = CodeLexer.tokens

def script_type(s):
    '''script : Simple
                | RigidBody
                | CharacterController'''


def simple_script(s):
    'Simple : SpeedId Movement'

    f = [s[1]]
    f.extend(s[2])
    s[0] = f


def movement_rule(s):
    #First move is in x, followed by y , endind with z
    'Movement : ID EQUALS Direction ID EQUALS Direction  ID EQUALS Direction'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] 


def Direction(s):
    '''Direction : Horizontal
    | NONE
    | Vertical'''
    s[0] = s[1]

#Preguntarle a angel sobre esto para speed id ya q speed es un keyword
def speed_Id(s):
    'SpeedId : ID EQUALS Float'
    s[0] = s[1] + s[2] + s[3]


def rigid_script(s):
    'RigidBody : RIGIDBODY SpeedId  Movement  ForceMode  Action'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] 


def chraracter_controller_script(s):
    'CharacterController : CHARACTERCONTROLLER SpeedId GravityID Movement  ForceMode  Action'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] + s[6]
	
	
	
	
	
def force_mode(s):
    '''ForceMode : Force
                 | Impulse
                 | Acceleration
                 | None'''
    s[0] = s[1]


def action(s):
    '''Action : Jump
              | Dash
              | Jetpack'''
    s[0] = s[1]


def KeyCodes(s):
    '''KeyCode : KeyCode_ESC
         
          | KeyCode_A
          | KeyCode_B
          | KeyCode_C
          | KeyCode_D
          | KeyCode_E
          | KeyCode_F
          | KeyCode_G
          | KeyCode_H
          | KeyCode_I
          | KeyCode_J
          | KeyCode_K
          | KeyCode_L
          | KeyCode_M
          | KeyCode_N
          | KeyCode_O
          | KeyCode_P
          | KeyCode_Q
          | KeyCode_R
          | KeyCode_S
          | KeyCode_T
          | KeyCode_U
          | KeyCode_V
          | KeyCode_W
          | KeyCode_X
          | KeyCode_Y
          | KeyCode_Z
          | KeyCode_NUMLOCK
          | KeyCode_PRINTSCREEN
          | KeyCode_SCROLL
          | KeyCode_PAUSE
          | KeyCode_INSERT
          | KeyCode_HOME
          | KeyCode_PAGEUP
          | KeyCode_DELETE
          | KeyCode_END
          | KeyCode_PAGEDOWN
          | KeyCode_UP
          | KeyCode_LEFT
          | KeyCode_DOWN
          | KeyCode_RIGHT
          | KeyCode_TAB
          | KeyCode_CAPSLOCK
          | KeyCode_BACKSPACE
          | KeyCode_ENTER
          | KeyCode_LCTRL
          | KeyCode_LWIN
          | KeyCode_LALT
          | KeyCode_SPACE
          | KeyCode_RALT
          | KeyCode_FN
          | KeyCode_RMENU
          | KeyCode_RCTRL
          | KeyCode_LSHIFT
          | KeyCode_RSHIFT
'''
    s[0] = s[1]


def jump(s):
    '''Jump :JUMP EQUALS KeyCode
            | JUMP EQUALS KeyCode Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def dash(s):
    '''Dash : DASH EQUALS KeyCode
            | DASH EQUALS KeyCode Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def jetpack(s):
    '''JetPack : JETPACK EQUALS KeyCode
            | JETPACK EQUALS KeyCode Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def error(s):
    print("Syntax error in input")
    # Will not raise a flag


def translate(s):
    try:
        BotifulCode = open(s, 'r')
    except IOError:
        print("Error opening File")
        exit()

    fileScript = BotifulCode.read()

    parser = yacc.yacc()
    res = parser.parse(fileScript)
