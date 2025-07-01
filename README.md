# epistolary-formatter

This program formats an [epistolary](https://en.wikipedia.org/wiki/Epistolary_novel) in a .txt file to a format that is visually similar to two people texting. The file created is a HTML table meant to be compatible for viewing on AO3. This currently only accomodates two speakers, and must follow the format shown in the sample input text. Future plans may include catering to multiple speakers with the speaker's name right above their dialogue

## How to use:
1. In Command Prompt, navigate to the folder you downloaded this file and run ``` python main.py```.
2. When prompted, enter info such as the EXACT name of the file your are trying to format in ```input filename```, the name of the file the program creates in ```output filename```, and the names of the speakers in ```left_speaker``` and ```right_speaker``` (not case sensitive)
3. Once the program is done running, go to the folder where you downloaded this program. You can see how your formatted text looks by double clicking the created file, or view the code by opening it in with any text editor program you have.

**Example of input**

```
John: Hi there!
Jane: Hi John!
John: Nice to meet you. Are we two characters texting each other in a chunk of sample text?
Jane: Yes, that's right.
Jane: Multiple lines said by a character will turn out like this. These lines are longer to show how the text doesn't bleed into the other speaker's section of the page.
John: Cool.
```
<br/>**Viewing output file in a browser**

![Text from both speakers aligned to either left or right of the page](https://i.postimg.cc/ydJWKtgz/convobrowser.png)

<br/>**Viewing preview on AO3**

![Text from both speakers aligned to either left or right of the page](https://i.postimg.cc/RFjhZdKJ/convoplatform.png)

<br/>**Example of output**

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
<hr/>

**Notes/design justifications:**
- This only accepts txt files for ease of processing. The more commonly used .docx extention would require users to install a package.
- The code uses the depreciated HTML5 attribute 'align' instead of 'text-align' because the platform this code is for only recognises that.
- User HAS to key in the file extension when typing the input file name because they can then see immediately whether they have the wrong file format.
- Work skins on AO3 are an alternative, but they are mainly for more detailed aesthetics and you still have to assign which style applies to which line of text. I just wanted simple text alignment, and I wanted to save time on assigning every single line of text, hence this code.
