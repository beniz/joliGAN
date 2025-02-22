import os.path
from data.unaligned_labeled_mask_online_dataset import UnalignedLabeledMaskOnlineDataset
from data.online_creation import fill_mask_with_random, fill_mask_with_color
from PIL import Image
import numpy as np
import torch
import warnings


class SelfSupervisedLabeledMaskOnlineDataset(UnalignedLabeledMaskOnlineDataset):
    """
    This dataset class can create datasets with mask labels from one domain.
    """

    def __init__(self, opt):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        super().__init__(opt)

    def get_img(
        self,
        A_img_path,
        A_label_mask_path,
        A_label_cls,
        B_img_path=None,
        B_label_mask_path=None,
        B_label_cls=None,
        index=None,
    ):
        result = super().get_img(
            A_img_path,
            A_label_mask_path,
            A_label_cls,
            B_img_path,
            B_label_mask_path,
            B_label_cls,
            index,
        )

        if self.opt.data_online_creation_rand_mask_A:
            A_img = fill_mask_with_random(result["A"], result["A_label_mask"], -1)
        elif self.opt.data_online_creation_color_mask_A:
            A_img = fill_mask_with_color(result["A"], result["A_label_mask"], {})
        else:
            raise Exception(
                "self supervised dataset: no self supervised method specified"
            )

        result.update(
            {
                "A": A_img,
                "B": result["A"],
                "B_img_paths": result["A_img_paths"],
                "B_label_mask": result["A_label_mask"].clone(),
            }
        )
        return result
