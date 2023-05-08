
# The Ultimate Macro Language

## About

I was bored so i made this

Its a macro language that is ran using Python

how to use/learn
>1. read basic syntax
>2. read command list for descriptions
>3. read more info on commands in other collapsed sections
>4. extra examples are the example_macro.macro file
>5. download source(***requires pyqutogui***) or [latest release](https://github.com/Cooperzilla/Macro-Language/releases/tag/1.dev)
>6. configure macro.macro
>7. run main.py or the exe

Todo:
>- [X] figure out how to compile
>- [X] add more hotkey functions

## Documentation
<details>
<summary>Basic Syntax</summary>

>(command)/(parameters)/(more parameters)
>
>examples:
>- move/x/500
>- click/2
>- type/hello world!
</details>
<details>

<summary>list of commands</summary>

- mouse movement
    >- move - modify the x or y of the mouse
    >- goto - set yhe x and y of the mouse
    >- setpos - set the x or y of the mouse
- mouse usage
    >- click - click left/right/middle once or twice
    >- scroll - scroll so many clicks
    >- mousedown - clicks with the mouse but stays down until mouseup
    >- mouseup - un-clicks the mouse from mousedown
- keyboard
    >- key - press a key
    >- type - type in words
    >- hotkey - use a ctrl hotkey
    >- keydown - presses with the key but stays down until keyup
    >- keyup - un-presses the mouse from mousedown
    >- extra hotkeys (most of these have obvious uses)
    >>- copy - copy file or text
    >>- paste - paste file or text
    >>- cut - cut a file or text
    >>- delete - delete a file or text
    >>- selectall - select all text
    >>- undo - undo last key press or hotkey
    >>- redo - undo last undo
- Screen
    >- screenshot - takes a screenshot
    >- Alert - pops up a message
    >- getscreen - pops uop a message with your screen size
    >- getpos - pops up a message with your mouse posistion
- Commands
    >- execute - execute a command line command
    >- start - start running a proggram
- miscellaneous
    >- comment (// or #) - comment
    >- wait - pause the code

    extra information below
</details>

<details>
<summary>Mouse movement</summary>

<details>
<summary>move</summary>

>usage - move/(x or y)/(number)
>
>example - move/x/400
>
>advanced - move/random/(nothing, up, down, left, right)
>
>alternative - move/(x or y)/random/(nothing if x left/right if y up/down)
>
>>examples:
>>- move/x/random
>>- move/x/random/left
>>- move/random/up
>>- move/y/random
</details>


<details>
<summary>goto</summary>

>usage - goto/(x number)/(y number)
>
>>examples:
>>- goto/300/20
>>- goto/400/1000
>
>TODO implement random
</details>

<details>
<summary>setpos</summary>

>usage - setpos/(x or y)/(number)
>
>>examples
>>- setpos/x/999
>>- setpos/y/44
>>- setpos/y/500
</details>
</details>

<details>
<summary>Mouse usage</summary>

<details>
<summary>click</summary>

>usage click/(left, right, or middle)/(1 or 2)
>
>>examples:
>>- click/left/1
>>- click/left/2
>>- click/right/1
>>-click/middle/2
</details>

<details>
<summary>scroll</summary>

>usage scroll/(number)
>
>>examples:
>>- scroll/10
>>- scroll/2
</details>

<details>
<summary>mousedown</summary>

>usage mousedown/
>
>>examples:
>>- mousedown
</details>

<details>
<summary>mouseup</summary>

>usage mouseup
>
>>examples:
>>- mouseup
</details>

</details>

<details>
<summary>Keyboard</summary>

<details>
<summary>key</summary>

>usage - key/(a key)
>
>>examples:
>>- key/a
>>- key/y
>>- key/space
</details>

<details>
<summary>type</summary>

>usage - type/(message)
>
>>examples:
>>- type/hello world
>>- type/this is a message
>>- type/hello
</details>

<details>
<summary>keydown</summary>

>usage keydown/(key)
>
>>examples:
>>- keydown/w
>>- keydown/ctrl
</details>

<details>
<summary>keyup</summary>

>usage keyup(key)
>
>>examples:
>>- keyup/w
>>- keydown/ctrl
</details>

<details>
<summary>hotkey</summary>

>usage - hotkey/(a extra key ex: ctrl)/(a key)
>
>>examples:
>>- hotkey/ctrl/v
>>- hotkey/ctrl/z
>>- hotkey/alt/tab
</details>

</details>

<details>
<summary>Hotkeys</summary>

<details>
<summary>copy</summary>

>usage - copy
>
>>examples:
>>- copy
</details>
<details>
<summary>paste</summary>

>usage - paste
>
>>examples:
>>- paste
</details>

<details>
<summary>cut</summary>

>usage - cut
>
>>examples:
>>- cut
</details>
<details>
<summary>undo</summary>

>usage - undo
>
>>examples:
>>- undo
</details>

<details>
<summary>redo</summary>

>usage - redo
>
>>examples:
>>- redo
</details>

<details>
<summary>selectall</summary>

>usage - selectall
>
>>examples:
>>- selectall
</details>

<details>
<summary>delete</summary>

>usage - delete
>
>>examples:
>>- delete
</details>

</details>


<details>
<summary>Screen</summary>

<details>
<summary>screenshot</summary>

>usage - screenshot/(file for this to be saved)
>
>>examples:
>>- screenshot/my_screenshot.png
>>- screenshot/image.png
>>- screenshot/file.png
>
>I know png files work I am not sure about other file types
</details>

<details>
<summary>alert</summary>

>usage - alert/(title)/(text)/(optional button name)
>
>>examples:
>>- alert/info/this is infornation
>>- alert/title/infornation/ok
>>- alert/this is a title/infornation or something/conform
</details>

<details>
<summary>getscreen</summary>

>usage - getscreen
>
>>examples:
>>- getscreen
</details>

<details>
<summary>getpos</summary>

>usage - getpos
>
>>examples:
>>- getscreen
</details>
</details>

<details>
<summary>Commands</summary>

<details>
<summary>Execute</summary>

>usage execute/(command)
>
>>examples:
>>- execute/echo hello world!
>>- execute/pip install numpy
>>- execute/npm init
>
>***Experimental may not work***
</details>

<details>
<summary>start</summary>

>usage start/(proggram)
>
>>examples:
>>- start/minecraft
>>- start/code
>>- start/cmd
>
>***Experimental may not work***
</details>

</details>


<details>
<summary>Miscellaneous</summary>

<details>
<summary>comment</summary>

>usage - // or #
>
>>examples:
>>- // this is a comment
>>- '# this is also a comment'
</details>

<details>
<summary>wait</summary>

>usage - wait/(number)
>
>>examples:
>>- wait/6
>>- wait/2
>>- wait/20
</details>

</details>

## Technical details

This works by reading the macro.macro file and then goes line by line and

depending on the 1st thing before the / it executes code using pyautogui

Below is a flow chart to explain it (does not render on mobile)

```mermaid
---
title: Flowchart to explain code
---
flowchart TD
    A(file) --> B(code)
    B --> C(execute line)
    C --> D{is done}
    D -- yes --> F(code compleat)
    D -- no --> C
```

## Git graph
I added because idk (does not render on mobile)

```mermaid
---
title: My git graph
---
gitGraph
    commit
    branch LICENSE
    commit
    checkout main
    merge LICENSE
    commit
    commit
    commit
    commit
    commit
    commit
    commit
```
