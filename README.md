# CHESS Move app
Technologies used used:  
- Language: Python
- Framework: Fast API
- Docker

### Running server
- Install Docker
- Build the image by running 
    ```
        docker-compose build
    ```
- Next run docker-compose up to run the server
    ```
        docker-compose up
    ```

For testing postman can be used and post request on http://localhost:8000/chess/\<peice-of-choice> endpoint with data in this format {"postions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3""}} to get relevent output

