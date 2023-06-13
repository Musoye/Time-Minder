## ALX Foundation Stage Final project - Time-Master

![DO HARD THINGS](https://github.com/Musoye/Time-Master/blob/main/hardthings.jpeg)

`Developed By [Oyebamiji Mustapha Oyetunde](https://github.com/musoye)`

`The only way we can justify privilege is by doing hard things:by solving the world biggest problems - Fred Swaniker, Founder ALX`

## Description / Overview

A project management tool is a software application that helps teams manage tasks and projects by providing a centralized platform for creating, assigning, tracking, and prioritizing tasks.  view project here [musoye.tech](https://musoye.tech)

## Architecture:

The project used micro-services based archtecture.It divide the architecture into users and their projects; message and notifcation micro services; the backend that connects them together.

## User - Interface

The user interface is built with HTML, CSS, and JavaScript and some others front-end framework not limited to bootstrap, google font and others.

## User / Project Microservice

This contain both the project and the user information.we use various level of security which includes hashing of password and others.

## Message Microservices

This contain the notificaton of various action that takes place within the web application which includes email sending and others

## Deployment

Each Microservice will be deployed independently using gunicorn. failure of one will minimally or not cause the entire failure of the web applications

## Testing

Pytest is used and some test will be written before the deployment of this application.

## Authors

1. Oyebamiji Mustapha Oyetunde [musoye](https://twitter.com/musoye1)
