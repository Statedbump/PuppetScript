from _testcapi import raise_exception

import ply.yacc as yacc


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
    'Movement : ID EQUALS move COMA ID EQUALS move COMA ID EQUALS move'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] + s[10] + s[11]


def move(s):
    '''move : Horizontal
    | None
    | Vertical'''
    s[0] = s[1]


def speed_Id(s):
    'SpeedId : ID EQUALS INT'
    s[0] = s[1] + s[2] + s[3]


def rigid_script(s):
    'RigidBody : SpeedId COMA RigidBodyId COMA Movement COMA ForceMode COMA Action'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9]


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


def keys(s):
    '''Key : KEY_ESC
          | KEY_F1
          | KEY_F2
          | KEY_F3
          | KEY_F4
          | KEY_F5
          | KEY_F6
          | KEY_F7
          | KEY_F8
          | KEY_F9
          | KEY_F10
          | KEY_F11
          | KEY_F12
          | KEY_1
          | KEY_2
          | KEY_3
          | KEY_4
          | KEY_5
          | KEY_6
          | KEY_7
          | KEY_8
          | KEY_9
          | KEY_0
          | KEY_A
          | KEY_B
          | KEY_C
          | KEY_D
          | KEY_E
          | KEY_F
          | KEY_G
          | KEY_H
          | KEY_I
          | KEY_J
          | KEY_K
          | KEY_L
          | KEY_M
          | KEY_N
          | KEY_O
          | KEY_P
          | KEY_Q
          | KEY_R
          | KEY_S
          | KEY_T
          | KEY_U
          | KEY_V
          | KEY_W
          | KEY_X
          | KEY_Y
          | KEY_Z
          | KEY_NUMLOCK
          | KEY_NUMPAD
          | KEY_NUMPAD2
          | KEY_NUMPAD3
          | KEY_NUMPAD4
          | KEY_NUMPAD5
          | KEY_NUMPAD6
          | KEY_NUMPAD7
          | KEY_NUMPAD8
          | KEY_NUMPAD9
          | KEY_NUMPAD_DIVIDE
          | KEY_NUMPAD_MULTIPLY
          | KEY_NUMPAD_SUBTRACT
          | KEY_NUMPAD_ADD
          | KEY_NUMPAD_ENTER
          | KEY_NUMPAD_DECIMAL
          | KEY_PRINTSCREEN
          | KEY_SCROLL
          | KEY_PAUSE
          | KEY_INSERT
          | KEY_HOME
          | KEY_PAGEUP
          | KEY_DELETE
          | KEY_END
          | KEY_PAGEDOWN
          | KEY_UP
          | KEY_LEFT
          | KEY_DOWN
          | KEY_RIGHT
          | KEY_TAB
          | KEY_CAPSLOCK
          | KEY_BACKSPACE
          | KEY_ENTER
          | KEY_LCTRL
          | KEY_LWIN
          | KEY_LALT
          | KEY_SPACE
          | KEY_RALT
          | KEY_FN
          | KEY_RMENU
          | KEY_RCTRL
          | KEY_LSHIFT
          | KEY_RSHIFT
          | KEY_MACRO1
          | KEY_MACRO2
          | KEY_MACRO3
          | KEY_MACRO4
          | KEY_MACRO5
          | KEY_OEM_1
          | KEY_OEM_2
          | KEY_OEM_3
          | KEY_OEM_4
          | KEY_OEM_5
          | KEY_OEM_6
          | KEY_OEM_7
          | KEY_OEM_8
          | KEY_OEM_9
          | KEY_OEM_10
          | KEY_OEM_11
          | KEY_EUR_1
          | KEY_EUR_2
          | KEY_JPN_1
          | KEY_JPN_2
          | KEY_JPN_3
          | KEY_JPN_4
          | KEY_JPN_5
          | KEY_KOR_1
          | KEY_KOR_2
          | KEY_KOR_3
          | KEY_KOR_4
          | KEY_KOR_5
          | KEY_KOR_6
          | KEY_KOR_7'''
    s[0] = s[1]


def jump(s):
    '''Jump : Key
            | Key Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def dash(s):
    '''Dash : Key
            | Key Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def jetpack(s):
    '''JetPack : Key
            | Key Action'''
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
