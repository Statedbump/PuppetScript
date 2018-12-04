using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SimpleMovement : MonoBehaviour {
private float speed;
private float time; 
void Start() 
 { 
speed = 10.0; 
time = Time.deltaTime; 
 } 
void Update() 
 { 
transform.Translate(0f,speed * Input.GetAxis(Horizontal) * time, 0f); 
transform.Translate(0f, 0f, speed * Input.GetAxis(Vertical) * time); 

 } 
 } 
