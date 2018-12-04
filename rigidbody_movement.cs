using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class RigidMovement:MonoBehaviour 
 { 
float _speed = 10.0f;
string _movementX = "Horizontal" ; 
string _movementZ = "Vertical" ; 
Rigidbody _rigidBody; 
 float _moveX; 
 float _moveZ; 
 float dist_to_ground = 1f;void Start() 
 {_rigidBody = this.GetComponent<Rigidbody>(); 
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
rigidBody.AddForce(moveVector,ForceMode.Acceleration); 
if(Input.GetKey(KeyCode.W)) {
_rigidBody.AddForce(moveVector*0.5f, ForceMode.Force);
}

}
bool isGrounded() {
return Physics.Raycast(transform.position, Vector3.down, dist_to_ground);
}

void jump() {
_rigidBody.AddForce(new Vector3(0,_jump,0), ForceMode.Impulse);
}
void dash(Vector3 moveVector) 
 { 
 _rigidBody.AddForce(moveVector*2f, ForceMode.Force); 
 } 
 } 
