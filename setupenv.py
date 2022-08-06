import yaml
import os

# load yamel file into dictionary
tools = yaml.full_load(open('./conf/tools.yml', 'r'))

# read install folder and remove (key,value) pair
install_folder  = tools["TOOLS_PATH"]
del tools["TOOLS_PATH"]

# Make install folder if not present
if os.path.isdir(install_folder) == False:
    os.mkdir(install_folder)
    
os.chdir(install_folder)

for key in tools:
    # install tool if not already present
    if os.path.isdir(tools[key]['dir']) == False:
        
        print(f"\n")
        print(f"Installing {key}")
        print(f"name    : {tools[key]['name']}")
        print(f"version : {tools[key]['version']}")
        print(f"file    : {tools[key]['file']}")
        
        if tools[key]['file'] == "archive":
            
            if tools[key]['type'] == "tar":
                # download archive, extract and remove
                os.system(f"wget {tools[key]['url']} -q --show-progress")
                os.system(f"tar -xf {tools[key]['archive']}")
                os.remove(f"./{tools[key]['archive']}")
                
        elif tools[key]['file'] == "repos":
            
            if tools[key]['type'] == "svn":
                # check out svn repos into specified folders
                os.system(f"svn checkout {tools[key]['url']} {tools[key]['dir']}")
        
        # Execute extra commands if present
        if 'command' in tools[key]:

            for cmd in tools[key]['command']:
                
                print(f"Executing {cmd}:")
                
                # change path if requested and run command
                if 'path' in tools[key]['command'][cmd]:
                    os.chdir(tools[key]['command'][cmd]['path'])
                    os.system(tools[key]['command'][cmd]['run'])
                    os.chdir(install_folder)
                else:
                    os.system(tools[key]['command'][cmd]['run'])