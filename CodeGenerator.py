code = ""
variables = {}
keys = []
actions = []

def createVariable(command):
    variables[command[1]] = command[2]
    print(variables)


def move(command):
    
        

def initialRigidbody(speed, Horizontal, Vertical):
    code = "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "\n" \ 
            "public class RigidMovement : MonoBehaviour {\n" \
            "string _movementX = \"" + Horizontal + "\";\n" \
            "\n" \
            "string _movementZ = \"" + Vertical + "\";\n" \
            "\n" \
            "_speed = " + speed + ";\n" \
            "\n" \
            "Rigidbody _rigidBody;\n" \
            "float _moveX;\n" \
            "float _moveZ;\n" \
            "float dist_to_ground = 1f;\n" \
            "\n" \
            "void Start() {\n" \
            "_rigidBody = this.GetComponent<Rigidbody>();\n" \
            "\n" \
            "if (_rigidBody == null)\n {" \
            "Debug.LogError(\"Rigid body could not be found.\");\n" \
            "}\n" \
            "}\n" \
            "\n" \
            "// Update is called once per frame\n" \
            "void Update() {\n" \
            "_moveX = Input.GetAxis(_movementX);\n" \
            "_moveZ = Input.GetAxis(_movementZ);\n" \
            "}\n" \
            "void FixedUpdate() {\n" \
            "\n" \
            "if (_rigidBody != null) {\n" \
            "Vector3 moveVector = new Vector3(_moveX, 0, _moveZ) * _speed;\n" \
            "_rigidBody.AddForce(moveVector, ForceMode.Acceleration);\n"


def jumpRigidBody():
    code += "if(Input.GetKey(KeyCode.Space) && isGrounded()) {\n" \
            "jump();\n" \
            "}\n"


def helperJump():
    code += "}\n" \
            "}\n" \
            "bool isGrounded() {\n" \
            "return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);\n" \
            "}\n" \
            "\n" \
            "void jump() {\n" \
            "_rigidBody.AddForce(new Vector3(0,1f,0), ForceMode.Impulse);\n" \
            "}\n"


def initialCharCont(speed, jump, gravity):
    code = "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "\n" \
            "public class PlayerMovement : MonoBehaviour {\n" \
            "\n" \
            "private float speed = " + speed + ";\n" \
            "private float jump = " + jump + ";\n" \
            "private float gravity = " + gravity + ";\n" \
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
            "float deltaX = Input.GetAxis(\"Horizontal\");\n" \
            "float deltaZ = Input.GetAxis(\"Vertical\");\n" \
            "\n" \
            "movement = new Vector3(deltaX, 0, deltaZ);\n" \
            "\n" \
            "movement = transform.TransformDirection(movement);\n" \
            "\n" \
            "movement *= speed;\n"


def walkCharCont():
    code += "if (Input.GetKey(KeyCode.LeftShift))\n" \
            "movement *= .5f;\n"


def sprintCharCont():
    code += "if (Input.GetKey(KeyCode.LeftShift))\n" \
            "movement *= 2f;\n"


def jumpCharCont():
    code += "if (Input.GetButtonDown(\"Jump\"))\n" \
            "movement.y = jump;\n"


def endCharCont():
    code += "}\n" \
            "movement.y -= gravity;\n:" \
            "\n" \
            "charCont.Move(movement);\n" \
            "}\n" \
            "}\n"


def upload():
    code += "}"
    filePath = ""
