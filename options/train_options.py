from .base_options import BaseOptions
from util.util import MAX_INT


class TrainOptions(BaseOptions):
    """This class includes training options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)

        # visdom and HTML visualization parameters
        parser.add_argument(
            "--output_display_freq",
            type=int,
            default=400,
            help="frequency of showing training results on screen",
        )
        parser.add_argument(
            "--output_display_ncols",
            type=int,
            default=4,
            help="if positive, display all images in a single visdom web panel with certain number of images per row.",
        )
        parser.add_argument(
            "--output_display_id",
            type=int,
            default=1,
            help="window id of the web display",
        )
        parser.add_argument(
            "--output_display_server",
            type=str,
            default="http://localhost",
            help="visdom server of the web display",
        )
        parser.add_argument(
            "--output_display_env",
            type=str,
            default="main",
            help='visdom display environment name (default is "main")',
        )
        parser.add_argument(
            "--output_display_port",
            type=int,
            default=8097,
            help="visdom port of the web display",
        )
        parser.add_argument(
            "--output_update_html_freq",
            type=int,
            default=1000,
            help="frequency of saving training results to html",
        )
        parser.add_argument(
            "--output_print_freq",
            type=int,
            default=100,
            help="frequency of showing training results on console",
        )
        parser.add_argument(
            "--output_no_html",
            action="store_true",
            help="do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/",
        )

        # training output
        parser.add_argument(
            "--output_display_winsize",
            type=int,
            default=256,
            help="display window size for both visdom and HTML",
        )
        parser.add_argument(
            "--output_display_networks",
            action="store_true",
            help="Set True if you want to display networks on port 8000",
        )
        parser.add_argument(
            "--output_verbose",
            action="store_true",
            help="if specified, print more debugging information",
        )
        parser.add_argument(
            "--output_display_diff_fake_real",
            action="store_true",
            help="if True x - G(x) is displayed",
        )
        parser.add_argument("--output_display_G_attention_masks", action="store_true")

        # network saving and loading parameters
        parser.add_argument(
            "--train_save_latest_freq",
            type=int,
            default=5000,
            help="frequency of saving the latest results",
        )
        parser.add_argument(
            "--train_save_epoch_freq",
            type=int,
            default=1,
            help="frequency of saving checkpoints at the end of epochs",
        )
        parser.add_argument(
            "--train_save_by_iter",
            action="store_true",
            help="whether saves model by iteration",
        )

        parser.add_argument(
            "--train_export_jit",
            action="store_true",
            help="whether to export model in jit format",
        )

        parser.add_argument(
            "--train_continue",
            action="store_true",
            help="continue training: load the latest model",
        )
        parser.add_argument(
            "--train_epoch_count",
            type=int,
            default=1,
            help="the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...",
        )

        # training parameters
        parser.add_argument(
            "--train_batch_size", type=int, default=1, help="input batch size"
        )
        parser.add_argument(
            "--train_epoch",
            type=str,
            default="latest",
            help="which epoch to load? set to latest to use latest cached model",
        )
        parser.add_argument(
            "--train_optim",
            default="adam",
            choices=["adam", "radam", "adamw"],
            help="optimizer (adam, radam, adamw, ...)",
        )
        parser.add_argument(
            "--train_load_iter",
            type=int,
            default=0,
            help="which iteration to load? if load_iter > 0, the code will load models by iter_[load_iter]; otherwise, the code will load models by [epoch]",
        )
        parser.add_argument("--train_compute_fid", action="store_true")
        parser.add_argument("--train_compute_fid_val", action="store_true")
        parser.add_argument("--train_fid_every", type=int, default=1000)
        parser.add_argument(
            "--train_G_ema",
            action="store_true",
            help="whether to build G via exponential moving average",
        )
        parser.add_argument(
            "--train_G_ema_beta",
            type=float,
            default=0.999,
            help="exponential decay for ema",
        )
        parser.add_argument("--train_compute_D_accuracy", action="store_true")
        parser.add_argument("--train_D_accuracy_every", type=int, default=1000)
        parser.add_argument(
            "--train_n_epochs",
            type=int,
            default=100,
            help="number of epochs with the initial learning rate",
        )
        parser.add_argument(
            "--train_n_epochs_decay",
            type=int,
            default=100,
            help="number of epochs to linearly decay learning rate to zero",
        )
        parser.add_argument(
            "--train_beta1", type=float, default=0.9, help="momentum term of adam"
        )
        parser.add_argument(
            "--train_beta2", type=float, default=0.999, help="momentum term of adam"
        )
        parser.add_argument(
            "--train_G_lr",
            type=float,
            default=0.0002,
            help="initial learning rate for generator",
        )
        parser.add_argument(
            "--train_D_lr",
            type=float,
            default=0.0002,
            help="discriminator separate learning rate",
        )
        parser.add_argument(
            "--train_gan_mode",
            type=str,
            default="lsgan",
            choices=["vanilla", "lsgan", "wgangp", "projected"],
            help="the type of GAN objective. vanilla GAN loss is the cross-entropy objective used in the original GAN paper.",
        )
        parser.add_argument(
            "--train_pool_size",
            type=int,
            default=50,
            help="the size of image buffer that stores previously generated images",
        )
        parser.add_argument(
            "--train_lr_policy",
            type=str,
            default="linear",
            choices=["linear", "step", "plateau", "cosine"],
            help="learning rate policy.",
        )
        parser.add_argument(
            "--train_lr_decay_iters",
            type=int,
            default=50,
            help="multiply by a gamma every lr_decay_iters iterations",
        )
        parser.add_argument(
            "--train_nb_img_max_fid",
            type=int,
            default=MAX_INT,
            help="Maximum number of samples allowed per dataset to compute fid. If the dataset directory contains more than nb_img_max_fid, only a subset is used.",
        )
        parser.add_argument(
            "--train_iter_size",
            type=int,
            default=1,
            help="backward will be apllied each iter_size iterations, it simulate a greater batch size : its value is batch_size*iter_size",
        )
        parser.add_argument("--train_use_contrastive_loss_D", action="store_true")

        # multimodal training
        parser.add_argument(
            "--train_mm_lambda_z",
            type=float,
            default=0.5,
            help="weight for random z loss",
        )
        parser.add_argument(
            "--train_mm_nz", type=int, default=8, help="number of latent vectors"
        )

        # train with semantics (for all semantic types)
        parser.add_argument(
            "--train_sem_use_label_B",
            action="store_true",
            help="if true domain B has labels too",
        )

        parser.add_argument(
            "--train_sem_idt",
            action="store_true",
            help="if true apply semantic loss on identity",
        )

        parser.add_argument(
            "--train_sem_net_output",
            action="store_true",
            help="if true apply generator semantic loss on network output for real image rather than on label.",
        )

        # train with cls semantics
        parser.add_argument(
            "--train_semantic_cls",
            action="store_true",
            help="if true semantic class losses will be used",
        )

        parser.add_argument(
            "--train_sem_cls_B",
            action="store_true",
            help="if true cls will be trained not only on domain A but also on domain B",
        )
        parser.add_argument(
            "--train_sem_cls_template",
            type=str,
            help="classifier/regressor model type, from torchvision (resnet18, ...), default is custom simple model",
            default="basic",
        )
        parser.add_argument(
            "--train_sem_cls_pretrained",
            action="store_true",
            help='whether to use a pretrained model, available for non "basic" model only',
        )

        parser.add_argument(
            "--train_cls_regression",
            action="store_true",
            help="if true cls will be a regressor and not a classifier",
        )

        parser.add_argument(
            "--train_sem_lr_cls", type=float, default=0.0002, help="cls learning rate"
        )

        parser.add_argument(
            "--train_sem_cls_lambda",
            type=float,
            default=1.0,
            help="weight for semantic class loss",
        )
        parser.add_argument(
            "--train_cls_l1_regression",
            action="store_true",
            help="if true l1 loss will be used to compute regressor loss",
        )

        # train with mask semantics

        parser.add_argument(
            "--train_sem_lr_f_s", type=float, default=0.0002, help="f_s learning rate"
        )

        parser.add_argument(
            "--train_sem_mask_lambda",
            type=float,
            default=1.0,
            help="weight for semantic mask loss",
        )

        parser.add_argument(
            "--train_semantic_mask",
            action="store_true",
            help="if true semantic mask losses will be used",
        )
        parser.add_argument(
            "--train_mask_f_s_B",
            action="store_true",
            help="if true f_s will be trained not only on domain A but also on domain B",
        )
        parser.add_argument(
            "--train_mask_no_train_f_s_A",
            action="store_true",
            help="if true f_s wont be trained on domain A",
        )
        parser.add_argument(
            "--train_mask_out_mask", action="store_true", help="use loss out mask"
        )
        parser.add_argument(
            "--train_mask_lambda_out_mask",
            type=float,
            default=10.0,
            help="weight for loss out mask",
        )
        parser.add_argument(
            "--train_mask_loss_out_mask",
            type=str,
            default="L1",
            choices=["L1", "MSE", "Charbonnier"],
            help="loss for out mask content (which should not change).",
        )
        parser.add_argument(
            "--train_mask_charbonnier_eps",
            type=float,
            default=1e-6,
            help="Charbonnier loss epsilon value",
        )
        parser.add_argument(
            "--train_mask_disjoint_f_s",
            action="store_true",
            help="whether to use a disjoint f_s with the same exact structure",
        )
        parser.add_argument(
            "--train_mask_for_removal",
            action="store_true",
            help="if true, object removal mode, domain B images with label 0, cut models only",
        )

        parser.add_argument("--train_mask_compute_miou", action="store_true")
        parser.add_argument("--train_mask_miou_every", type=int, default=1000)

        # train with temporal criterion loss
        parser.add_argument(
            "--train_temporal_criterion",
            action="store_true",
            help="if true, MSE loss will be computed between successive frames",
        )

        parser.add_argument(
            "--train_temporal_criterion_lambda",
            type=float,
            default=1.0,
            help="lambda for MSE loss that will be computed between successive frames",
        )

        # train with re-(cycle/cut)
        parser.add_argument(
            "--alg_re_adversarial_loss_p",
            action="store_true",
            help="if True, also train the prediction model with an adversarial loss",
        )
        parser.add_argument(
            "--alg_re_nuplet_size", type=int, default=3, help="Number of frames loaded"
        )
        parser.add_argument(
            "--alg_re_netP",
            type=str,
            default="unet_128",
            choices=[
                "resnet_9blocks",
                "resnet_6blocks",
                "resnet_attn",
                "unet_256",
                "unet_128",
            ],
            help="specify P architecture",
        )
        parser.add_argument(
            "--alg_re_no_train_P_fake_images",
            action="store_true",
            help="if True, P wont be trained over fake images projections",
        )
        parser.add_argument(
            "--alg_re_projection_threshold",
            default=1.0,
            type=float,
            help="threshold of the real images projection loss below with fake projection and fake reconstruction losses are applied",
        )
        parser.add_argument(
            "--alg_re_P_lr",
            type=float,
            default=0.0002,
            help="initial learning rate for P networks",
        )

        # data augmentation
        parser.add_argument(
            "--dataaug_no_flip",
            action="store_true",
            help="if specified, do not flip the images for data augmentation",
        )
        parser.add_argument(
            "--dataaug_no_rotate",
            action="store_true",
            help="if specified, do not rotate the images for data augmentation",
        )
        parser.add_argument(
            "--dataaug_affine",
            type=float,
            default=0.0,
            help="if specified, apply random affine transforms to the images for data augmentation",
        )
        parser.add_argument(
            "--dataaug_affine_translate",
            type=float,
            default=0.2,
            help="if random affine specified, translation range (-value*img_size,+value*img_size) value",
        )
        parser.add_argument(
            "--dataaug_affine_scale_min",
            type=float,
            default=0.8,
            help="if random affine specified, min scale range value",
        )
        parser.add_argument(
            "--dataaug_affine_scale_max",
            type=float,
            default=1.2,
            help="if random affine specified, max scale range value",
        )
        parser.add_argument(
            "--dataaug_affine_shear",
            type=int,
            default=45,
            help="if random affine specified, shear range (0,value)",
        )
        parser.add_argument(
            "--dataaug_imgaug",
            action="store_true",
            help="whether to apply random image augmentation",
        )
        parser.add_argument(
            "--dataaug_diff_aug_policy",
            type=str,
            default="",
            help="choose the augmentation policy : color randaffine randperspective. If you want more than one, please write them separated by a comma with no space (e.g. color,randaffine)",
        )
        parser.add_argument(
            "--dataaug_diff_aug_proba",
            type=float,
            default=0.5,
            help="proba of using each transformation",
        )

        # adaptive pseudo augmentation using G
        parser.add_argument(
            "--dataaug_APA",
            action="store_true",
            help="if true, G will be used as augmentation during D training adaptively to D overfitting between real and fake images",
        )
        parser.add_argument("--dataaug_APA_target", type=float, default=0.6)
        parser.add_argument(
            "--dataaug_APA_p",
            type=float,
            default=0,
            help="initial value of probability APA",
        )
        parser.add_argument(
            "--dataaug_APA_every",
            type=int,
            default=4,
            help="How often to perform APA adjustment?",
        )
        parser.add_argument(
            "--dataaug_APA_nimg",
            type=int,
            default=50,
            help="APA adjustment speed, measured in how many images it takes for p to increase/decrease by one unit.",
        )

        # augmentation using D
        parser.add_argument(
            "--dataaug_D_label_smooth",
            action="store_true",
            help="whether to use one-sided label smoothing with discriminator",
        )
        parser.add_argument(
            "--dataaug_D_noise",
            type=float,
            default=0.0,
            help="whether to add instance noise to discriminator inputs",
        )

        self.isTrain = True
        return parser
