using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour {

private float speed = 10.0f;
private float jump = 1f;
private float gravity = 0.1f;
float deltaX; 
 float deltaZ; 
private Vector3 movement = Vector3.zero;

private CharacterController charCont;

// Use this for initialization
void Start() {
charCont = GetComponent<CharacterController>();

if (charCont == null) {
Debug.LogError("character controller could not be found.");
}
} 

// FixedUpdate is called for physics calculations
void FixedUpdate() { 
deltaX = Input.GetAxis( "Horizontal");
deltaZ = Input.GetAxis( "Vertical");

movement = new Vector3(deltaX, 0, deltaZ); 
 
movement = transform.TransformDirection(movement);
 
movement *= speed;
if (Input.GetKey(KeyCode.Space) && charCont.isGrounded) 
 { 
movement.y = jump; 
 } 

movement.y -= gravity;
charCont.Move(movement);
}
}
