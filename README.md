# Milestone Project 1 - Embrace Support Group
![image](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/user_wins.JPG)

## Table of Contents

* Introduction
* UX
 
  * Owner Goals
  * User Goals

* Layout
 
  
 * Features

* Structure
  * FLowchart
  * General logic
  * Functions
  * Discrepancies with original ideas
  

* Technologies

* Testing

* Bugs, Issues

* Deployment

* Acknowledgements

# Introduction
The product (Battleship game in Python) is a logic game based on the well known boardgame, where two players play against each other. Each player has two grids, one with different sizes of battleships on it, and the other oneis to mark off the guesses they made about the other players battleships. Battleships are represented by intersections of rows and columns. They can be only vertical or horizontal, not diagonal. Ships can touch each other, though. 

The players are not allowed to see the other player's grids. 

The players take turns making guesses by calling out row and column intersections. If a player calls out a row and column intersection with no battleship, he crosses it off with an X and the other player does it, too on their own grid. Hits are marked differently. The player, who guesses all the other player's battleship first, wins the game.

In this project the user plays against the computer. The computer generates a random row and column number, and the intersection represents a ship. 

This game has currently one ship only. It is more for the showcasing of programming logic, putting together code components and user input validation. In future, I would like to implement more ships in the game, to make it more challenging and enjoyable for users andto improve my Python skills.


# UX

* Owner goals

The owners of the product is the programmer who would like to showcase her skills for users, fellow programmers and prospective employers. 


* User goals

Potential users would like to achieve the following:

* Play a logic based game
* Play the game on different difficuly levels

The game uses a very basic logic of elimination: once you guessed something and it was wrong, you shouldn't guess that again but move onto a next guess. 

Different diffuculty levels are achieved by the different grid sizes.
Possible grid sizes are 4 x 4, 6 x 6, 8 x 8, 10 x 10. They can be set by the initial user input.


# Layout

My battleship is a very simple console based game. Only the mere instructions, user feedbacks and the grid at the different stages of the game is displayed. In future, I would like to display some ASCII graphics to make the game more attractive and to get learn more about graphics in Python.

