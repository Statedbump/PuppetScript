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
    print ( "_speed = " + speed + ";\n")


def move(x,y,z):
    if (type  == 'RIGIDBODY'):
        print ("string _movementX = \"" + x + "\" \n" )
        print ( "string _movementZ = \"" + z + "\" \n" )
        print ("Rigidbody _rigidBody; \n float _moveX; \n float _moveZ; \n float dist_to_ground = 1f;" )
        print ( "void Start() \n {")
        print ("  _rigidBody = this.GetComponent<Rigidbody>(); \n  if (_rigidBody == null) \n { \n ")
        print  ("Debug.LogError(\"Rigid body could not be found.\"); \n {")
        print("void Update() \n { \n _moveX = Input.GetAxis(_movementX); \n _moveZ = Input.GetAxis(_movementZ); \n } \n ")
        print("void FixedUpdate() \n { \n Vector3 moveVector = new Vector3(_moveX,0,_moveZ)*_speed;\n" )
		

def addForce(force):
	print("_rigidBody.AddForce(moveVector,ForceMode."+force+"); \n")
	
def jump_rigid_body():
    block = "if(Input.GetKey(KeyCode.Space) && isGrounded()) {\n" \
            "jump();\n" \
            "}\n"
    code.append(block)


def helper_jump():
    block = "}\n" \
            "}\n" \
            "bool isGrounded() {\n" \
            "return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);\n" \
            "}\n" \
            "\n" \
            "void jump() {\n" \
            "_rigidBody.AddForce(new Vector3(0,1f,0), ForceMode.Impulse);\n" \
            "}\n"
    code.append(block)


def initial_char_cont(speed, horizontal, vertical):
    block = "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "\n" \
            "public class PlayerMovement : MonoBehaviour {\n" \
            "\n" \
            "private float speed = " + speed + ";\n" \
            "private float jump = 1f;\n" \
            "private float gravity = .1f;\n" \
            "private Vector3 movement = Vector3.zero;\n" \
            "\n" \
            "private CharacterController charCont;\n" \
            "\n" \
            "// Use this for initialization\n" \
            "void Start() {\n" \
            "charCont = GetComponent<CharacterController>();\n" \
            "\n" \
            "if (charCont == null) {\n" \
            "Debug.LogError(\"character controller could not be found.\");\n" \
       	    "}\n" \
            "}\n" \
            "\n" \
            "// FixedUpdate is called for physics calculations\n" \
            "void FixedUpdate() {\n" \
            "\n" \
            "if (charCont.isGrounded) {\n" \
            "float deltaX = Input.GetAxis(" + horizontal + ");\n" \
            "float deltaZ = Input.GetAxis(" + vertical + ");\n" \
            "\n" \
            "movement = new Vector3(deltaX, 0, deltaZ);\n" \
            "\n" \
            "movement = transform.TransformDirection(movement);\n" \
            "\n" \
            "movement *= speed;\n"
    code.append(block)


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

