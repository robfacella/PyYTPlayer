import os
playlistFile = open(os.path.join('playlist.txt'))
playlist = playlistFile.readlines()
playlistFile.close()

newPlaylist = set()
#unique = []
unique = 0
for x in playlist:
    if x not in newPlaylist:
        #unique.append(x)
        unique = unique + 1
        newPlaylist.add(x)
print("Non-duplicate items: " + str(unique))
#print(unique)
playlistFile = open(os.path.join('playlist.txt'), 'w')
for line in newPlaylist:
	playlistFile.write(line)
playlistFile.close()

print ("Removed Duplicates.")
print ("[***]Warning, sometimes writes 2 lines together..")
