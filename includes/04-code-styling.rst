
***********************
Code styling/guidelines
***********************


|CSS|/|Sass|
============

- |CSS| files that where generated from |Sass| sources are exempt from any styling rules. Trying to configure the output of |Sass| generated files is like trying to teach to talk to a rock!!! ¬¬
- Styling rules for |CSS| files:

    * 4 spaces indentation.
    * Open bracket same line as rule.
    * Space before open bracket.
    * Closing bracket on its own line at the start of last line of rule.
    * One selector per line.
    * Use hexadecimal colors unless alpha is needed.
    * Space after ``:`` of each declaration.
    * Each declaration on its own line.
    * All declarations ending with semi-colon. NO EXCEPTIONS.
    * Comma-separated property values should include a space after each comma.
    * Spaces after commas within rgba(), hsla(), or rect() values. If I couldn't read a the freaking parenthesis, I would go and program some garbage in C-sharp!!!
    * Prefix property values or color parameters with a leading zero (e.g., 0.5 instead of .5 and -0.5px instead of -.5px).
    * Do not specify units for zero values, e.g., ``margin: 0;`` instead of ``margin: 0px;``.

- Styling rules for |Sass| files:

    * Same as |CSS| files.
    * For the rest, don't even bother. Follow the rules forced by the *code formatter* in use...until it breaks due to an update that introduced *new features*. Then follow the rules forced by default by the following *code formatter* that works. It is absolutely pointless to rely on anything that it is based on web technologies and designed for and/or by web developers (in the span of just six weeks it will be broken again). ¬¬


JavaScript
==========

This is an abhorrent/always-evolving/never-finished language with an abhorrent release cycle whose only goal seems to be the destruction of software development (cursed the day that web developers started contaminating the software industry!!!). Guidelines will never have a chance to survive the countless stupid implementations by the countless |JS| engines.

- Until the *geniuses* at Mozilla and/or Gnome decide to FINALLY agree in a common AND unique implementation of |JS| classes, KEEP using *prototypes*.
- To avoid strict warnings triggered by SpiderMonkey:

    * Define all symbols that are meant to be exported with **var**. Use **let** or **const** to define symbols that are going to be used only at a module context.
    * All properties should be defined.

- Code styling:

    * Imports defined with PascalCase whether they are defined with **let**, **var** or **const**.
    * Constants defined with uppercase and low dashes.
    * Variables/Functions defined with camelCase.
    * Spaces around operators ( = + - \* / ), and after commas.
    * 4 spaces for indentation of code blocks.
    * End simple statements with a semicolon.
    * Rules for complex (compound) statements:

        - Put opening bracket at the end of the first line.
        - Use one space before the opening bracket.
        - Put closing bracket on a new line, without leading spaces.
        - Do not end complex statement with a semicolon.
        - Always use brackets, no exceptions.

    * General rules for object definitions:

        - Place the opening bracket on the same line as the object name.
        - Use colon plus one space between each property and its value.
        - Use quotes around string values, not around numeric values.
        - Do not add a comma after the last property-value pair.
        - Place the closing bracket on a new line, without leading spaces.
        - Always end an object definition with a semicolon.


Python
======

- THERE IS ONLY PYTHON 3!!! NOTHING ELSE EXISTS!!!
- The minimum Python 3 version supported is the one shipped with Ubuntu LTS versions until |EOL|.
- The maximum Python 3 version supported is the one considered by Python developers as stable.
- THERE IS ONLY PYTHON 3!!! NOTHING ELSE EXISTS!!!
- REPEAT PREVIOUS UNTIL THE END OF TIMES!!!

