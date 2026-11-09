
import os
from PIL import Image, ImageDraw

sprites_dir = "/home/administrador/Documentos/projetos/escape-room-2d/assets/sprites"

# 6. Quadro Negro (60x40) para Sala de Aula
blackboard = Image.new("RGBA", (60, 40), (20, 40, 30, 255))
d = ImageDraw.Draw(blackboard)
d.rectangle([0, 0, 59, 39], outline=(90, 60, 30), width=3)
d.text((10, 12), "E = 7+5?", fill=(255, 255, 255))
blackboard.save(os.path.join(sprites_dir, "school_blackboard.png"))

# 7. Estante de Livros (60x60) para Biblioteca
bookshelf = Image.new("RGBA", (60, 60), (90, 55, 25, 255))
d = ImageDraw.Draw(bookshelf)
d.rectangle([4, 4, 56, 56], outline=(50, 30, 10), width=3)
d.line([4, 20, 56, 20], fill=(50, 30, 10), width=2)
d.line([4, 40, 56, 40], fill=(50, 30, 10), width=2)
# Livros coloridos nas prateleiras
d.rectangle([10, 8, 16, 18], fill=(200, 50, 50))
d.rectangle([18, 8, 24, 18], fill=(50, 150, 50))
d.rectangle([26, 8, 34, 18], fill=(50, 50, 200))
bookshelf.save(os.path.join(sprites_dir, "school_bookshelf.png"))

# 8. Computador / Bancada de Laboratório (60x60)
lab_bench = Image.new("RGBA", (60, 60), (100, 110, 120, 255))
d = ImageDraw.Draw(lab_bench)
d.rectangle([4, 4, 56, 56], outline=(70, 80, 90), width=3)
d.rectangle([18, 14, 42, 34], fill=(30, 30, 35)) # Monitor
d.rectangle([22, 38, 38, 44], fill=(150, 150, 150)) # Teclado
lab_bench.save(os.path.join(sprites_dir, "school_lab_bench.png"))

print("Sprites adicionais criados com sucesso.")
