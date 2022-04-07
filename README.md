# Kitchen Database App

This is the website that allows you to inventory everything in your home, via entering it
in or a barcode reader (coming soon). The items will come up in your "What you have" page. The page is sorted by item priority and then by item quantity.

## Random error problems in editor

If your editor gives you a problem with the file

    /website/templates/what_you_have.html

About some of the jinja templating, don't worry, ignore it.

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
