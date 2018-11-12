
import ply.lex as lex

#List of tokens

tokens = [
	#Character
	'ID',
	
	#Float number
	'Float',
	
	#Equals
	'EQUALS',
	
	#Simple	
	'SIMPLE',
	
	#RigidBody	
	'RIGIDBODY',
	
	#Character Controller
	'CHARACTERCONTROLLER',
	
	#Special iD's 
	'Speed','Gravity'
	
	#This part will be the movements
	
	#MoveX
	'Horizontal',
	#MoveZ
	'Vertical',
	#MoveY
	'NONE',
	
	#Actions
	'JUMP','DASH','JETPACK'
	
	#Forces
	'Force','Impulse','Acceleration',
	
	#KEYS
	
	#Letters
	'KeyCode_A','KeyCode_B','KeyCode_C','KeyCode_D','KeyCode_E','KeyCode_F','KeyCode_G',
	'KeyCode_H','KeyCode_I','KeyCode_J','KeyCode_K','KeyCode_L','KeyCode_M','KeyCode_N'
	'KeyCode_O','KeyCode_P','KeyCode_Q','KeyCode_R','KeyCode_S','KeyCode_T','KeyCode_U'
	'KeyCode_V','KeyCode_W','KeyCode_X','KeyCode_Y','KeyCode_Z',
	
	#Other Keys
	'KeyCode_Backspace','KeyCode_Tab', 'KeyCode_SysReq','KeyCode_Break',
	'KeyCode_CapsLock', 'KeyCode_ScrollLock', 'KeyCode_RightShift','KeyCode_LeftShift',
    'KeyCode_RightControl','KeyCode_LeftControl', 'KeyCode_RightAlt','KeyCode_LeftAlt',
    'KeyCode_RightCommand','KeyCode_RightApple', 'KeyCode_LeftCommand','KeyCode_LeftWindows', 
    'KeyCode_RightWindows','KeyCode_AltGr','KeyCode_Help','KeyCode_Print', 
	'KeyCode_Clear', 'KeyCode_Return', 'KeyCode_Pause', 'KeyCode_Escape', 
    'KeyCode_Space', 'KeyCode_Exclaim','KeyCode_DoubleQuote','KeyCode_Hash', 
    'KeyCode_Dollar','KeyCode_Ampersand','KeyCode_Quote', 'KeyCode_LeftParen', 
    'KeyCode_RightParen', 
    'KeyCode_Asterisk', 
    'KeyCode_Plus', 
    'KeyCode_Comma', 
    'KeyCode_Minus', 
    'KeyCode_Period', 
    'KeyCode_Slash', 

    'KeyCode_Colon', 
    'KeyCode_Semicolon',
    'KeyCode_Less',
    'KeyCode_Equals',
    'KeyCode_Greater',
    'KeyCode_Question,'
    'KeyCode_At',
    'KeyCode_LeftBracket',
    'KeyCode_Backslash',
    'KeyCode_RightBracket',
    'KeyCode_Caret', 
    'KeyCode_Underscore',
    'KeyCode_BackQuote',
     
]	

t_Float = r'[[0-9]+([.][0-9]+)*'
t_ID = r'[a-zA-z]([a-zA-Z]|[0-9])*'
t_EQUALS = r'\='
t_ignore = ' \t\n'


    #ScripTypes
def t_SIMPLE(t):
    r'SIMPLE'
    t.value = 'SIMPLE'
    return t

	
	
def t_RIGIDBODY(t):
	r'RIGIDBODY'
    t.value = 'RIGIDBODY'
    return t
	
def t_CHARACTERCONTROLLER(t):
	r'CHARACTERCONTROLLER'
    t.value = 'CHARACTERCONTROLLER'
    return t
	
	
	#Special IDs
def t_Speed(t):
    r'Speed'
    t.value = 'Speed'
    return t

def t_Gravity(t):
    r'Gravity'
    t.value = 'Gravity'
    return t	

	#Movement
def t_Horizontal(t):
    r'Horizontal'
    t.value = 'Horizontal'
    return t

def t_Vertical(t):
    r'Vertical'
    t.value = 'Vertical'
    return t
	
def t_NONE(t):
    r'NONE'
    t.value = 'NONE'
    return t


	#Actions
	
def t_JUMP(t):
    r'JUMP'
    t.value = 'JUMP'
    return t
def t_DASH(t):
    r'DASH'
    t.value = 'DASH'
    return t
def t_JETPACK(t):
    r'JETPACK'
    t.value = 'JETPACK'
    return t

	#Forces
def t_Force(t):
    r'Force'
    t.value = 'Force'
    return t


def t_Impulse(t):
    r'Impulse'
    t.value = 'Impulse'
    return t

def t_Acceleration(t):
    r'Acceleration'
    t.value = 'Acceleration'
    return t
	

#Keys
#LETTERS
def t_KeyCode_A(t):
    r'KeyCode.A'
    t.value = 'KeyCode_A'
    return t
def t_KeyCode_B(t):
    r'KeyCode.B'
    t.value = 'KeyCode_B'
    return t

