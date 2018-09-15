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
	for file in DATABASE_FILES_TO_COPY:
		if (os.path.isfile(os.path.join(dstFolder,file))):
			print("Deleting ",os.path.join(dstFolder,file))
			os.remove(os.path.join(dstFolder,file))
		shutil.copy(os.path.join(srcFolder,file), dstFolder)

	return None
	
def switchFolders(srcFolder, dstFolder):
	#dstFolder is newer, srcFolder needs to be updated. We switch p
	temp=srcFolder
	srcFolder=dstFolder
	dstFolder=temp
	return None
	
def getLastModificationTime(folder):
	lastTime=0
	for file in DATABASE_FILES_TO_COPY:
		filePath=os.path.join(folder,file)
		if os.path.isfile(filePath) and os.stat(filePath).st_mtime > lastTime:
			lastTime = os.stat(filePath).st_mtime		
	return lastTime
	
# -------------------------
# Config
# -------------------------
DATABASE_SYSTEM_FOLDER = r'/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/'
DATABASE_EXDISK_FOLDER = r'/mnt/volume/plexmediaserver/Plex Media Server/Plug-in Support/Databases'
#DATABASE_SYSTEM_FOLDER = './Pc'
#DATABASE_EXDISK_FOLDER = './Raspi'
DATABASE_FILES_TO_COPY = ['com.plexapp.plugins.library.db','com.plexapp.plugins.library.blobs.db-shm','com.plexapp.plugins.library.db-wal','com.plexapp.plugins.library.db-shm']

# -------------------------
# Main
# -------------------------
stopServer()

srcFolder=DATABASE_SYSTEM_FOLDER
dstFolder=DATABASE_EXDISK_FOLDER

diff_time = getLastModificationTime(srcFolder) - getLastModificationTime(dstFolder)

if diff_time < 0:
	switchFolders(srcFolder,dstFolder)
	
if diff_time == 0:
	print("No changes in database. Nothing to be done.")
else:
	print("Copy from source: ", srcFolder)
	print("to destination: ", dstFolder)
	updateDatabase(srcFolder, dstFolder)

startServer()
	
sys.exit(0)
