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

def updateDatabase(srcFolder, dstFolder):
	return None
def switchFolders(srcFolder, dstFolder):
	#dstFolder is newer, srcFolder needs to be updated. We switch p
	temp=srcFolder
	srcFolder=dstFolder
	dstFolder=temp
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

srcFolder=DATABASE_SYSTEM_FOLDER
dstFolder=DATABASE_EXDISK_FOLDER

diff_time = os.stat(os.path.join(srcFolder,DATABASE_FILE_NAME)).st_mtime - os.stat(os.path.join(dstFolder,DATABASE_FILE_NAME)).st_mtime

if diff_time < 0:
	switchFolders(srcFolder,dstFolder)
	
if diff_time == 0:
	print("No changes in database. Nothing to be done.")
else:
	print("Copy from source: ", srcFolder)
	print("to destination: ", dstFolder)
	#El copy no me lo esta haciendo bien, al menos no parece verse actualizado:
	updateDatabase(srcFolder, dstFolder)
	#shutil.copy2(srcFolder, dstFolder)
	#os.system("cp -f "+srcFolder+" "+dstFolder)

startServer()
	
sys.exit(0)