def t_KeyCode_C(t):
    r'KeyCode.C'
    t.value = 'KeyCode_C'
    return t

def t_KeyCode_D(t):
    r'KeyCode.D'
    t.value = 'KeyCode_D'
    return t
	
def t_KeyCode_E(t):
    r'KeyCode.E'
    t.value = 'KeyCode_E'
    return t	
	
def t_KeyCode_F(t):
    r'KeyCode.F'
    t.value = 'KeyCode_F'
    return t	
	
def t_KeyCode_G(t):
    r'KeyCode.G'
    t.value = 'KeyCode_G'
    return t	
	
def t_KeyCode_H(t):
    r'KeyCode.H'
    t.value = 'KeyCode_H'
    return t	
	
def t_KeyCode_I(t):
    r'KeyCode.I'
    t.value = 'KeyCode_I'
    return t	
	
def t_KeyCode_J(t):
    r'KeyCode.J'
    t.value = 'KeyCode_J'
    return t	
	
def t_KeyCode_K(t):
    r'KeyCode.K'
    t.value = 'KeyCode_K'
    return t	
	
def t_KeyCode_L(t):
    r'KeyCode.L'
    t.value = 'KeyCode_L'
    return t	
	
def t_KeyCode_M(t):
    r'KeyCode.M'
    t.value = 'KeyCode_M'
    return t	
	
def t_KeyCode_N(t):
    r'KeyCode.N'
    t.value = 'KeyCode_N'
    return t	
	
def t_KeyCode_O(t):
    r'KeyCode.O'
    t.value = 'KeyCode_O'
    return t	
	
def t_KeyCode_P(t):
    r'KeyCode.P'
    t.value = 'KeyCode_P'
    return t
	
def t_KeyCode_Q(t):
    r'KeyCode.Q'
    t.value = 'KeyCode_Q'
    return t	
	
def t_KeyCode_R(t):
    r'KeyCode.R'
    t.value = 'KeyCode_R'
    return t	
	
def t_KeyCode_S(t):
    r'KeyCode.S'
    t.value = 'KeyCode_S'
    return t	
	
def t_KeyCode_T(t):
    r'KeyCode.T'
    t.value = 'KeyCode_T'
    return t	
	
def t_KeyCode_U(t):
    r'KeyCode.U'
    t.value = 'KeyCode_U'
    return t	
	
def t_KeyCode_V(t):
    r'KeyCode.V'
    t.value = 'KeyCode_V'
    return t	
	
def t_KeyCode_W(t):
    r'KeyCode.W'
    t.value = 'KeyCode_W'
    return t	
	
def t_KeyCode_X(t):
    r'KeyCode.X'
    t.value = 'KeyCode_X'
    return t	
	
def t_KeyCode_Y(t):
    r'KeyCode.Y'
    t.value = 'KeyCode_Y'
    return t	
	
def t_KeyCode_Z(t):
    r'KeyCode.Z'
    t.value = 'KeyCode_Z'
    return t
	
#OTHER BUTTONS	
	

def t_KeyCode_Backspace(t):
    r'KeyCode.Backspace'
    t.value = 'KeyCode_Backspace'
    return t
def t_KeyCode_Tab(t):
    r'KeyCode.Tab'
    t.value = 'KeyCode_Tab'
    return t
def t_KeyCode_SysReq(t):
    r'KeyCode.SysReq'
    t.value = 'KeyCode_SysReq'
    return t
def t_KeyCode_Break(t):
    r'KeyCode.Break'
    t.value = 'KeyCode_Break'
    return t
def t_KeyCode_CapsLock(t):
    r'KeyCode.CapsLock'
    t.value = 'KeyCode_CapsLock'
    return t
def t_KeyCode_ScrollLock(t):
    r'KeyCode.ScrollLock'
    t.value = 'KeyCode_ScrollLock'
    return t
def t_KeyCode_RightShift(t):
    r'KeyCode.RightShift'
    t.value = 'KeyCode_RightShift'
    return t
def t_KeyCode_LeftShift(t):
    r'KeyCode.LeftShift'
    t.value = 'KeyCode_LeftShift'
    return t
def t_KeyCode_RightControl(t):
    r'KeyCode.RightControl'
    t.value = 'KeyCode_RightControl'
    return t
def t_KeyCode_RightAlt(t):
    r'KeyCode.RightAlt'
    t.value = 'KeyCode_RightAlt'
    return t
def t_KeyCode_LeftAlt(t):
    r'KeyCode.LeftAlt'
    t.value = 'KeyCode_LeftAlt'
    return t
def t_KeyCode_RightCommand(t):
    r'KeyCode.RightCommand'
    t.value = 'KeyCode_RightCommand'
    return t
def t_KeyCode_RightApple(t):
    r'KeyCode.RightApple'
    t.value = 'KeyCode_RightApple'
    return t
def t_KeyCode_LeftCommand(t):
    r'KeyCode.LeftCommand'
    t.value = 'KeyCode_LeftCommand'
    return t
