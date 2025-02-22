import subprocess
import random
import shutil
import time
from terminaltexteffects.effects.effect_beams import Beams
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_bouncyballs import BouncyBalls
from terminaltexteffects.effects.effect_binarypath import BinaryPath
from terminaltexteffects.effects.effect_blackhole import Blackhole
from terminaltexteffects.effects.effect_spotlights import Spotlights
from terminaltexteffects.effects.effect_vhstape import VHSTape
from terminaltexteffects.effects.effect_waves import Waves

from terminaltexteffects.effects.effect_bubbles import Bubbles
from terminaltexteffects.effects.effect_colorshift import ColorShift
from terminaltexteffects.effects.effect_crumble import Crumble
from terminaltexteffects.effects.effect_decrypt import Decrypt
from terminaltexteffects.effects.effect_errorcorrect import ErrorCorrect
from terminaltexteffects.effects.effect_expand import Expand
from terminaltexteffects.effects.effect_fireworks import Fireworks
from terminaltexteffects.effects.effect_middleout import MiddleOut
from terminaltexteffects.effects.effect_orbittingvolley import OrbittingVolley
from terminaltexteffects.effects.effect_overflow import Overflow
from terminaltexteffects.effects.effect_pour import Pour
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.effects.effect_rain import Rain
from terminaltexteffects.effects.effect_random_sequence import RandomSequence
from terminaltexteffects.effects.effect_rings import Rings
from terminaltexteffects.effects.effect_scattered import Scattered
from terminaltexteffects.effects.effect_slice import Slice
from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.effects.effect_spray import Spray
from terminaltexteffects.effects.effect_swarm import Swarm
from terminaltexteffects.effects.effect_synthgrid import SynthGrid
from terminaltexteffects.effects.effect_unstable import Unstable
from terminaltexteffects.effects.effect_wipe import Wipe


# 1. Carregar a arte ASCII da caveira
with open('anony', 'r') as file:
    ascii_art = file.readlines()


# 2. Capturar a saída do neofetch
neofetch_output = subprocess.run(
    ['neofetch', '--color_blocks', 'off', '--color', 'off', 
     '--disable', 'host', 
     '--disable', 'os', 
     '--disable', 'packages', 
     '--disable', 'resolution', 
     '--disable', 'de', 
     '--disable', 'theme', 
     '--disable', 'icons', 
     '--disable', 'wm_theme', 
     '--disable', 'gpu', 
     '--stdout'],
    stdout=subprocess.PIPE,
    text=True
).stdout.splitlines()


time.sleep(0.1)
# 3. Calcular a largura da tela e o padding à esquerda
term_size = shutil.get_terminal_size()
term_width = term_size.columns

# Assumir que queremos que o conteúdo ocupe uma largura máxima de 100 caracteres
content_width = 100
left_padding = (term_width - content_width) // 2

# 4. Combinar a arte ASCII com a saída do neofetch
combined_output = []
max_art_lines = len(ascii_art)

for i in range(max(len(ascii_art), len(neofetch_output))):
    art_line = ascii_art[i].rstrip() if i < max_art_lines else ''
    neofetch_line = neofetch_output[i] if i < len(neofetch_output) else ''
    
    # Ajustar o comprimento das linhas para o mesmo tamanho
    art_line = art_line.ljust(50)
    combined_line = f"{art_line} {neofetch_line}"
    
    # Adicionar padding à esquerda
    padded_line = ' ' * left_padding + combined_line
    
    # Adicionar padding à direita até o final do terminal e incluir o caractere |
    final_line = padded_line.ljust(term_width - 1) + '|'
    
    combined_output.append(final_line)

# Combinar tudo em um único conteúdo com alinhamento ao meio da tela horizontalmente
conteudo = "\n".join(combined_output)

# 5. Aplicar um efeito visual aleatório
effects = [
    Beams(conteudo),
    BouncyBalls(conteudo),
    BinaryPath(conteudo),
    Burn(conteudo),
    Blackhole(conteudo),
    Spotlights(conteudo),
    VHSTape(conteudo),
    Waves(conteudo),
    Bubbles(conteudo),
    ColorShift(conteudo),
    Crumble(conteudo),
    Decrypt(conteudo),
    ErrorCorrect(conteudo),
    Expand(conteudo),
    Fireworks(conteudo),
    MiddleOut(conteudo),
    OrbittingVolley(conteudo),
    Overflow(conteudo),
    Pour(conteudo),
    Print(conteudo),
    Rain(conteudo),
    RandomSequence(conteudo),
    Rings(conteudo),
    Scattered(conteudo),
    Slice(conteudo),
    Slide(conteudo),
    Spray(conteudo),
    Swarm(conteudo),
    SynthGrid(conteudo),
    Unstable(conteudo),
    Wipe(conteudo)
]

# Escolhe um efeito aleatoriamente
effect = random.choice(effects)

# Executa o efeito escolhido
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)

time.sleep(3)
