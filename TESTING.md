# Crushed Grapes - Testing Details

[Back to README.md file](README.md)

[Live website](https://crushed-grapes.herokuapp.com/)

___
## Contents
* [Code Validation](#code-validation)
* [Automated Testing](#automated-testing)
    + [Lighthouse Testing](#lighthouse-testing)
* [Manual Testing](#manual-testing)
    + [Functionality Testing](#functionality-testing)
    + [Responsiveness](#responsiveness)
    + [Cross Browser](#cross-browser)
* [User Stories Testing](#user-stories-testing)
* [Bugs and Fixes](#bugs-and-fixes)
___

## Code Validation

1. **HTML validated on [W3C Markup Validation Service](https://validator.w3.org/)**
Checked using the 'Validate By URI'.
* Blog app, Cart app, Home app, Products app, Profiles app, Reviews app pages and base.html were checked - only errors due to use of django template logic 
* Checkout app pages - warning 'p' element not allowed as child of 'small' - fixed this warning


2. **CSS validated on [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)**
Checked using the 'Validate by Direct Input' method.
* Blog.css, checkout.css, profile.css, base.css - all passed with no errors

3. **JavaScript validated on [JSHint](https://jshint.com/)**
* All js files and snippets of code within html files were tested using JSHint. Minor errors (missing semicolons) showed up on a couple of files. No other errors were found.

4. **Python valdiated on [PEP8 online](http://pep8online.com/)**
* Adjustments made where possible after running code through pep8 online & also using the `python3 -m flake 8` command in the terminal - most errors were line too long or trailing whitespaces. Some such errors were evident in base code set by Django so I did not change this. 


[Back to Contents](#contents)
***

## Automated Testing
___
### Lighthouse Testing

[Back to Contents](#contents)
***
## Manual Testing
___
### Functionality Testing

[Back to Contents](#contents)
___

#### Responsiveness



#### Cross Browser


[Back to Contents](#contents)
___
### User Stories Testing

[Back to Contents](#contents)
___
### Bugs and Fixes

[Back to Contents](#contents)
___
