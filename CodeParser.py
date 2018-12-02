from _testcapi import raise_exception

import ply.yacc as yacc
import CodeLexer
import CodeGenerator as gen
tokens = CodeLexer.tokens

action_args = 0
d_args = 0
j_args = 0
jet_args = 0
keyList =[]

def p_script_type(p):
    '''script : Simple
                | RigidBody
                | CharacterController'''

def p_simple_script(p):
 'Simple : SIMPLE SpeedId Movement'
 p[0] = (p[1], p[2], p[3] )

   

def p_rigid_script(p):
    'RigidBody : RIGIDBODY SpeedId  Movement  ForceMode  Action'
    x = p[3]
    f = [p[1]]
    f.extend( [ p[2], p[3], p[4], p[5] ] )
    print (f)
    p[0] = [f]
    gen.set_scripttype('RIGIDBODY')
    gen.initial_rigid_body(p[2])
    gen.move(x[0], x[1], x[2])
    gen.addForce(p[4])
    gen.set_Action(p[5])
    gen.end_rigidbody()



def p_chraracter_controller_script(p):
    'CharacterController : CHARACTERCONTROLLER SpeedId GravityId Movement  ForceMode  Action'
    p[0] = (p[1], p[2], p[3], p[4], p[5], p[6])
    x = p[4]
    f = [p[1]]
    f.extend([p[2], p[3], p[4], p[5]])
    print(f)
    gen.set_scripttype('CHARACTERCONTROLLER')
    gen.initial_char_cont(p[2], p[3])
    gen.move(x[0], x[1], x[2])



def p_speed_Id(p):
    'SpeedId : Speed EQUALS Float'
    print(type)
    p[0] = (p[3])

    


def p_gravity_Id(p):
    'GravityId : Gravity EQUALS Float'
    p[0] = (p[3])
  
	
	
def p_movement_rule(p):
    #First move is in x, followed by y , endind with z
    'Movement : ID EQUALS Direction ID EQUALS Direction  ID EQUALS Direction'

    p[0] = p[3], p[6], p[9]



def p_Direction(p):
    '''Direction : Horizontal
    | NONE
    | Vertical'''
    p[0] = p[1]
	
	
def p_force_mode(p):
    '''ForceMode : Force
                 | Impulse
                 | Acceleration
                 | NONE'''
    p[0] = p[1]


def p_action(p):
        '''Action : Jump
                  | Dash
                  | JetPack'''
        p[0] = p[1]
        global action_args
        action_args += 1
        if(action_args > 3):
            p_error(p)



def p_KeyCode(p):
    '''KeyCode : 
          | A
          | B
          | C
          | D
          | E
          | F
          | G
          | H
          | I
          | J
          | K
          | L
          | M
          | N
          | O
          | P
          | Q
          | R
          | S
          | T
          | U
          | V
          | W
          | X
          | Y
          | Z
          | Backspace
          | Tab
          | SysReq
          | Break
          | CapsLock
          | ScrollLock
          | RightShift
          | LeftShift
          | RightControl
          | LeftControl
          | RightAlt
          | LeftAlt
          | RightCommand
          | RightApple
          | LeftCommand
          | LeftWindows
          | RightWindows
          | AltGr
          | Help
          | Print
          | Clear
          | Return
          | Pause
          | Escape
          | Space
          | Exclaim
          | DoubleQuote
          | Hash
          | Dollar
		  | Ampersand
		  | Quote
		  | LeftParen
		  | RightParen
		  | Asterisk
		  | Plus
		  | Comma
		  | Minus
		  | Period
		  | Slash
		  | Colon
		  | Semicolon
		  | Less
		  | Equals
		  | Greater
		  | Question
		  | At
		  | LeftBracket
		  | Backslash
		  | RightBracket
		  | Caret
		  | Underscore
		  | BackQuote
		  
'''
    p[0] = p[1]
    keyList.append(p[1])
    if check_repeated_keys(keyList) == True :
        p_error(p)

def p_Jump(p):
    '''Jump : JUMP EQUALS KeyCode
            | JUMP EQUALS KeyCode Action'''
    global j_args
    j_args += 1
    if(j_args > 1):
        print ("JUMP action can only be called once!!")
        p_error(p)

    if(len(p)== 4):
        p[0] = (p[1], p[3] )
    else:
        f = [p[1], p[3]]
        f.extend( p[4] )
        p[0] = f


def p_Dash(p):
    '''Dash : DASH EQUALS KeyCode
            | DASH EQUALS KeyCode Action'''

    global d_args
    d_args += 1
    if (d_args > 1):
        print ("DASH action can only be called once!!")
        p_error(p)

    if (len(p) == 4):
        p[0] = (p[1], p[3])
    else:
        f = [p[1], p[3]]
        f.extend(p[4])
        p[0] = f


	

def p_JetPack(p):
    '''JetPack : JETPACK EQUALS KeyCode
            | JETPACK EQUALS KeyCode Action'''

    global jet_args
    jet_args += 1
    if (jet_args > 1):
        print ("DASH action can only be called once!!")
        p_error(p)

    if (len(p) == 4):
        p[0] = (p[1], p[3])
    else:

        f = [p[1], p[3]]
        f.extend(p[4])
        p[0] = f

def p_error(p):
    print("Syntax error in input")
    exit()

def check_repeated_keys(keyList):
    seen = set()
    for x in keyList:
        if x in seen:
            print( "Key_"+ x +" Is already being used ")
            return True
        seen.add(x)
    return False



def translate(s):

    try:
        BotifulCode = open(s, 'r')
    except IOError:
        print("Error opening File")
        exit()

    fileScript = BotifulCode.read()
    parser = yacc.yacc()
    res = parser.parse(fileScript)
    print (type)

