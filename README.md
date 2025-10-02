# Rasa + PostgreSQL Dummy Bot

A tiny Rasa chatbot prototype running in Docker, storing conversations in PostgreSQL.

---

## What it does

- Handles 4 intents: `greet`, `ask_help`, `out_of_scope`, `goodbye`.
- Replies with simple responses (utterances).
- Stores all messages in a PostgreSQL tracker store.
- Default reply for unknown input.

---

## Quick Demo

### Swagger UI

Main page:

![Swagger UI Main](images/swagger.png)

Try it out with a chat request:

![Swagger UI Request](images/swagger_2.png)

### Chat Demo GIF

![Chatbot Demo](images/chatbot_demo.gif)


> All messages get saved in the DB.

---

## Notes

- Stories/rules are minimal and consistent.
- Runs via Docker Compose: Rasa + Action Server (not used currently) + PostgreSQL.

---

## Tech

- Rasa  
- Python  
- PostgreSQL  
- Docker / Docker Compose
- FastAPI
