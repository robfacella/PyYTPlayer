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
print ("[***]Warning, used to occasionally write 2 lines together..")
print ("[???]Believe that to be fixed, instead we now leave up to 2 blank lines in the document (one just as \"\\n\" the other \"\" ) but error checking in the runner effectively ignores these in the queue anyway.")
