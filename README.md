## A SELF QUIZZING PROGRAM ON RENAISSANCE ARTWORKS

This repo contains a dataset on more than 60 artworks from the Renaissance period, produced by Italian artists between 1250-1450. To contribute to the data set,
add the name of the artworks, the name of the artists, the location and the date it was produced to the Excel file artworks.xlsx in the folder **data**. You do not
have to provide a png file for the artwork. This will be done automatically by the program given the name of the artwork and the artist.

This repo also contains a self quizzing program I made to help me study for my exams. The program will shuffle the list of artworks, show a picture of the painting/sculpture for
**n** seconds, and print out the information of the piece to the terminal. I would love to create a GUI for the project, but due to time constraint, there are still a few kinks 
I have not fixed, like automatic closing of the png file.

To run the program, type the following to your terminal in the root directory:

```
python3 main.py
```

After you are done with one artwork, you will have to close the image file manually. A new artwork will be display in a given number of seconds.
