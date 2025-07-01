def format_story(input_file, output_file, left_speaker, right_speaker):
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    with open(output_file, 'w') as f:
        f.write('<table>\n<tbody>\n')

        for line in lines:
            if ':' not in line:
                continue

            speaker, dialogue = line.split(':', 1)
            speaker_clean = speaker.strip().lower()
            dialogue = dialogue.strip()

            if speaker_clean == left_speaker.lower():
                f.write(f'<tr>\n<td width="25%" align="left">{dialogue}</td>\n<td width="50%"></td>\n<td width="25%"></td>\n</tr>\n<tr>\n<td></td>\n</tr>\n')
            elif speaker_clean == right_speaker.lower():
                f.write(f'<tr>\n<td width="25%"></td>\n<td width="50%"></td>\n<td width="25%" align="right">{dialogue}</td>\n</tr>\n<tr>\n<td></td>\n</tr>\n')
            else:
                # Default to centre if speaker is unknown/line is not dialogue
                f.write(f'<tr align="center">{dialogue}</tr>')

        f.write('</tbody>\n</table>\n')

    print(f"\nFormatting completed. If text is center-aligned when it shouldn't be, check for typos in speaker names.")

def main():
    print("Enter the required information:")
    input_file = input("Input filename (e.g. story.txt): ").strip()
    try:
        open_file = open(input_file, "r")
    except:
        print(f"The file '{input_file}' was not found. Please try again.")
        input_file = input("Input filename (e.g. story.txt): ").strip()
    output_file = input("Output filename (e.g. story.html): ").strip()
    left_speaker = input("Left speaker: ").strip()
    right_speaker = input("Right speaker: ").strip()

    format_story(input_file, output_file, left_speaker, right_speaker)

if __name__ == '__main__':
    main()