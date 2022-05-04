# Kitchen Database App

This is the website that allows you to inventory everything in your home, via entering it
in or a barcode reader (coming soon). The items will come up in your "What you have" page. The page is sorted by item priority and then by item quantity.

## Getting started (auto-setup)

- If you're looking to get a quickstart, make sure the repository is downloaded and then go to /scripts. In there you will find 'setup', just run the file and the project answer a few questions and the project will get setup

      ./setup

- Because of the vast number of linux distributions, support for Windows and Mac is only being added first. If you would like to add a setup script for your distribution, you are more than welcome to do so.

## Getting Started (manual)

- In case the auto setup script didn't work, there is the manual setup which will take just an extra second, but will work just as well.

- In order to get started working on this project, you will need to make a clone of the project (make sure you are in the directory you want the project to be in):

      git clone https://github.com/sudoaptwhyupdate/KitchenDatabseWebsite.git

- Then, also make sure you have python installed so that you can run the project. You can go to the website or install it some other way. As long as the python version is higher than python 3.8.x
- Now it's time to install dependencies/python modules. You are going to need flask and sqlalchemy

        pip install flask
    
        pip install sqlalchemy

- Now that you have the project cloned, made sure python was installed, and modules downloaded, you should be good to go, you can run the project.

    python3 app.py

## Random error problems in editor

If your editor gives you a problem with the file

    /website/templates/what_you_have.html

About some of the jinja templating, don't worry, ignore it.

## Getting Picture Files (not necessary for operation)

- NOTE!! These images are not uploaded to dropbox yet, they will be soon but there are other, more important things that need to be worked on
- Please make sure your are not wasting your bandwidth. The picture files are pictures of the items that will appear on screen with the list, so if you're not handling that you don't need to download them.
- Use the dropbox link provided and then add the pictures to the static/images folder

    https://www.dropbox.com/sh/80w3gbdeywjg0b8/AAAq3aBqh0Vd0awEUntDqZGha?dl=0

## Input validation module

To use the module there are two functions that can be used from outside the module:

    len_check(name, min, max)
    type_check(data, data_type)

- "len_check" takes three arguments, name, min, and max. "Name" is what is getting checked, "min" is the minimum length, and "max" is the maximum length.
- "type_check" takes two arguments: data and data_type. Data is the thing you want checked, data_type is is the type you're checking for. so an example instance would be:

      type_check(variable_name, str)

    or

      type_check(9087, int)

Also to mention there is error_message_generator() which is private and only returns errors.
It sits in there in case it is needed for something later, but for now it it not used and is so
small it's not even worth removing from the project

## Secret Keys, and things that should normally be kept private

If you check in __init__.py you will note that there is a SECRET_KEY variable
which is to store a secret key for authentication in flask. Although normally this should
not be leaked, it's going to be changed before it's hosted, so put whatever you want in there.

## Weird GIT stuff

- I am really bad with git (as of now), so sometimes if you look at the tree, you might have a stroke, thats ok. Everything will get up to-date soon enough and with every branch merge I'm getting better.
