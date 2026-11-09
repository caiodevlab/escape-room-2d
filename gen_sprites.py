
import os
from PIL import Image, ImageDraw

sprites_dir = "/home/administrador/Documentos/projetos/escape-room-2d/assets/sprites"
os.makedirs(sprites_dir, exist_ok=True)

# 1. Piso de Ladrilho Escolar (64x64 com grade nítida para pixel art)
floor = Image.new("RGBA", (64, 64), (70, 75, 85, 255))
d = ImageDraw.Draw(floor)
d.rectangle([0, 0, 63, 63], outline=(50, 55, 65), width=2)
d.line([0, 32, 63, 32], fill=(55, 60, 70), width=1)
d.line([32, 0, 32, 63], fill=(55, 60, 70), width=1)
floor.save(os.path.join(sprites_dir, "school_floor.png"))

# 2. Parede Escolar com rodapé (64x64)
wall = Image.new("RGBA", (64, 64), (190, 195, 205, 255))
d = ImageDraw.Draw(wall)
d.rectangle([0, 0, 63, 63], outline=(140, 145, 155), width=2)
# Rodapé na parte inferior
d.rectangle([0, 54, 63, 63], fill=(100, 70, 40))
wall.save(os.path.join(sprites_dir, "school_wall.png"))

# 3. Personagem Detalhado (32x48)
player = Image.new("RGBA", (32, 48), (0, 0, 0, 0))
d = ImageDraw.Draw(player)
# Cabelo castanho
d.rectangle([8, 2, 24, 12], fill=(80, 50, 30))
# Rosto
d.rectangle([10, 12, 22, 20], fill=(255, 220, 177))
# Olhos
d.point([(12, 15), (19, 15)], fill=(0, 0, 0))
# Uniforme Escolar (Camisa branca e colete azul escuro)
d.rectangle([7, 20, 25, 34], fill=(240, 240, 240))
d.rectangle([10, 20, 22, 34], fill=(20, 50, 120)) # colete
# Calça / Pernas
d.rectangle([9, 34, 14, 46], fill=(50, 50, 70))
d.rectangle([18, 34, 23, 46], fill=(50, 50, 70))
player.save(os.path.join(sprites_dir, "player_sprite.png"))

# 4. Mesa / Armário Escolar (60x60)
desk = Image.new("RGBA", (60, 60), (0, 0, 0, 0))
d = ImageDraw.Draw(desk)
d.rectangle([4, 4, 56, 56], fill=(130, 90, 50), outline=(90, 60, 30), width=3)
d.rectangle([10, 10, 50, 50], fill=(150, 110, 70))
# Detalhe de papéis na mesa
d.rectangle([18, 18, 30, 28], fill=(240, 240, 240))
desk.save(os.path.join(sprites_dir, "school_desk.png"))

# 5. Porta de Escola (60x60)
door = Image.new("RGBA", (60, 60), (0, 0, 0, 0))
d = ImageDraw.Draw(door)
d.rectangle([4, 2, 56, 58], fill=(110, 65, 35), outline=(70, 40, 20), width=3)
d.line([10, 2, 10, 58], fill=(80, 45, 20), width=2)
# Maçaneta dourada
d.ellipse([44, 28, 52, 36], fill=(230, 200, 50))
door.save(os.path.join(sprites_dir, "school_door.png"))

print("Sprites detalhados gerados com sucesso.")
