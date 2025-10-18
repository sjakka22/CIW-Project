
In this repository, we would like to share and manage the update of our project: 

# Weekly update reports ```Updates```
In this directory, we create and collect the slides for our next presentation, 
preferably written in TeX. 
Proceed as follows:
1. Clone the repository via:
```
git clone https://github.com/sjakka22/CIW-Project.git
```
1. Write your slides in some .tex file, e. g. ``my_slides_group_X.tex``
Make sure to create distinguishable file names.
```
\begin{frame}{Our findings this week}
We found out that:
\begin{itemize}
    \item Point1
    \item Point2
\end{itemize}
\end{frame}
```
3. Commit your created (or modified) slides via:
```
git add my_slides.tex
git commit -m "I have completed my Slides"
git push
```
4. To be updated on the changes made to the repo, use the following command before working:
```
git pull
```

# Project report ```Report```
In this directory, we collect the chapters of our project report, 
preferably written in TeX. 
Proceed as follows:

1. Write your chapter in some .tex file, e. g. ``my_directory\my_chapter.tex``.

```
\section{Mein Kapitel}
Some text...
```

2. Use ``pdflatex my_directory\my_chapter.tex`` to compile your chapter.

3. Clone the repository via and change into the directory:
```
git clone https://github.com/sjakka22/CIW-Project.git
cd CIW-Project/Report
```
4. Move your .tex file into the Project directory via:
```
mv my_directory\my_chapter.tex .
```
Make sure that the .tex file is now in the Project directory.

5. Commit your created (or modified) chapter via:
```
git add my_chapter.tex
git commit -m "I have completed my Chapter on Topic XY"
git push
```
6. To be updated on the changes made to the repo, use the following command before working:
```
git pull
```

