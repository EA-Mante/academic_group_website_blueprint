# Introduction

In this document I will explain how to use each page on the website. The aim of this project is for any academic, regardless of position or department, to clone this repository and customize the pages to easily set up their own group page.

This is an ongoing project, I will update the github when I can.

# The Design

## <ins>Templates (the .html pages)</ins>

**_header.html_** allows you to customize the header of the website, including adding your group's logo

**_home.html_** is the home page, the first page visitors will see. A brief description of the group can be given here, as well as a group photo

**_PI_page.html_** is where the PI of the group can be introduced. I have given a generic description of a computation chemist, users can insert their own bio as well as edit the awards section at the bottom of the page

**_members.html_** shows the group members, at this stage simply copy and paste the relevant lines of html to add another member to a section (or another section, e.g. if your group has BSc students). **You can add linkedin or other hyperlinks, as shown in the "Fromer student 1" section**

**_opportunities.html_** gives you the chance to highlight any open opportunities in your group

**_publication.html_** provides the opportunity to familiarize visitors with your work [I am currently working on this section as well]

## <ins>Static (the images, etc.)</ins>

Place the images you want to use on your pages in this folder. **Ensure the name of the images matches the name of the file you are calling on your .html page**

# Getting started

To get started, open trun the following command in your preferred terminal:

```console
foo@bar:~$ git clone https://github.com/EA-Mante/academic_group_website_blueprint
```

This clones the repo to your computer

Next:
* Locate the folder in your computer
* Run using your preferred app (I use VS Code)
* Go to the main.py file and run it
* Wait for the line "Running on http://XXX.X.X.X:XXXX" to appear, and click the link to run locally, editing as you see fit
* Once the website is ready, launch it to a server to make it live
* Enjoy!
