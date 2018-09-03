import shutil
import os.path


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
DATABASE_RASPI_FOLDER = 'C:/Users/eshm02/Personal/Python/Raspi'
DATABASE_PC_FOLDER = 'C:/Users/eshm02/Personal/Python/Pc'

# -------------------------
# Main
# -------------------------
src=os.path.join(DATABASE_RASPI_FOLDER,DATABASE_FILE_NAME)
dst=os.path.join(DATABASE_PC_FOLDER,DATABASE_FILE_NAME)

shutil.copy2(src, dst)
