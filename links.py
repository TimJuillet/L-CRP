import glob
from pathlib import Path

def create_dataset_txt():
    # Créer les chemins de base
    coco_path = Path('datasets/coco2017/coco')
    
    # Pour train2017
    print("Creating train2017.txt...")
    with open(coco_path / 'train2017.txt', 'w') as f:
        images = glob.glob(str(coco_path / 'images/train2017/*.jpg'))
        for img_path in images:
            f.write(f'{img_path}\n')
            
    # Pour val2017
    print("Creating val2017.txt...")
    with open(coco_path / 'val2017.txt', 'w') as f:
        images = glob.glob(str(coco_path / 'images/val2017/*.jpg'))
        for img_path in images:
            f.write(f'{img_path}\n')
    
    print("Done!")

if __name__ == '__main__':
    create_dataset_txt()