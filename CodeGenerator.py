code = []
type


def set_scripttype(sct):
    global type
    type = sct
    print(type)


def initial_simple(speed):
    block = "using System.Collections;\n" + \
            "using System.Collections.Generic;\n" + \
            "using UnityEngine;\n" + \
            "\n" + \
            "public class SimpleMovement : MonoBehaviour {\n" + \
            "private float speed;\n" + \
            "private float time; \n" + \
            "void Start() \n { \n" + \
            "speed = " + speed + "; \n" + \
            "time = Time.deltaTime; \n } \n"
    if code != block:
        code.append(block)


def initial_rigid_body(speed):
    block = "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "public class RigidMovement:MonoBehaviour \n { \n" \
            "float _speed = " + speed + "f;\n"

    code.append(block)


def initial_char_cont(speed, gravity):
    block = "using System.Collections;\n" \
            "using System.Collections.Generic;\n" \
            "using UnityEngine;\n" \
            "\n" \
            "public class PlayerMovement : MonoBehaviour {\n" \
            "\n" \
            "private float speed = " + speed + "f;\n" \
            "private float jump = 1f;\n" \
            "private float gravity = " + gravity + "f;\n" \
            "float deltaX; \n float deltaZ; \n" \
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
            "}\n} \n" \
            "\n// FixedUpdate is called for physics calculations\n" \
            "void FixedUpdate() { \n"
    code.append(block)


def move(x, y, z):
    if type == 'RIGIDBODY':
        block = "string _movementX = \"" + x + "\" ; \n" \
                "string _movementZ = \"" + z + "\" ; \n" \
                "Rigidbody _rigidBody; \n float _moveX; \n float _moveZ; \n float dist_to_ground = 1f;" \
                "void Start() \n {" \
                "_rigidBody = this.GetComponent<Rigidbody>(); \n  if (_rigidBody == null) \n { \n " \
                "Debug.LogError(\"Rigid body could not be found.\"); \n } \n }" \
                "void Update() \n { \n _moveX = Input.GetAxis(_movementX); \n _moveZ = Input.GetAxis(_movementZ); \n " \
                "} \n" \
                "void FixedUpdate() \n { \n Vector3 moveVector = new Vector3(_moveX,0,_moveZ)*_speed;\n"
        code.append(block)

    elif type == 'CHARACTERCONTROLLER':
        block = "deltaX = Input.GetAxis( \"" + x + "\");\n" \
                "deltaZ = Input.GetAxis( \"" + z + "\");\n" \
                "\n" \
                "movement = new Vector3(deltaX, 0, deltaZ); \n " \
                "\n" \
                "movement = transform.TransformDirection(movement);\n " \
                "\n" \
                "movement *= speed;\n"
        code.append(block)
    else:
        block = "void Update() \n { \n"
        code.append(block)
        if x == 'NONE':
            simple_noX(y, z)
        elif y == 'NONE':
            simple_noY(x, z)
        else:
            simple_noZ(x, y)


def addForce(force):
    block = "rigidBody.AddForce(moveVector,ForceMode."+force+"); \n"
    code.append(block)


def set_Action(actionList):
    for i in range(0, len(actionList), 2):
        if actionList[i] == 'JUMP':
            jump_action(actionList[i+1])
        elif actionList[i] == 'DASH':
            dash_action(actionList[i+1])
        else:
            jetpack_action(actionList[i+1])


def jump_action(key):
    if type == 'RIGIDBODY':
        block = "if(Input.GetKey(KeyCode."+key+") && isGrounded()) {\n" \
                "jump();\n" \
                "}\n"
        code.append(block)
    elif type == 'CHARACTERCONTROLLER':
        block = "if (Input.GetKey(KeyCode."+key+") && charCont.isGrounded) \n { \n" \
                "movement.y = jump; \n } \n"
        code.append(block)


def dash_action(key):
    if type == 'RIGIDBODY':
        block = "if(Input.GetKey(KeyCode." + key + ")) {\n" \
              "dash(moveVector);\n" \
              "}\n"
        code.append(block)
    if type == 'CHARACTERCONTROLLER':
        block = "if (Input.GetKey(KeyCode."+key+")) \n { \n" \
                "movement *= 2f;\n } \n"
        code.append(block)


def jetpack_action(key):
    if type == 'RIGIDBODY':
        block = "if(Input.GetKey(KeyCode." + key + ")) {\n" \
                "jump();\n" \
                "}\n"
        code.append(block)
    if type == 'CHARACTERCONTROLLER':
        block = "if (Input.GetKey(KeyCode." + key + ")) \n { \n" \
                "movement.y = jump; \n } \n"
        code.append(block)

# Helpers for Simple movement

def simple_noY(x, z):
    block = "transform.Translate(speed * Input.GetAxis(" + x + ") * time, 0f, 0f); \n" \
            "transform.Translate(0f, 0f, speed * Input.GetAxis(" + z + ") * time); \n"
    code.append(block)


def simple_noX(y, z):
    block = "transform.Translate(0f,speed * Input.GetAxis(" + y + ") * time, 0f); \n" \
            "transform.Translate(0f, 0f, speed * Input.GetAxis(" + z + ") * time); \n"
    code.append(block)


def simple_noZ(x, y):
    block = "transform.Translate(speed * Input.GetAxis(" + x + ") * time, 0f, 0f); \n" \
            "transform.Translate(0f,speed * Input.GetAxis(" + y + ") * time, 0f); \n"
    code.append(block)

# Script enders

def end_rigidbody():
    block = "}\n" \
            "}\n" \
            "bool isGrounded() {\n" \
            "return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);\n" + "}\n" \
            "\n" \
            "void jump() {\n" \
            "_rigidBody.AddForce(new Vector3(0,_jump,0), ForceMode.Impulse);\n" \
            "}\n" \
            "void dash(Vector3 moveVector) \n { \n " \
            "_rigidBody.AddForce(moveVector, ForceMode.VelocityChange); \n } \n } \n"
    code.append(block)


def end_char_cont():
    block = "\n" \
            "movement.y -= gravity;" \
            "\n" \
            "charCont.Move(movement);\n" \
            "}\n" \
            "}\n"
    code.append(block)


def end_simple():
    block = "\n } \n } \n"
    code.append(block)


def walk_char_cont():
    block = "if (Input.GetKey(KeyCode.LeftShift))\n" \
            "movement *= .5f;\n"
    code.append(block)


def upload():
    final_code = code[0]

    for block in code:
        if final_code != block:
            final_code += block

    file = open("player_movement.cs", 'w')
    file.write(final_code)
    file.close()
