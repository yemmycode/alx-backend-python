0x01. Python - Async

Asynchronous programming in Python, often referred to as "async" programming, allows developers to write code that can handle multiple tasks concurrently, without blocking the execution of other tasks. This programming model is especially useful for tasks that involve waiting, such as I/O operations (reading/writing files, accessing databases, making API calls), where synchronous programming would otherwise keep the entire system idle while waiting for one operation to finish.

In this project, we explore the fundamentals of Python's async features, such as asyncio, async functions, coroutines, and handling concurrent tasks. By the end of this project, you will have a deeper understanding of how to structure asynchronous code to improve efficiency, responsiveness, and scalability in your applications.


Learning Objectives
Understand the concept of asynchronous programming and its advantages.
Learn how to use Python’s asyncio module to handle asynchronous operations.
Write and use async functions (coroutines).
Implement concurrent task execution with asyncio.gather and asyncio.create_task.
Work with asynchronous I/O operations for improved performance.
Handle exceptions in asynchronous functions.


Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
All your files must be executable
The length of your files will be tested using wc
The first line of all your files should be exactly #!/usr/bin/env python3
Your code should use the pycodestyle style (version 2.5.x)
All your functions and coroutines must be type-annotated.
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
