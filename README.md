# Game of Philosophy
![alt text](https://github.com/txstc55/wiki_philosophy/blob/master/Frequency.png)

## Purpose of the project
For long we have heard the myth that if you keep clicking on the first link on a wikipedia page (other than pronounciation and reference), and assume that you do not get stuck in a loop, then you will eventually get to the philosophy page.

This project explores that myths by doing the analysis on over 20000 wiki links, which is randomly generated by the wikipedia python api.

## What we did
For each link that we have, we did two analysis. First of all, does it really go to philosophy page? And if so, how long is the path. Second of all, what category does it belong to.

It seems hard to define what category a page really belongs to. However, this can also be done in the same fashion. By keep clicking on the first category of the page. Eventually it will go to a category under category.csv. Keep in mind that we did not generate the categories ourselves, it is actually provided by wikipedia.

## The result
To see a full presentation of this project please refer to The-Game-Of-Philosophy.pdf

The visualization of the project is the following graph, where each node is a wikipedia page, and each edge means a connection. We can see in the heart of the graph is Philosophy.
![alt text](https://github.com/txstc55/wiki_philosophy/blob/master/path.png)