def t_KeyCode_LeftWindows(t):
    r'KeyCode.LeftWindows'
    t.value = 'KeyCode_LeftWindows'
    return t
def t_KeyCode_RightWindows(t):
    r'KeyCode.RightWindows'
    t.value = 'KeyCode_RightWindows'
    return t
def t_KeyCode_AltGr'(t):
    r'KeyCode.AltGr''
    t.value = 'KeyCode_AltGr''
    return t

def t_KeyCode_Help(t):
    r'KeyCode.Help'
    t.value = 'KeyCode_Help'
    return t
def t_KeyCode_Print(t):
    r'KeyCode.Print'
    t.value = 'KeyCode_Print'
    return t
def t_KeyCode_Clear(t):
    r'KeyCode.Clear'
    t.value = 'KeyCode_Clear'
    return t
def t_KeyCode_Return(t):
    r'KeyCode.Return'
    t.value = 'KeyCode_Return'
    return t
def t_KeyCode_Pause(t):
    r'KeyCode.Pause'
    t.value = 'KeyCode_Pause'
    return t
def t_KeyCode_Escape(t):
    r'KeyCode.Escape'
    t.value = 'KeyCode_Escape'
    return t
def t_KeyCode_Space(t):
    r'KeyCode.Space'
    t.value = 'KeyCode_Space'
    return t
def t_KeyCode_Exclaim(t):
    r'KeyCode.Exclaim'
    t.value = 'KeyCode_Exclaim'
    return t
def t_KeyCode_DoubleQuote(t):
    r'KeyCode.DoubleQuote'
    t.value = 'KeyCode_DoubleQuote'
    return t
def t_KeyCode_Hash(t):
    r'KeyCode.Hash'
    t.value = 'KeyCode_Hash'
    return t
def t_KeyCode_Dollar(t):
    r'KeyCode.Dollar'
    t.value = 'KeyCode_Dollar'
    return t
def t_KeyCode_Ampersand(t):
    r'KeyCode.Ampersand'
    t.value = 'KeyCode_Ampersand'
    return t
def t_KeyCode_Quote(t):
    r'KeyCode.Quote'
    t.value = 'KeyCode_Quote'
    return t
def t_KeyCode_LeftParen(t):
    r'KeyCode.LeftParen'
    t.value = 'KeyCode_LeftParen'
    return t
def t_KeyCode_RightParen(t):
    r'KeyCode.RightParen'
    t.value = 'KeyCode_RightParen'
    return t
def t_KeyCode_Asterisk(t):
    r'KeyCode.Asterisk'
    t.value = 'KeyCode_Asterisk'
    return t
def t_KeyCode_Plus(t):
    r'KeyCode.Plus'
    t.value = 'KeyCode_Plus'
    return t
def t_KeyCode_Comma(t):
    r'KeyCode.Comma'
    t.value = 'KeyCode_Comma'
    return t
def t_KeyCode_Minus(t):
    r'KeyCode.Minus'
    t.value = 'KeyCode_Minus'
    return t
def t_KeyCode_Period(t):
    r'KeyCode.Period'
    t.value = 'KeyCode_Period'
    return t
def t_KeyCode_Slash(t):
    r'KeyCode.Slash'
    t.value = 'KeyCode_Slash'
    return t
def t_KeyCode_Colon(t):
    r'KeyCode.Colon'
    t.value = 'KeyCode_Colon'
    return t
def t_KeyCode_Semicolon(t):
    r'KeyCode.Semicolon'
    t.value = 'KeyCode_Semicolon'
    return t
def t_KeyCode_Less(t):
    r'KeyCode.Less'
    t.value = 'KeyCode_Less'
    return t
def t_KeyCode_Equals(t):
    r'KeyCode.Equals'
    t.value = 'KeyCode_Equals'
    return t
def t_KeyCode_Greater(t):
    r'KeyCode.Greater'
    t.value = 'KeyCode_Greater'
    return t
def t_KeyCode_Question(t):
    r'KeyCode.Question'
    t.value = 'KeyCode_Question'
    return t
def t_KeyCode_At(t):
    r'KeyCode.At'
    t.value = 'KeyCode_At'
    return t
def t_KeyCode_LeftBracket(t):
    r'KeyCode.LeftBracket'
    t.value = 'KeyCode_LeftBracket'
    return t
def t_KeyCode_Backslash(t):
    r'KeyCode.Backslash'
    t.value = 'KeyCode_Backslash'
    return t
def t_KeyCode_RightBracket(t):
    r'KeyCode.RightBracket'
    t.value = 'KeyCode_RightBracket'
    return t
def t_KeyCode_Caret(t):
    r'KeyCode.Caret'
    t.value = 'KeyCode_Caret'
    return t
def t_KeyCode_Underscore(t):
    r'KeyCode.Underscore'
    t.value = 'KeyCode_Underscore'
    return t
def t_KeyCode_BackQuote(t):
    r'KeyCode.BackQuote'
    t.value = 'KeyCode_BackQuote'
    return t

