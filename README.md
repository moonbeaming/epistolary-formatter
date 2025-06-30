# epistolary-formatter

This program formats an [epistolary](https://en.wikipedia.org/wiki/Epistolary_novel) in a .txt file to a format that is visually similar to two people texting. The file created is a HTML table meant to be compatible for viewing on AO3.

## How to use:
1. In Command Prompt, navigate to the folder you downloaded this file and run ``` python format_story.py```.
2. When prompted, enter info such as the name of the file your are trying to format in ```input filename```, the name of the file the program creates in ```output filename```, and the names of the speakers in ```left_speaker``` and ```right_speaker```
3. Once the program is done running, go to the folder where you downloaded this program. You can see how your formatted text looks by double clicking the created file, or view the code by opening it in with any text editor program you have.

Example of input

```
John: Hi there!
Jane: Hi John!
John: Nice to meet you. Are we two characters texting each other in a chunk of sample text?
Jane: Yes, that's right.
Jane: Multiple lines said by a character will turn out like this. These lines are longer to show how the text doesn't bleed into the other speaker's section of the page.
John: Cool.
```
Viewing output file in a browser
insert convo browser image here later

Preview on AO3
convo result image

Example of output

```
<table>
<tbody>
<tr>
<td width="25%" align="left">Hi there!</td>
<td width="50%"></td>
<td width="25%"></td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td width="25%"></td>
<td width="50%"></td>
<td width="25%" align="right">Hi John!</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td width="25%" align="left">Nice to meet you. Are we two characters texting each other in a chunk of sample text?</td>
<td width="50%"></td>
<td width="25%"></td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td width="25%"></td>
<td width="50%"></td>
<td width="25%" align="right">Yes, that's right.</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td width="25%"></td>
<td width="50%"></td>
<td width="25%" align="right">Multiple lines said by a character will turn out like this. These lines are longer to show how the text doesn't bleed into the other speaker's section of the page.</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td width="25%" align="left">Cool.</td>
<td width="50%"></td>
<td width="25%"></td>
</tr>
<tr>
<td></td>
</tr>
</tbody>
</table>
```
