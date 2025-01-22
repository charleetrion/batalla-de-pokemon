import time
import numpy as np
import sys

# imprimir con demora
def imprimir_con_demora(s):
    # imprimir una letra a la vez
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)
        