import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

a = "Lee Minji"

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix(c)
