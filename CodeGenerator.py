code = []
type = 'HEY'



def set_scripttype(sct):
    global type
    type = sct
    print(type)
    
def initial_simple(speed):
    print("using System.Collections;\n" +
            "using System.Collections.Generic;\n" +
            "using UnityEngine;\n" +
            "\n" +
            "public class SimpleMovement : MonoBehaviour {\n" +
            "private float speed;\n" +
            "private float time; \n" +
            "void Start() \n { \n"+
            "speed = "+speed+"; \n"+
            "time = Time.deltaTime; \n } \n")

def initial_rigid_body(speed,jump):
    print ("using System.Collections;\n" )
    print ("using System.Collections.Generic;\n" )
    print ( "using UnityEngine;\n" )
    print ( "public class RigidMovement:MonoBehaviour \n { \n" )
    print ( "float _speed = " + speed + "f;\n")
    print ( "float _jump = " + jump + "f;\n")
    


def initial_char_cont(speed,gravity,jump):
    print ( "using System.Collections;\n" +
            "using System.Collections.Generic;\n" +
            "using UnityEngine;\n" +
            "\n" +
            "public class PlayerMovement : MonoBehaviour {\n" +
            "\n" +
            "private float speed = " + speed + "f;\n" +
            "private float jump = " + jump + "f;\n" +
            "private float gravity = " + gravity + "f;\n" +
            "float deltaX; \n float deltaZ; \n" +
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
       	    "}\n" + "} \n" +
            "\n" + "// FixedUpdate is called for physics calculations\n" +
            "void FixedUpdate() { \n" )

    #code.append(block)




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
        print(
              "deltaX = Input.GetAxis( \"" + x + "\");\n" +
              "deltaZ = Input.GetAxis( \"" + z + "\");\n" +
              "\n" +
              "movement = new Vector3(deltaX, 0, deltaZ); \n " +
              "\n" +
              "movement = transform.TransformDirection(movement);\n " +
              "\n" +
              "movement *= speed;\n")
    else:
        print("void Update() \n { \n")
        if x == 'NONE':
            simple_noX(y, z)
        elif y == 'NONE':
            simple_noY(x, z)
        else:
            simple_noZ(x, y)


def addForce(force):
    print("rigidBody.AddForce(moveVector,ForceMode."+force+"); \n")




def set_Action(actionList):
    for i in range(0, len(actionList), 2 ):
        if actionList[i] == 'JUMP':
            jump_action(actionList[i+1])
        elif actionList[i] == 'DASH':
            dash_action(actionList[i+1])
        else:
            jetpack_action(actionList[i+1])




def jump_action(key):
    if type == 'RIGIDBODY':
        print( "if(Input.GetKey(KeyCode."+key+") && isGrounded()) {\n" +
            "jump();\n" +
            "}\n")
    elif type == 'CHARACTERCONTROLLER':
        print(" if (Input.GetKey(KeyCode."+key+") && charCont.isGrounded) \n { \n" +
              "movement.y = jump; \n } \n")



def dash_action(key):
    if type == 'RIGIDBODY':
        print("if(Input.GetKey(KeyCode." + key + ")) {\n" +
              "dash(moveVector);\n" +
              "}\n")
    if type == 'CHARACTERCONTROLLER':
        print("if (Input.GetKey(KeyCode."+key+")) \n { \n" +
              "movement *= 2f;\n } \n")


def jetpack_action(key):
    if type == 'RIGIDBODY':
        print("if(Input.GetKey(KeyCode." + key + ")) {\n" +
              "jump();\n" +
              "}\n")
    if type == 'CHARACTERCONTROLLER':
        print(" if (Input.GetKey(KeyCode." + key + ")) \n { \n" +
              "movement.y = jump; \n } \n")


# Helpers for Simple movement

def simple_noY(x, z):
    print(" transform.Translate(speed * Input.GetAxis(" + x + ") * time, 0f, 0f); \n" +
          " transform.Translate(0f, 0f, speed * Input.GetAxis(" + z + ") * time); \n")


def simple_noX(y, z):
    print(" transform.Translate(0f,speed * Input.GetAxis(" + y + ") * time, 0f); \n" +
          " transform.Translate(0f, 0f, speed * Input.GetAxis(" + z + ") * time); \n")


def simple_noZ(x, y):
    print(" transform.Translate(speed * Input.GetAxis(" + x + ") * time, 0f, 0f); \n" +
          "transform.Translate(0f,speed * Input.GetAxis(" + y + ") * time, 0f); \n")



# Script enders

def end_rigidbody():
    print("}\n" +
            "}\n" +
            "bool isGrounded() {\n" +
            "return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);\n" +            "}\n" \
            "\n" +
            "void jump() {\n" +
            "_rigidBody.AddForce(new Vector3(0, _jump,0), ForceMode.Impulse);\n" +
            "}\n" +
            "void dash(Vector3 moveVector) \n { \n "+
            "_rigidBody.AddForce(moveVector, ForceMode.VelocityChange); \n } \n } \n" )

def end_char_cont():
    print("\n" +
            "movement.y -= gravity;" +
            "\n" +
            "charCont.Move(movement);\n" +
            "}\n" +
            "}\n")



def end_simple():
    print("\n } \n } \n")





def walk_char_cont():
    block = "if (Input.GetKey(KeyCode.LeftShift))\n" \
            "movement *= .5f;\n"
    code.append(block)



def upload():
    final_code = code[0]

    for block in code:
         final_code += code[block]

    file = open("player_movement.cs", 'w')
    file.write(final_code)
    file.close()

