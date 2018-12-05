# Introduction

## About Unity

Unity is a cross-platform video game engine developed by Unity Technologies. As of 2018, the engine has been extended to support 27 platforms. The engine can be used to create both three-dimensional and two-dimensional games as well as simulations for its many platforms. Unity offers a primary scripting API in C#, for both the Unity editor in the form of plugins, and games themselves, as well as drag and drop functionality. The popularity of this engine and its features make it generally easy to use for those new to game development. 

## Why use PuppetScript?

Since Unity's primary scripting API is in C#, some people can find themselves stuck in the process of creating scripts regardless of their programming knowledge. With the use of PuppetScript, users will be able to easily hop over one of the main hurdles found in scripting, three-dimensional player movement. This language features easy to learn functions which can be used by new and experienced developers alike. 



# About the Language

## Language Features

PuppetScript has the purpose of bringing simplicity to its users in order for them to reach the type of movement they desire in their 3D game's environment. This is achieved with the inclusion of some key features to facilitate the process of implementing player movement. Such language features include: 
 
* Translate simple and easy to learn grammar to complex C# code to work with Unity
* Creation of custom movement scripts for the game's playable character
* Functions that cut off the need for long and hard to learn movement customization scripts

## Approach
 <a href="https://imgur.com/UzlzF7n"><img src="https://i.imgur.com/UzlzF7n.png" title="source: imgur.com" /></a>

##### The PuppetScript Architecture works the following way:

1. First the user writes code in Unity in the PuppetScript Language.
2. The user runs the PuppetScript translator, which reads the PuppetScript code and is sends it to the PLY Lexer which tokenizes the code and then to the PLY parser which parses it.
3. After all data has been obtained from the code, it is sent to the Python intermediate code which categorizes and translates it into C# source code. 
4. The C# code creates the player controller according to the specifications provided.
5. When the aforementioned is ready, it is compiled.
6. And finally, the user is able to use their newly created PuppetScript script to control their character using Unity!


# Learning PuppetScript!

## Video Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/LJFQkBjePXQ?ecver=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Language tutorial

Click [here](https://github.com/jeanrodriguez27/PuppetScript/wiki/Language-Tutorial) to go to the Language Tutorial.

## Reference Manual

Click [here](https://github.com/jeanrodriguez27/PuppetScript/wiki/Reference-Manual) to go to the Reference Manual.



# Contributors

* [Angel Carrillo](https://github.com/AngelGCL)
* [Luis Cintron](https://github.com/Statedbump)
* [Fernando Guzman](https://github.com/FernandoLGuzman)
* [Jean Carlos Rodriguez](https://github.com/jeanrodriguez27)
