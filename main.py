def bottles_of_beer(start, end):

    if (start >= 100) or (end < 0) or (start < end):
        return "Invalid range of bottles."

    def normal_verse(bottle):
        verse = f"{bottle} bottles of beer on the wall,\n{bottle} bottles of beer.\nTake one down, pass it around,\n{bottle-1} {'bottles' if bottle -1 > 1 else 'bottle'} of beer on the wall.\n\n"
        return verse

    def singular_verse(bottle):
        verse = f"{bottle} bottle of beer on the wall,\n{bottle} bottle of beer.\nTake one down, pass it around,\nNo bottles of beer on the wall.\n\n"
        return verse

    def zero_verse(start_bottle):
        verse = f"No bottles of beer on the wall,\nNo bottles of beer.\nGo to the store, buy some more,\n{start_bottle} bottles of beer on the wall."
        return verse

    song = ""
    for n in range(start, end, -1):
        if n > 1:
            song += normal_verse(n)
        
        if n == 1:
            song += singular_verse(n)

    if end == 0:
        song += zero_verse(start)


    return song.strip()
