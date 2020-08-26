import os,shutil,tqdm,wikipedia,time,webbrowser,requests,random,sys
from tqdm import tqdm as tq
def path_extractor(full_path):
    if '\\' in full_path:
        reversed_path = full_path[::-1]
        slash_pos = reversed_path.find('\\')
        reversed_file = reversed_path[:slash_pos]
        file_name = reversed_file[::-1]
        reversed_path2 = reversed_path[slash_pos+1:]
        final_path = reversed_path2[::-1]
        return file_name,final_path    
    if '/' in full_path:
        reversed_path = full_path[::-1]
        slash_pos = reversed_path.find('/')
        reversed_file = reversed_path[:slash_pos]
        file_name = reversed_file[::-1]
        reversed_path2 = reversed_path[slash_pos+1:]
        final_path = reversed_path2[::-1]
        return file_name,final_path
    file_name = full_path
    final_path = ''
    return file_name,final_path
while 1==1:
    print('\n')
    command = input(f'{os.getcwd()} >>  ')
    command = command.lower()
    actual_command = command.replace(' ','')
    print('\n')
    if actual_command == 'cwd':
        print(os.getcwd())
    if actual_command[:4]=='show':
        dot_pos = actual_command.find('.')
        extension = actual_command[dot_pos+1:]
        name = actual_command[actual_command.find('w')+1:dot_pos]
        if (actual_command=='show'):
            for files in os.listdir():
                print(files)
        if (actual_command=='show*.*') or (actual_command=='show-fi'):
            for i in os.listdir():
                if '.' in i:
                    print(i)
        if (actual_command=='show-fo'):
            for i in os.listdir():
                if '.' not in i:
                    print(i)
        if (name=='*') and (extension!='') and (extension!='*'):
            for i in os.listdir():
                if i.endswith(extension):
                    print(i)
        if (name!='') and (name!='*')  and (extension=='*'):
            for i in os.listdir():
                if i.startswith(name):
                    print(i)
    if actual_command[:2]=='mk':
        if ('"' not in command) and ("'" not in command):
            print('\nPlase specify file by using inverted commas\n')
            continue
        if '"' in command:
            if (actual_command.count('"')%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find('"')
            second_comma = 0 
            hiphen_f_range = command[2:first_comma]
            if '-f' in hiphen_f_range:
                for i in range(5000):
                    second_comma = command.find('"',first_comma+1)
                    if first_comma==-1:
                        break
                    if os.path.exists(f'{command[first_comma+1:second_comma]}'):
                        print('\nGiven file name already exists\n')
                        break
                    os.mkdir(command[first_comma+1:second_comma])
                    first_comma = command.find('"',second_comma+1)
            if '-f' not in hiphen_f_range:
                for i in range(5000):
                    second_comma = command.find('"',first_comma+1)
                    if first_comma==-1:
                        break
                    if os.path.exists(f'{command[first_comma+1:second_comma]}'):
                        print('\nGiven file name already exists\n')
                        break
                    with open(f'{command[first_comma+1:second_comma]}','w') as f:
                        f.close()
                    first_comma = command.find('"',second_comma+1)
        if "'" in command:
            if  (actual_command.count("'")%2!=0):
                print("Inverted comma is missing/extra")    
                continue
            first_comma = command.find("'")
            second_comma = 0 
            hiphen_f_range = command[2:first_comma]
            if '-f' in hiphen_f_range:
                for i in range(5000):
                    second_comma = command.find("'",first_comma+1)
                    if first_comma==-1:
                        break
                    if os.path.exists(f'{command[first_comma+1:second_comma]}'):
                        print('\nGiven file name already exists\n')
                        break
                    os.mkdir(command[first_comma+1:second_comma])
                    first_comma = command.find("'",second_comma+1)
            if '-f' not in hiphen_f_range:
                for i in range(5000):
                    second_comma = command.find("'",first_comma+1)
                    if first_comma==-1:
                        break
                    if os.path.exists(f'{command[first_comma+1:second_comma]}'):
                        print('\nGiven file name already exists\n')
                        break
                    with open(f'{command[first_comma+1:second_comma]}','w') as f:
                        f.close()
                    first_comma = command.find("'",second_comma+1)          
    if actual_command[:2]=='rm':
        if ('"' not in command) and ("'" not in command):
            print('\nPlase specify file by using inverted commas\n')
            continue
        if '"' in command:
            if (actual_command.count('"')%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find('"')
            second_comma = 0 
            for i in range(5000):
                second_comma = command.find('"',first_comma+1)
                if first_comma==-1:
                    break
                if not  os.path.exists(f'{command[first_comma+1:second_comma]}'):
                    print('\nGiven file not exists\n')
                    break
                if os.path.isdir(command[first_comma+1:second_comma]):
                    shutil.rmtree(command[first_comma+1:second_comma])
                if os.path.isfile(command[first_comma+1:second_comma]):
                    os.remove(command[first_comma+1:second_comma])
                first_comma = command.find('"',second_comma+1)
        if "'"  in command:
            if (actual_command.count("'")%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find("'")
            second_comma = 0 
            for i in range(5000):
                second_comma = command.find("'",first_comma+1)
                if first_comma==-1:
                    break
                if not  os.path.exists(f'{command[first_comma+1:second_comma]}'):
                    print('\nGiven file not exists\n')
                    break
                if os.path.isdir(command[first_comma+1:second_comma]):
                    shutil.rmtree(command[first_comma+1:second_comma])
                if os.path.isfile(command[first_comma+1:second_comma]):
                    os.remove(command[first_comma+1:second_comma])
                first_comma = command.find("'",second_comma+1)
    if actual_command[:2]=='rn':
        if ('"' not in command) and ("'" not in command):
            print('\nPlase specify file by using inverted commas\n')
            continue
        if '"' in command:
            if (actual_command.count('"')%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find('"')
            second_comma = command.find('"',first_comma+1)
            third_comma = command.find('"',second_comma+1)
            fourth_comma = command.find('"',third_comma+1)
            if not os.path.exists(command[first_comma+1:second_comma]):
                print('\nThe given file path doesn\'t exists\n')
                continue
            the_file,the_path = path_extractor(command[first_comma+1:second_comma])
            current_path = os.getcwd()
            if the_path!='':
                os.chdir(the_path)
            os.rename(f'{the_file}',f'{command[third_comma+1:fourth_comma]}')
            os.chdir(current_path)
            continue
        if "'" in command:
            if (actual_command.count("'")%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find("'")
            second_comma = command.find("'",first_comma+1)
            third_comma = command.find("'",second_comma+1)
            fourth_comma = command.find("'",third_comma+1)
            if not os.path.exists(command[first_comma+1:second_comma]):
                print('\nThe given file path doesn\'t exists\n')
                continue
            the_file,the_path = path_extractor(command[first_comma+1:second_comma])
            current_path = os.getcwd()
            if the_path!='':
                os.chdir(the_path)
            os.rename(f'{the_file}',f'{command[third_comma+1:fourth_comma]}')
            os.chdir(current_path)
            continue
    if actual_command[:2]=='cp':
        if ('"' not in command) and ("'" not in command):
            print('\nPlase specify file by using inverted commas\n')
            continue
        if '"' in command:
            if (actual_command.count('"')<4):
                print('\nGive the destination to copy the file\n')
                continue
            if (actual_command.count('"')%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find('"')
            second_comma = command.find('"',first_comma+1)
            third_comma = command.find('"',second_comma+1)
            fourth_comma = command.find('"',third_comma+1)
            if (not os.path.exists(command[first_comma+1:second_comma])) or (not os.path.exists(command[third_comma+1:fourth_comma])):
                print('\nThe given file path  doesn\'t not  exists\n')
                continue
            current_path = os.getcwd()
            the_file,the_path = path_extractor(command[first_comma+1:second_comma])
            if the_path!='':
                os.chdir(the_path)
            try:
                shutil.copytree(f'{the_file}',f'{command[third_comma+1:fourth_comma]}/{the_file}')
                os.chdir(current_path)
            except FileExistsError:
                print('\nFile already exists at the location\n')
                continue
            except NotADirectoryError:
                try:
                    shutil.copy(f'{the_file}',f'{command[third_comma+1:fourth_comma]}')
                    os.chdir(current_path)
                except PermissionError:
                    print('\nPlease run the terminal in adminstrator mode\n')
        if "'" in command:
            if (actual_command.count("'")%2!=0):
                print("Inverted comma is missing/extra")
                continue
            if (actual_command.count("'")<4):
                print('\nGive the destination to copy the file\n')
                continue
            first_comma = command.find("'")
            second_comma = command.find("'",first_comma+1)
            third_comma = command.find("'",second_comma+1)
            fourth_comma = command.find("'",third_comma+1)
            if (not os.path.exists(command[first_comma+1:second_comma])) or (not os.path.exists(command[third_comma+1:fourth_comma])):
                print('\nThe given file path  doesn\'t not  exists\n')
                continue
            current_path = os.getcwd()
            the_file,the_path = path_extractor(command[first_comma+1:second_comma])
            if the_path!='':
                os.chdir(the_path)
            try:
                shutil.copytree(f'{the_file}',f'{command[third_comma+1:fourth_comma]}/{the_file}')
                os.chdir(current_path)
            except FileExistsError:
                print('\nFile already exists at the location\n')
                continue
            except NotADirectoryError:
                try:
                    shutil.copy(f'{the_file}',f'{command[third_comma+1:fourth_comma]}')
                    os.chdir(current_path)
                except PermissionError:
                    print('\nPlease run the terminal in adminstrator mode\n')
    if actual_command[:2]=='mv':
        if ('"' not in command) and ("'" not in command):
            print('\nPlase specify file by using inverted commas\n')
            continue
        if (actual_command.count('"')<4):
                print('\nGive the destination to copy the file\n')
                continue
        if '"' in command:
            if (actual_command.count('"')%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find('"')
            second_comma = command.find('"',first_comma+1)
            third_comma = command.find('"',second_comma+1)
            fourth_comma = command.find('"',third_comma+1)
            if (not os.path.exists(command[first_comma+1:second_comma])) or (not os.path.exists(command[third_comma+1:fourth_comma])):
                print('\nThe given file path  doesn\'t not  exists\n')
                continue
            the_file,the_path = path_extractor(command[first_comma+1:second_comma])
            current_path = os.getcwd()
            if the_path!='':
                os.chdir(the_path)
            try:
                shutil.move(f'{the_file}',f'{command[third_comma+1:fourth_comma]}')
                os.chdir(current_path)
            except FileExistsError:
                print('\nFile already exists at the location\n')
                continue
            except PermissionError:
                print('\nPlease run the terminal in adminstrator mode\n')
                continue
            except shutil.Error:
                print('\nFile already exists at given destination\n')
        if "'" in command:
            if (actual_command.count("'")<4):
                print('\nGive the destination to copy the file\n')
                continue
            if (actual_command.count("'")%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find("'")
            second_comma = command.find("'",first_comma+1)
            third_comma = command.find("'",second_comma+1)
            fourth_comma = command.find("'",third_comma+1)
            if (not os.path.exists(command[first_comma+1:second_comma])) or (not os.path.exists(command[third_comma+1:fourth_comma])):
                print('\nThe given file path  doesn\'t not  exists\n')
                continue
            the_file,the_path = path_extractor(command[first_comma+1:second_comma])
            current_path = os.getcwd()
            if the_path!='':
                os.chdir(the_path)
            try:
                shutil.move(f'{the_file}',f'{command[third_comma+1:fourth_comma]}')
                os.chdir(current_path)
            except FileExistsError:
                print('\nFile already exists at the location\n')
                os.chdir(current_path)
                continue
            except PermissionError:
                    print('\nPlease run the terminal in adminstrator mode\n')
                    os.chdir(current_path)
                    continue
    if actual_command[:6]=='search':
        if actual_command[6:]=='':
            print("\nGive a topic to search\n")
            continue
        search_engine_urls = ['https://www.bing.com/search?q=','https://www.google.co.in/search?q=','https://in.search.yahoo.com/search;_ylt=AwrwSY6UO_5df1QA1RC6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA2luLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDNARxdWVyeQNpZ2kyBHRfc3RtcAMxNTc2OTQ3ODc0?fr2=sb-top-in.search&p=','https://duckduckgo.com/?q=']
        if '-' not in actual_command[:8]:
            engine_choice = random.choice(search_engine_urls)
            webbrowser.open(engine_choice+actual_command[6:])
            continue
        hiphen_pos = command.find('-')
        if actual_command[:8]=='search-g':
            if actual_command[8:]=='':
                print("\nGive a topic to search\n")
                continue
            webbrowser.open('https://www.google.co.in/search?q='+command[hiphen_pos+2:])
            continue
        if actual_command[:8]=='search-y':
            if actual_command[6:]=='':
                print("\nGive a topic to search\n")
                continue
            webbrowser.open('https://in.search.yahoo.com/search;_ylt=AwrwSY6UO_5df1QA1RC6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA2luLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMEcXN0cmwDNARxdWVyeQNpZ2kyBHRfc3RtcAMxNTc2OTQ3ODc0?fr2=sb-top-in.search&p='+command[hiphen_pos+2:])
            continue
        if actual_command[:8]=='search-b':
            if actual_command[8:]=='':
                print("\nGive a topic to search\n")
                continue
            webbrowser.open('https://www.bing.com/search?q='+command[hiphen_pos+2:])
            continue
        if actual_command[:8]=='search-d':
            if actual_command[8:]=='':
                print("\nGive a topic to search\n")
                continue
            webbrowser.open('https://duckduckgo.com/?q='+command[hiphen_pos+2:])
            continue
        else:
            print('\nInvalid command\n')
            continue
    if actual_command[:4] == 'wiki':
        if command[4:]=='':
            print('Please give a topic to search')
            continue
        try:
            summary = wikipedia.summary(command[4:])
        except wikipedia.exceptions.PageError:
            print('',f'Sorry! there is no any information related to {command[4:]}')
            continue
        except wikipedia.exceptions.DisambiguationError:
            print('',f'There are many topic related to {command[4:]}\nPlease specify')
            continue
        except:
            print('','Please check your internet connection')
            continue
        while True:
            try:
                ask = int(input("""Available options: - 
                              
                        1) Write the information in text file
                        2) Print the information in terminal 
                        
                        Choose a option: - """))
                break
            except:
                print('\nOnly integers are allowed\n')
                continue
        if ask!=1 and ask!=2:
            print("\nThere are two options only 1 and 2\n")
            continue
        if ask==1:
            location_of_text = input("\nEnter the location to save:  ")
            if location_of_text=='':
                print("\nGive a location to save\n")
                continue
            if not os.path.exists(location_of_text):
                print("\nPath not exists\n")
                continue
            name_of_txt_file = input("\nGive a name to the text file: ")
            with open(f'{location_of_text}/{name_of_txt_file}.txt' ,'w',encoding='utf-8') as txt:
                txt.write(summary)
                print("\nFile written\n")
        if ask==2:
            print("\n"+summary)
    if actual_command[:8] =='download':
        for i in tq(range(100)):
            time.sleep(0.1)
    if actual_command[:4] == 'open':
        if ('"' not in command) and ("'" not in command):
            print('\nPlase specify file by using inverted commas\n')
            continue
        if '"' in command:
            if (actual_command.count('"')%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find('"')
            second_comma = 0 
            for i in range(5000):
                second_comma = command.find('"',first_comma+1)
                if first_comma==-1:
                    break
                if not  os.path.exists(f'{command[first_comma+1:second_comma]}'):
                    print('\nGiven file not exists\n')
                    break
                os.startfile(command[first_comma+1:second_comma])
                first_comma = command.find('"',second_comma+1)
        if "'"  in command:
            if (actual_command.count("'")%2!=0):
                print("Inverted comma is missing/extra")
                continue
            first_comma = command.find("'")
            second_comma = 0 
            for i in range(5000):
                second_comma = command.find("'",first_comma+1)
                if first_comma==-1:
                    break
                if not  os.path.exists(f'{command[first_comma+1:second_comma]}'):
                    print('\nGiven file not exists\n')
                    break
                os.startfile(command[first_comma+1:second_comma])
                first_comma = command.find("'",second_comma+1)
    if actual_command=='clear':
        os.system('cls')
    if actual_command == 'exit':
        break
    if (actual_command[:4]!='show') and (actual_command!='exit') and (actual_command[:3]!='cwd') and (('\\'  not in command) and ('/' not in command )) and (actual_command[:2]!='mk') and (actual_command[:2]!='rm') and (actual_command[:2]!='rn') and (actual_command[:2]!='mv') and (actual_command[:2]!='cp') and (actual_command[:6]!='search') and (actual_command[:4]!='wiki') and (actual_command[:8]!='download') and (actual_command[:4]!='open') and (actual_command!='clear'):
        os.system(command)
        continue
    if  (actual_command[:4]!='show') and ('exit' not in command) and ('cwd' not in command) and (('\\' in command) or ('/' in command )) and ('mk' not in command) and ('rm' not in command) and ('rnm' not in command) and ('mv' not in command) and ('cp' not in command) and ('search' not in command) and ('wiki' not in command) and ('download' not in command) and ('open' not in command) and ('clear' not in command):
        if not os.path.exists(command):
            print('Path doesn\'t exists')
        if os.path.exists(command):
            os.chdir(command)
    continue