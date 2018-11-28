code = []
variables = {}
keys = []
actions = []

def create_variable(command):
    variables[command[1]] = command[2]
    print(variables)


def move(command):
    if command[1] == "RIGIDBODY":
        initial_rigid_body(variables[1], variables[2], variables[3])
        if command[2] == "Jump":
            jump_rigid_body()
        """
        if command[3] == "Dash":
            
        if command[4] == "Jetpack":
        """
    elif command[1] == "CHARACTERCONTROLLER":
        initial_char_cont(variables[1], variables[2], variables[3])
        if command[2] == "Jump":
            jump_char_cont()
        if command[3] == "Dash":
            sprint_char_cont()
        'if command[4] == "Jetpack":'
        end_char_cont()


def initial_rigid_body(speed, horizontal, vertical):
    block =  "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "\n" \ 
            "public class RigidMovement : MonoBehaviour {\n" \
            "string _movementX = \"" + horizontal + "\";\n" \
            "\n" \
            "string _movementZ = \"" + vertical + "\";\n" \
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
    code.append(block)


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
