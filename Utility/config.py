import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
from torchvision import transforms as T

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "/content/drive/My Drive/data/train"
VAL_DIR = "/content/drive/My Drive/data/val"
BATCH_SIZE = 1
LEARNING_RATE = 2e-4
LAMBDA_IDENTITY = 0.0
LAMBDA_CYCLE = 10
NUM_WORKERS = 4
NUM_EPOCHS = 200
LOAD_MODEL = True
SAVE_MODEL = True
CHECKPOINT_GEN_SUMMER = "gen_summer.pth.tar"
CHECKPOINT_GEN_WINTER = "gen_winter.pth.tar"
CHECKPOINT_DISC_SUMMER = "disc_summer.pth.tar"
CHECKPOINT_DISC_WINTER = "disc_winter.pth.tar"

transforms = A.Compose(
    [
        A.Resize(width=256, height=256),
        A.HorizontalFlip(p=0.5),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255),
        ToTensorV2(),
     ],
    additional_targets={"image0": "image"},
)

#transforms = T.Compose(
    #[
        #T.Resize(256),
        #T.RandomHorizontalFlip(p=0.5),
        #T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5] ),
        #T.ToTensor(),
     #],
#)