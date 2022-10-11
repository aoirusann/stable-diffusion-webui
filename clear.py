import os.path
import shutil

def ClearCache():
	cache_dirs = []
	# out
	cache_dirs.extend([
		r"outputs/img2img-grids",
		r"outputs/img2img-images",
		r"outputs/txt2img-grids",
		r"outputs/txt2img-images",
	])
	# log
	cache_dirs.extend([
		r"log/images",
	])
	# textual inversion
	cache_dirs.extend([
		r"textual_inversion",
	])

	for cache_dir in cache_dirs:
		print("Cleaning " + cache_dir + "...")
		shutil.rmtree(cache_dir)

if __name__ == "__main__":
	if not os.path.exists("webui.bat"):
		print("Call `clear.py` in stable-diffusion-webui's root dir.")
	else:
		ClearCache()
		print("Cleared.")



