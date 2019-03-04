import subprocess
import os
shapes = ['1.png','1.png', '1.png','1.png', '1.png','1.png', '1.png',
          '2.png','2.png','2.png','2.png','2.png','2.png','2.png',
          '3.png', '3.png', '3.png','3.png','3.png','3.png','3.png',
          '4.png', '4.png', '4.png', '4.png', '4.png', '4.png', '4.png',
          '5.png', '5.png', '5.png', '5.png', '5.png', '5.png', '5.png',
          '6.png', '6.png', '6.png', '6.png', '6.png', '6.png', '6.png', ]

os.system('convert -delay 0 -dispose Background +page -loop 4 %s anime.gif' % ' '.join(shapes))
