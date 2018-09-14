import shutil
import os
import sys





#Stop server
#sudo /etc/init.d/plexmediaserver stop

#Copy databases
#cp -rf /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plug-in\ Support/Databases/*.db /mnt/volume/plexmediaserver/Plex\ Media\ Server/Plug-in\ Support/Databases

#Start server
#sudo /etc/init.d/plexmediaserver start

# -------------------------
# Config
# -------------------------
DATABASE_FILE_NAME = 'database.dat'
DATABASE_RASPI_FOLDER = 'C:/Users/eshm02/Personal/PlexUpdater/Raspi'
DATABASE_PC_FOLDER = 'C:/Users/eshm02/Personal/PlexUpdater/Pc'

# -------------------------
# Main
# -------------------------
src=os.path.join(DATABASE_RASPI_FOLDER,DATABASE_FILE_NAME)
dst=os.path.join(DATABASE_PC_FOLDER,DATABASE_FILE_NAME)

diff_time = os.stat(src).st_mtime - os.stat(dst).st_mtime

if diff_time < 0:
	#dst is newer, src needs to be updated. We switch p
	temp=src
	src=dst
	dst=temp
	
if diff_time == 0:
	print("No changes in database. Nothing to be done.")
else:
	print("Copy from source: ", src)
	print("to destination: ", dst)
	shutil.copy2(src, dst)
sys.exit(0)
