import shutil

def getFreeSpace(path):
    total, used, free = shutil.disk_usage(path)
    total, used, free = total/(1024**3), used/(1024**3), free/(1024**3)
	
    noti = '' if (free > 30) else '⚠'
    return f'{noti}Free: {free:.1f}GB'
