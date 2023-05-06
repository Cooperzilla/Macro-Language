
# The Ultimate Macro Language

## About

I was bored so i made this

Its a macro language that is ran using Python

**Requires the pip module pyautogui**

how to use/learn
>1. read basic syntax
>2. read command list for descriptions
>3. read more info on commands in other collapsed sections
>4. extra examples is macro.macro file
>5. write your macro in macro.macro file and run main.py

Todo:
>- figure out how to compile
>- add more hotkey functions

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
    >- click - click once or twice
- keyboard
    >- key - press a key
    >- type - type in words
    >- hotkey - use a ctrl hotkey
    >- copy - copy text
    >- paste - paste text
- miscellaneous
    >- execute - execute a command line command
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

>usage click/(1 or 2)
>
>>examples:
>>- click/1
>>- click/2
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
<summary>hotkey</summary>

>usage - hotkey/(a extra key ex: ctrl)/(a key)
>
>>examples:
>>- hotkey/ctrl/v
>>- hotkey/ctrl/z
>>- hotkey/alt/tab
</details>

<details>
<summary>paste</summary>

>usage - paste
>
>>examples:
>>- paste
</details>

<details>
<summary>copy</summary>

>usage - copy
>
>>examples:
>>- copy
</details>

</details>

<details>
<summary>Miscellaneous</summary>

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
<summary>Comment</summary>

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
