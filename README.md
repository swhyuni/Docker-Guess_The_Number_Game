# **Guess the Number**

## **Description:**
Welcome to the simple game application "Guess the Number"! In this game, you have the opportunity to guess a number from 0 to 9 three times. You will be given chances to make sequential guesses, and the application will inform you if your guess is **TRUE or FALSE**. If you manage to guess the correct number, you will be the winner!

# **How to Play:**
1. Download the source code from this repository.
2. Make sure you have Python and Docker installed on your system.
3. Open a terminal or command prompt and navigate to the directory of this game application.
4. Run the application with the following command:

```
python app.py
```
Or in Docker 
```
docker run -it yunisswh/my-game-yuni:v.0.0.1
```
5. The application will prompt you to guess the first number from 0 to 9.
6. Enter your guess and press Enter.
7. The application will notify you if your guess is correct, too high, or too low.
8. Repeat steps 5 and 6 to guess the second and third numbers.
   
## **Technology Used**
This game application is built using the Python programming language with the assistance of the NumPy library. NumPy is used to simplify data processing and allows the application to randomly choose the numbers to be guessed.

## **Docker:**
Docker is used to package this application into isolated containers, making it easy to run the application on various systems without worrying about configuration or environment differences.