[Battleship running in Heroku](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/user_loses.JPG)
[Battleship running in IDLE](https://github.com/renatalantos/Battleship-in-Python/blob/main/documents/screenshots/run_in_pyhton_idle.JPG) 



# Features


## Future features

A hamburger menu for mobile view.

# Structure
## Wireframes


### Wireframes for mobile, tablet and desktop view are available here: 

[Mobile View](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/wireframes/Milestone_Project_1_Wireframes%20for%20mobile%20view.pdf)


[Tablet View](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/wireframes/Milestone_Project_1_Wireframes%20for%20tablet%20view.pdf)


[Desktop View](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/wireframes/Milestone_Project_1_Wireframes%20for%20desktop%20view.pdf)

## Discrepancies with original ideas


*  Overall 

Overall I kept to the basic layout described in the wireframes. The main discrepancy  is that I didn't implement a hamburger menu in mobile
view as planned. Also, in tablet and mobile view, the copyright message is not displayed. See Issues for explanation.

* On individual pages
  * Home page

  I added more text start with, as I felt the user would look for information on the group. I added smaller images to enhance the content and make the site visually more appealing. I divided the text area into a left and right section. The testimonials are displayed in a 2-by-2 view, instead of a 4-by-1 and used images, too to introduce the reviewers. I used Welcome instead of Intro.

    *  About page


    I added smaller images to enhance the content and make the site visually more appealing. I divided the text area into a left and right section. I used Our Group Leaders instead of History and used images, too to introduce them. I also planned to put the child psychologist contact details and image here, which are on the Contact page right now. I felt this was more logical and coherent.

    *  Sessions page 

    I added smaller images to enhance the content and make the site visually more appealing. I divided the text area into a left and right section. Also, a video is featured here, that I wanted to display in the Gallery page, as one of the images.

    *  Gallery page


    Instead of a mosaic image layout I displayed a whole page slideshow gallery. I felt this is more consistent with the layout of the previous pages that display a large size main image on top.

    *  Contact page 


    I changed the arrangements of the 3 sections on the page. The two 50% size sections are displayed in reverse order as the user will look for the contact details first according to the page title and on smaller screens the contact details might not show without scrolling down first. Also I inserted the child psychologist's details here. 


    The contact form is for newsletter subscription purposes, as opposed to the original where it was meant for contacting the site. This would have merely duplicated the contact option, without any added function.


    The radio button question has been changed to asking the user whether they would want to join soon. The original question would have been answered by the user in the process of contacting the group anyway.

    *  Confidentiality page - was meant to be the way it is in the final version. 

    ## Colours

    For the colours I partly used the [mycolor.space](https://mycolor.space/) site and the in-built colour palette in Gitpod. I aimed for low-tone, relaxing colours that harmonize with each other, as users turn to the site in distress, seeking for comfort. Dominant colours are shades of blue, shades  taupe, white, light blue-green and grey and black for text. Main images were selected accordingly.

    [Example for colour implementation - About page](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/About_page_main_image.JPG)

    ## Typography


    For the main text flow I used 'Lora', serif from Google fonts as it has nicely formed letters with a flow effect and it has a default font-weight that didn't need extra Css styling. 

    For links in the header and navbar and text-overlays displaying mottos and extra information, also image gallery overlay I used default 'Rubik', sans-serif from Google Fonts, sans-serif, as I find it matter-of fact letter-type. 

    For page headings I used the default 'Open Sans', sans-serif from Google Fonts, sans-serif, as I find it matter-of fact letter-type but it also differs from Rubik.


# Technologies

### The following technologies and platforms were used to create the site:

*  **HTML** for structure and text

*  **CSS** for styling

* **Javascript** for the Gallery page slideshow gallery

* **Google Fonts** for text

* **Font Awesome for icons** for icons

* **Responsivity mockup sites** to test responsivity

* **Gitpod** to create pages and assets

* **Github** to store created pages and assets


# Testing 

 ## Validation 

   My Home, About, Sessions, Gallery, Contact, Confidentiality html pages passed in the W3C HTML Validator with the following result. I needed to fix minor errors on 3 pages before: **Document checking completed. No errors or warnings to show.**

   My CSS page passed in the W3C Jigsaw CSS validator with the following result: **CSS Congratulations! No Error Found.**

  There were 9 warning messages displayed regarding imported elements. 
  These relate to the imported stylesheet on top of the page and the elements are imported to power the text overlay transform features.

  [CSS Warning messages after successful validation](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/CSS%20warning%20messages%20in%20Jigsaw.JPG)

  ## Testing in supported browsers

  I used the following most up-to-date browsers:

  * Google Chrome
  * Mozilla Firefox
  * Microsoft Edge
  * Internet Explorer

  Chrome, Firefox and Edge displayed the site without problems. Firefox and Edge display a sligthly different background color. 
  My guess is, they don't feature the colours I imported from the ColorSpace website and they substitute it with the closest match.

  Internet Explorer didn't display the animated features including the Javascript powered slideshow Gallery  first. 
  After I moved the javascript source links form the head into the end of the body page, these features worked as well.

  ## Responsiveness

  I checked the responsiveness on the following tools while creating the pages:

  * Google Developer Tools

  * Am I Responsive website

  The finished product was tested on the following devices:

  * Samsung Galaxy A51
  * Ipad
  * Huawei P30 Pro
  * Samsung Galaxy S5

  The site looked the way it was intended on almost all devices. However, the Ipad does not display the main images.
   Apparently that could do with the IOS system or Safari, I couldn't resolve this issue, however, in Google Developer 
   tools everything looks as meant.

  I also found while testing the responsive layout in Google Developer tools, that the smaller the device screen size, the better the header looks.

  ## Features 

  All features are working as intended. Contact form asks for relevant information if not given. 
  Radio buttons allow user to select one option at the time.

## Bugs, Issues


* Hamburger menu

I tried to insert a hamburger menu for mobile view using Javascript following the [https://www.w3schools.com/howto/howto_js_mobile_navbar.asp](https://www.w3schools.com/howto/howto_js_mobile_navbar.asp) link,
 however, the opened link tabs stayed open after being clicked on, and occupied too much space on the screen, so I reverted to using the header links. 

* Gap on the side of main images in large desktop view

This is due to the actual width of the images, which is 1500px and the screen width is wider than that. 
I considered resizing the images but I found that it affects the image quality, 
so I left it the way it is.  

* Header occupied a large portion of the screen in mobile view

 In mobile view the header took up too much space and nav elements appeared partly under each other. I resized the header in all views. In mobile views I reduced the line height, font size, the logo and all paddings and margins that could be done without. I gave the navbar a width of 90% and the logo 10%. This doesn't apply to devices under the screen width of under 321 px. Here I simply floated the logo to the left and reduced the navbar elements. On larger mobile devices the logo and the nav elements appear on 2 different lines, however the nav items are pretty much centered and the layout has improved a lot. 


* Extra space between elements Contact child psychologist link and copyright statement on About and Sessions pages. On the About page the footer was inside the #hero-text-area section, taking it out fixed the issue. 


* On the Sessions page an extra margin of 10px was was applied to the h3 footer elements, and extra 10px padding was applied to the footer h6 elements. Styling just the footer h3 elements by stopping them from sharing the same properties as the navbar elements and footer links was half of the solution. In the properties I set both margin and padding to 0. I created an id for the footer h6 and styled this again with no margin or padding.

[Gap as intended](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/gap%20between%20contact%20child%20psychologist%20link%20and%20copyright%20as%20intended.JPG)
[Gap appears larger than intended](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/gap%20appear%20larger%20on%20Sessions%20and%20Gallery%20pages.JPG)


* The above helped me solve another issue where creating an extra div for the copyright statement and placing it after the Follow us on social media text in the html file highlighted the flaws mentioned in the above section. The copyright statement had to be part of the of footer-item-center div, after the Contact a child psychologist link. Therefore, when diaplayed in mobile view, the copyright statement was displayed between links and not at the bottom. Therefore, in tablet and mobile view the copyright needed to hidden in the @media queries. 

[Illogical position of copyright statement in the footer in tablet and mobile view](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/footer%20and%20copyright.JPG)



* Radio buttons allow user to select two options at the same time. 

This was solved by adding a name to the radio input tags. 
[Radio button allows to selections at the same time](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/Radio%20buttons.JPG)

* Gap between main Home image and text area

A gap appeared between the main image and the text area in tablet and large desktop view. This was due to the narrower height and width of the image from the rest.
 I fixed this issue resizing the image for the 2 extra views. However, when tested on my Android Galaxy A51, the gap appeared there (not before). I fixed this by adding an extra 20px of height and line height in mobile view. This fixed the issue.

[Gap between main image and text area](https://github.com/renatalantos/Embrace-support-group/blob/master/documents/screenshots/Gap_between_image_and_text_area.jpg)

# Deployment

The site was deployed to GitHub pages. The steps to deploy are as follows:

1. In the GitPod Workspace I made sure that everything is saved.
2. In the Terminal window I added all my files by using git add . .
2. In the Terminal window I queued my files using git commit -m "Meaningful, descriptive note"
3. In the Terminal window I typed git push to push my updated files into GitHub.
4. In GitHub I selected my repository name from the dropdown window.
5. I navigated to the Settings tab on the right hand side (above Green Gipod button).
6. On the Settings page I navigated to GitHub Pages.
7. I clicked on the Check out here! link after the message: Pages settings now has its own dedicated tab!
8. This took me to the next page GitHub Pages. 
9. Under Source I selected branch **Master** from the **None**, **extensions** and **Master** options.
10. From the folders beside branch I selected /(root) from /(root) and /docs.
11. Next I clicked save.
12. My live site was deployed a few minutes later under [the following link:](https://renatalantos.github.io/Embrace-support-group/)


# Acknowledgements 

The below website is a collage for all over the web.

## Idea

Completely mine. However, I was glad to discover that there are web pages, images, videos featuring parent support groups and therapy groups in general. 

## Text 
Text is a mix from the following websites:

* [General1](https://www.relate.org.uk/)
* [General2](https://turn2me.ie/)
* [General3](http://www.familymatters.ie/testimonials.html)
* [General4](https://www.goodtherapy.org/learn-about-therapy/modes/group-therapy)
* [Confidentiality page](https://students.tufts.edu/sites/default/files/HWClientConsentConfidentialityPolicy.pdf)

## Images 

Images are  courtesy of the [pexels.com](https://www.pexels.com/).  Thanks Tima!
The main Home page image is featured on the [www.newportacademy.com](https://www.newportacademy.com/resources/restoring-families/parenting-support-groups/) webiste.

## Video 

Video is courtesy of a lovely parent support group and YouTube
[YouTube video link](https://www.youtube.com/watch?v=jAIRxEWfl7Y)

## Text styling
I used the GoogleFonts website to choose my letter styles.

## Icons

Icons are from the FontAwesome website.

## Colours
Colours were partly chosen from the mycolor.space website and the default palette in GitPod. 

## Technologies
My beloved cheetsheet, the www.w3schools website for Javascript. Kits to power image transformations, the gallery slideshow and buttons for the slideshow are from there. 

# Special Acknowledgements

* To Roman for staring us off on this journey.
* To Kasia for all her help and hard work.
* To my classmates who helped and advised.
* To my mentor Seun for her guidance.

And last but not least my family for testing my pages while I was testing their patience.
Sorry about the late dinners and horrible meals!!! And Thanks!































  










    
  




































  










    
  






