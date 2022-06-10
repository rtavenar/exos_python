import sys

class StdoutCollector:
    def __init__(self):
        self.data_list = []
        
    def __enter__(self):
        self.stdoutbak = sys.stdout
        sys.stdout = self
        return self
        
    def __exit__(self, *args):
        sys.stdout = self.stdoutbak
        
    def write(self, data=''):
        self.data_list.append(str(data))

    def flush(self):
        pass
        
    def get_output(self):
        return ''.join(self.data_list)
        
def done():
    f = open('.passed.json', 'w')
    f.close()

def grade():
    collector = StdoutCollector()
    with collector:
        import main
    try:
        main.bot
    except:
        print('(X) It seems like you do not have "bot" in your code!')
        return
    if main.bot.position_log != zigzag_log:
        print('(X) It seems like your bot did not move exactly like in the example!')
        return
    print('(V) Well done!')
    done()
    
grade()