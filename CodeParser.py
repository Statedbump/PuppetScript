from _testcapi import raise_exception

import ply.yacc as yacc
import CodeLexer

tokens = CodeLexer.tokens

def p_script_type(s):
    '''script : Simple
                | RigidBody
                | CharacterController'''


def p_simple_script(s):
    'Simple : SIMPLE SpeedId Movement'

    f = [s[1]]
    f.extend(s[2])
    s[0] = f

def p_rigid_script(s):
    'RigidBody : RIGIDBODY SpeedId  Movement  ForceMode  Action'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] 


def p_chraracter_controller_script(s):
    'CharacterController : CHARACTERCONTROLLER SpeedId GravityId Movement  ForceMode  Action'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] + s[6]
	
def p_speed_Id(s):
    'SpeedId : Speed EQUALS Float'
    s[0] = s[1] + s[2] + s[3]
	
def p_gravity_Id(s):
    'GravityId : Gravity EQUALS Float'
    s[0] = s[1] + s[2] + s[3]	
	
	
def p_movement_rule(s):
    #First move is in x, followed by y , endind with z
    'Movement : ID EQUALS Direction ID EQUALS Direction  ID EQUALS Direction'
    s[0] = s[1] + s[2] + s[3] + s[4] + s[5] + s[6] + s[7] + s[8] + s[9] 


def p_Direction(s):
    '''Direction : Horizontal
    | NONE
    | Vertical'''
    s[0] = s[1]
	
	
def p_force_mode(s):
    '''ForceMode : Force
                 | Impulse
                 | Acceleration
                 | NONE'''
    s[0] = s[1]


def p_action(s):
    '''Action : Jump
              | Dash
              | Jetpack'''
    s[0] = s[1]


def p_KeyCode(s):
    '''KeyCode : 
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
          | KeyCode_Backspace
          | KeyCode_Tab
          | KeyCode_SysReq
          | KeyCode_Break
          | KeyCode_CapsLock
          | KeyCode_ScrollLock
          | KeyCode_RightShift
          | KeyCode_LeftShift
          | KeyCode_RightControl
          | KeyCode_RightAlt
          | KeyCode_LeftAlt
          | KeyCode_RightCommand
          | KeyCode_RightApple
          | KeyCode_LeftCommand
          | KeyCode_LeftWindows
          | KeyCode_RightWindows
          | KeyCode_AltGr
          | KeyCode_Help
          | KeyCode_Print
          | KeyCode_Clear
          | KeyCode_Return
          | KeyCode_Pause
          | KeyCode_Escape
          | KeyCode_Space
          | KeyCode_Exclaim
          | KeyCode_DoubleQuote
          | KeyCode_Hash
          | KeyCode_Dollar
		  | KeyCode_Ampersand
		  | KeyCode_Quote
		  | KeyCode_LeftParen
		  | KeyCode_RightParen
		  | KeyCode_Asterisk
		  | KeyCode_Plus
		  | KeyCode_Comma
		  | KeyCode_Minus
		  | KeyCode_Period
		  | KeyCode_Slash
		  | KeyCode_Colon
		  | KeyCode_Semicolon
		  | KeyCode_Less
		  | KeyCode_Equals
		  | KeyCode_Greater
		  | KeyCode_Question
		  | KeyCode_At
		  | KeyCode_LeftBracket
		  | KeyCode_Backslash
		  | KeyCode_RightBracket
		  | KeyCode_Caret
		  | KeyCode_Underscore
		  | KeyCode_BackQuote
		  
'''
    s[0] = s[1]


def p_Jump(s):
    '''Jump : JUMP EQUALS KeyCode
            | JUMP EQUALS KeyCode Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def p_Dash(s):
    '''Dash : DASH EQUALS KeyCode
            | DASH EQUALS KeyCode Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def p_JetPack(s):
    '''JetPack : JETPACK EQUALS KeyCode
            | JETPACK EQUALS KeyCode Action'''
    if len(s) == 2:
        s[0] = s[1]
    else:
        f = [s[1]]
        f.extend(s[2])
        s[0] = f


def p_error(s):
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
