**Mini Project #4: Python on Django with React**

| Field | Detail |
|-------|--------|
| Project Name | {Online Guitar Shop}|
| Description | {A place for selling guitars} |
| Developers | {Nicholas Murray} |
| Live Website | {coming soon} |
| Repo | {Link to git repository} |

## Problem Being Solved and Target Market

This is a web application where musicians can post, edit, and view a variety of guitars
for sale.

## User Stories

- Users should be able to see the site on desktop and mobile
- Users can create a guitar
- Users can see an inventory of guitars
- Users can update guitars
- User can delete guitars when they are sold

## Backend 

Django backend: JSON API with full crud functionality for the model

## Route Tables

| Endpoint | Method | Response |
| -------- | ------ | -------- | 
| /guitars | GET | JSON of all guitars| 
| /guitars/create | POST | A form to get new guitar and return JSON of new guitar|
| /guitars/:id | GET | JSON of guitar with matching id number| 
| /update/:id | PUT | update guitar, return its JSON |
| /edit/:id | DELETE | delete the guitar with the matching id|

![alt text] (https://i.ibb.co/cX5YGLR/erd.png)
