import os

def filter_logs(path_out,filter:str):
    
    if filter == '':
        return
    
    filters = filter.split(",")

    if os.getenv('FLASK_DEBUG'):
        print("text filter:")
        for x in filters:
            print(f" - \"{x}\"")

    dir_list = os.listdir(path_out)

    for f in dir_list:
        log_file = ''
        
        with open(f'{path_out}/{f}', 'r') as file:
            
            for i in file:
                for x in filters:
                    if x in i:
                       break
                else:
                    log_file = f"{log_file}" + f"{i}"

        
        os.remove(f'{path_out}/{f}')
        
        with open(f'{path_out}/{f}', "w") as file:
            file.write(log_file)




filter_logs(path_out='./data',filter="[ServerMain/INFO],[Server thread/WARN]")