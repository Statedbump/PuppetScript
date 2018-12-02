code = []
type = 'HEY'



def set_scripttype(sct):
    global type
    type = sct
    print(type)


def initial_rigid_body(speed):
    print ("using System.Collections;\n" )
    print ("using System.Collections.Generic;\n" )
    print ( "using UnityEngine;\n" )
    print ( "public class RigidMovement:MonoBehaviour \n { \n" )
    print ( "float _speed = " + speed + "f;\n")


def move(x,y,z):
    if type  == 'RIGIDBODY':
        print("string _movementX = \"" + x + "\" ; \n" )
        print("string _movementZ = \"" + z + "\" ; \n" )
        print("Rigidbody _rigidBody; \n float _moveX; \n float _moveZ; \n float dist_to_ground = 1f;" )
        print("void Start() \n {")
        print("_rigidBody = this.GetComponent<Rigidbody>(); \n  if (_rigidBody == null) \n { \n ")
        print("Debug.LogError(\"Rigid body could not be found.\"); \n } \n }")
        print("void Update() \n { \n _moveX = Input.GetAxis(_movementX); \n _moveZ = Input.GetAxis(_movementZ); \n } \n")
        print("void FixedUpdate() \n { \n Vector3 moveVector = new Vector3(_moveX,0,_moveZ)*_speed;\n")

    elif type == 'CHARACTERCONTROLLER':
        print("if (charCont.isGrounded) {\n" +
              "float deltaX = Input.GetAxis( \"" + x + "\");\n" +
              "float deltaZ = Input.GetAxis( \"" + z + "\");\n" +
              "\n" +
              "movement = new Vector3(deltaX, 0, deltaZ); \n " +
              "\n" +
              "movement = transform.TransformDirection(movement);\n " +
              "\n" +
              "movement *= speed;\n")
		

def addForce(force):
    print("rigidBody.AddForce(moveVector,ForceMode."+force+"); \n")
	
def jump_Action(key):
    if type == 'RIGIDBODY':
        print( "if(Input.GetKey(KeyCode."+key+") && isGrounded()) {\n" +
            "jump();\n" +
            "}\n")

def dash_action(key):
    if type == 'RIGIDBODY':
        print("if(Input.GetKey(KeyCode." + key + ")) {\n" +
              "dash(moveVector);\n" +
              "}\n")
def jetpack_action(key):
    if type == 'RIGIDBODY':
        print("if(Input.GetKey(KeyCode." + key + ")) {\n" +
              "jump();\n" +
              "}\n")





def set_Action(actionList):
    for i in range(0, len(actionList), 2 ):
        if actionList[i] == 'JUMP':
            jump_Action(actionList[i+1])
        elif actionList[i] == 'DASH':
            dash_action(actionList[i+1])
        else:
            jetpack_action(actionList[i+1])



def end_rigidbody():
    print("}\n" +
            "}\n" +
            "bool isGrounded() {\n" +
            "return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);\n" +            "}\n" \
            "\n" +
            "void jump() {\n" +
            "_rigidBody.AddForce(new Vector3(0,1f,0), ForceMode.Impulse);\n" +
            "}\n" +
            "void dash(Vector3 moveVector) \n { \n "+
            "_rigidBody.AddForce(moveVector, ForceMode.VelocityChange); \n } \n } \n"


            )



def initial_char_cont(speed,gravity):
    print ( "using System.Collections;\n" +
            "using System.Collections.Generic;\n" +
            "using UnityEngine;\n" +
            "\n" +
            "public class PlayerMovement : MonoBehaviour {\n" +
            "\n" +
            "private float speed = " + speed + "f;\n" +
            "private float jump = 1f;\n" +
            "private float gravity = " + gravity + ";\n" +
            "private Vector3 movement = Vector3.zero;\n" +
            "\n" +
            "private CharacterController charCont;\n" +
            "\n" +
            "// Use this for initialization\n" +
            "void Start() {\n" +
            "charCont = GetComponent<CharacterController>();\n" +
            "\n" +
            "if (charCont == null) {\n" +
            "Debug.LogError(\"character controller could not be found.\");\n" +
       	    "}\n" +
            "}\n" +
            "\n" +
            "// FixedUpdate is called for physics calculations\n" +
            "void FixedUpdate() { \n" )

    #code.append(block)


def walk_char_cont():
    block = "if (Input.GetKey(KeyCode.LeftShift))\n" \
            "movement *= .5f;\n"
    code.append(block)


def sprint_char_cont():
    block = "if (Input.GetKey(KeyCode.LeftShift))\n" \
            "movement *= 2f;\n"
    code.append(block)


def jump_char_cont():
    block = "if (Input.GetButtonDown(\"Jump\"))\n" \
            "movement.y = jump;\n"
    code.append(block)


def end_char_cont():
    block = "}\n" \
            "movement.y -= gravity;\n:" \
            "\n" \
            "charCont.Move(movement);\n" \
            "}\n" \
            "}\n"
    code.append(block)


def upload():
    final_code = code[0]

    for block in code:
         final_code += code[block]

    file = open("player_movement.cs", 'w')
    file.write(final_code)
    file.close()

