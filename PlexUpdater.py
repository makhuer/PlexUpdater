import shutil
import os
import sys


def stopServer():
	print("Stoping server in Platform: ", sys.platform)
	if sys.platform == "win32" :
		#TODO
		print("Stoping windows server...")
	elif sys.platform == "linux2":
		os.system("sudo /etc/init.d/plexmediaserver stop")
	return None

def startServer():
	print("Starting server in platform: ", sys.platform)
	if sys.platform == "win32":
		#TODO
		print("Starting windows server...")
	elif sys.platform == "linux2":
		os.system("sudo /etc/init.d/plexmediaserver start")
	return None


# -------------------------
# Config
# -------------------------
DATABASE_FILE_NAME = 'com.plexapp.plugins.library.db'
DATABASE_SYSTEM_FOLDER = r'/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/'
DATABASE_EXDISK_FOLDER = r'/mnt/volume/plexmediaserver/Plex Media Server/Plug-in Support/Databases'

# -------------------------
# Main
# -------------------------
stopServer()

src=os.path.join(DATABASE_SYSTEM_FOLDER,DATABASE_FILE_NAME)
dst=os.path.join(DATABASE_EXDISK_FOLDER,DATABASE_FILE_NAME)

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
	#os.system("cp -f "+src+" "+dst)

startServer()
	
sys.exit(0)
