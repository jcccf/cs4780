import sys

# Create a Command-line progress bar that updates on the same line
# Untested on Windows machines
class ProgressBar:
  
  def __init__(self):
    self.text = '[' + ' ' * 50 + '] 0%'
    
  def update(self, percent, message):
    num_dashes = int(percent * 100 / 2)
    num_spaces = 50 - num_dashes
    self.text = '[' + '-' * num_dashes + ' ' * num_spaces + '] ' + str(int(percent*100)) + '% ' + message
    sys.stdout.write(self.text+'\r')
    sys.stdout.flush()
    if percent == 1.0:
      sys.stdout.write('\n')
    
  def __str__(self):
    return self.text