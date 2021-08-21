
from pathlib import Path

import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger

import torch

from litmodels import LitModel
from data import PatchDataModule, prepare_data

data_path = Path('data/webcam')
# data is excpected to be in folders:
# data_path /
#           input
#           target
#           mask (optional)

model_save_path = data_path / 'models'

if __name__ == "__main__":

    logger = TensorBoardLogger(Path(), 'lightning_logs')

    profiler = pl.profiler.SimpleProfiler()

    callbacks = []

    train_image_dd = prepare_data(data_path)

    dm = PatchDataModule(train_image_dd,
                         patch_size=2**6,
                         batch_size=2**3,
                         patch_num=2**6)

    model = LitModel( use_adversarial=True)

    # uncomment next line to start from latest checkpoint
    # model = LitModel.load_from_checkpoint(model_save_path/"latest.ckpt")
    
    trainer = pl.Trainer(
        gpus=-1,
        precision=16,
        max_epochs=100,
        log_every_n_steps=8,
        limit_train_batches=1.0,
        limit_val_batches=1.0,
        limit_test_batches=1.0,
        check_val_every_n_epoch=20,
        reload_dataloaders_every_epoch=True,
        profiler=profiler,
        logger=logger,
        callbacks=callbacks,
        # fast_dev_run=True,
    )

    trainer.fit(model, dm)

    trainer.save_checkpoint(model_save_path/"latest.ckpt")
    torch.save(model.generator, model_save_path/"generator.pt")
    torch.save(model.discriminator, model_save_path/"discriminator.pt")
