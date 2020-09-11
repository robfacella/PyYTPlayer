import os
playlistFile = open(os.path.join('playlist.txt'))
playlist = playlistFile.readlines()
playlistFile.close()

newPlaylist = set()
#unique = []
unique = 0
dupes = 0
for x in playlist:
    if x not in newPlaylist:
        #unique.append(x)
        unique = unique + 1
        newPlaylist.add(x)
    else:
        dupes = dupes + 1
print("Non-duplicate items: " + str(unique))
#print(unique)
playlistFile = open(os.path.join('playlist.txt'), 'w')
for line in newPlaylist:
	playlistFile.write(line)
playlistFile.write("")
playlistFile.close()

print ("Removed "+ str(dupes) +" Duplicates.")
print ("[***]Warning, sometimes writes 2 lines together..")
print ("[??]Have only seen it occur on one line per use, and only when removing duplicate entries; it's probably a relatively easy fix but so is manually scanning the text file of under 200 lines for the line twice as long as the others to split.")
