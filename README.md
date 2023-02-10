# Conversation matching with keywords
The goal of this project is to match a new user might have with conversation already present in the existing database

## Dataset:
For this demo I used a free ubuntu dataset with customer service chats, it came as a csv with the following structure:

 - **folder**: useless column for us with the folder where the conversation was saved
 - **dialogueID**: id of the dialogue
 - **date**: datetime of the message
 - **from**: username of the message's sender
 - **to**: username of the message's reciver
 - **text**: body of the message
 
## Processing:
Using pandas I joined the messages for each dialogue
then using yake(http://yake.inesctec.pt/) I exctacted the keywords of the dialogue to help the query process. 

## Database:
My database of choice is MongoDB, a non relational document based DB. 
The collection I created contains the dialogues with their keywords as documents.

## Querys and Usage:
I use the same method to extract keywords from a new quetion from the user then querys the database for a match.  
