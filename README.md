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
    
- "len_check" takes three arguements, name, min, and max. "Name" is what is getting checked, "min" is the minimum length, and "max" is the maximum length.
- "type_check" takes two arguements: data and data_type. "Data" is what is getting checked, and data_type is the data type you're checking for. When using data type, input the data type as you would usually, but instead in a string. For example, "string", "int", "bool" instead of *string*, *int*, *bool*

Also to mention there is error_message_generator() which is private and only returns errors.
