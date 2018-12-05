using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class RigidMovement: MonoBehaviour 
 { 
float _speed = 10.0f;
string _movementX = "Horizontal" ; 
string _movementZ = "Vertical" ; 
Rigidbody _rigidBody; 
 float _moveX; 
 float _moveZ; 
 float dist_to_ground = 1f; 
void Start() 
 { 
_rigidBody = this.GetComponent<Rigidbody>(); 
  if (_rigidBody == null) 
 { 
 Debug.LogError("Rigid body could not be found."); 
 } 
 }void Update() 
 { 
 _moveX = Input.GetAxis(_movementX); 
 _moveZ = Input.GetAxis(_movementZ); 
 } 
void FixedUpdate() 
 { 
 Vector3 moveVector = new Vector3(_moveX,0,_moveZ)*_speed;
_rigidBody.AddForce(moveVector,ForceMode.Acceleration); 
if(Input.GetKey(KeyCode.Space) && isGrounded()) {
jump();
}
if(Input.GetKey(KeyCode.LeftShift)) {
dash(moveVector);
}
if(Input.GetKey(KeyCode.X)) {
jump();
}

}
bool isGrounded() {
return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);
}

void jump() {
_rigidBody.AddForce(new Vector3(0,1f,0), ForceMode.Impulse);
}
void dash(Vector3 moveVector) 
 { 
 _rigidBody.AddForce(moveVector*2f, ForceMode.Force); 
 } 
 } 
